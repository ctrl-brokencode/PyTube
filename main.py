import os
import sys
import json

from proglog import ProgressBarLogger
from moviepy.editor import VideoFileClip, AudioFileClip
from PySide6.QtCore import QObject, QThread, Signal, SignalInstance, QRunnable, QThreadPool
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QFileDialog
from pytube import YouTube, Stream, StreamQuery
from pytube.exceptions import RegexMatchError
from pytube.innertube import _default_clients

from ui_pytube import Ui_MainWindow

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Youtube do Py')

        self.dir_download: str | None = self.buscar_diretorio()
        self.dir_temp: str = os.path.join(os.getcwd(), 'temp')
        
        self.btn_pesquisar.clicked.connect(self.info_url)
        
        self.btn_baixar_video.clicked.connect(self.baixar_video)
        self.btn_baixar_audio.clicked.connect(self.baixar_audio)
        

    def buscar_diretorio(self) -> str | None:
        """
        Verifica se existe um diretório informado no arquivo 'dados.json'.

        ### Retorna: 
            str: O diretório informado pelo usuário.
            None: Se nenhum diretório for fornecido ou se o arquivo 'dados.json' não existir.
        
        ### Notas:
            O arquivo 'dados.json' deve estar no formato JSON válido e conter a chave 'dir' com o valor do diretório.
        """

        if os.path.exists('dados.json'):
            with open('dados.json', mode='r', encoding='utf-8') as file:
                dados = json.load(file)
                return dados.get('dir')
        

    def diretorio_existe(self) -> bool:
        """
        Verifica se um diretório de download de arquivo é válido e definido.

        Se não houver um diretório, exibe uma mensagem de aviso e solicita que o usuário defina um diretório.
        - Se o usuário selecionar um diretório, este é salvo no arquivo 'dados.json' e retorna `True`.
        - Se o usuário não selecionar um diretório, exibe uma mensagem de erro e retorna `False`.

        ### Notas:
            O arquivo 'dados.json' é criado ou atualizado com o diretório selecionado pelo usuário.
        """

        if not self.dir_download:
            QMessageBox.warning(self, 'Diretório', 'Você não tem uma pasta definida para salvar seus aúdios e vídeos! Por favor, selecione uma pasta na próxima janela ao clicar em "OK".')

            diretorio: str = QFileDialog.getExistingDirectory(self, 'Pasta')
            if diretorio:
                self.dir_download: str = diretorio
                with open("dados.json", mode="w", encoding="utf-8") as file:
                    json.dump({'dir': diretorio}, file)
                return True
            else:
                QMessageBox.critical(self, 'Diretório', 'Você não informou um diretório. Por favor, reinicie o procedimento e tente novamente.')
                return False
        else:
            return True

    
    def info_url(self) -> None:
        """
        Busca o vídeo a partir da pesquisa fornecida pelo usuário na caixa de texto de pesquisa.
        
        Caso seja um link do Youtube válido, alterna para a página de carregamento, busca as informações e as exibe na página, voltando para a página de vídeo assim que este for carregado.
        Caso contrário, nada acontece.
        """

        pesquisa: str = self.input_pesquisa.text()
        if not pesquisa:
            return

        self.sinal = Signals()
        self.sinal.url.connect(self.informacoes_video)
        self.sinal.erro.connect(self.registrar_erro)
        
        self.progresso.hide()
        self.paginas.setCurrentWidget(self.pag_carregando)
        
        runnable = InfoUrlRunnable(pesquisa, self.sinal.url, self.sinal.erro)
        QThreadPool.globalInstance().start(runnable)


    def informacoes_video(self, video:YouTube | str) -> None:
        """
        Processa e registra informações recebidas pelo sinal emitido pela variável url da classe Signals.

        O sinal pode emitir dois tipos diferentes: um objeto `Youtube` ou uma `string`.

        ### Sinais emitidos: 
            :Youtube: As informações serão exibidas na página de vídeo.
            :str: Algum erro ocorreu.
        """

        ### CHECAGEM DO SINAL EMITIDO
        if not isinstance(video, YouTube):
            if str(video) == 'regex_search':
                QMessageBox.warning(self, 'Erro', 'Você não forneceu um link válido.')
            else:
                QMessageBox.critical(self, 'Erro', 'Ocorreu um erro ao tentar pesquisar seu vídeo.\nPor favor, tente novamente.')
                self.loggar_erro(video)
            self.paginas.setCurrentWidget(self.pag_video)
            return

        ### REGISTRAR INFORMAÇÕES        
        self.video: YouTube = video
        
        duracao: int = self.video.length
        mins: int = duracao // 60
        secs: int = duracao % 60
        
        self.nome_video.setText(self.video.title)
        self.label_nome_autor.setText(f'Por: {self.video.author}') 
        self.label_duracao.setText(f'Duração: {mins:02}:{secs:02}')
        self.label_views.setText(f'Views: {self.video.views:,}')
        
        ### STREAMS
        filtro_audio: StreamQuery = self.video.streams.filter(mime_type='audio/mp4', only_audio=True)
        filtro_video: StreamQuery = self.video.streams.filter(mime_type='video/mp4', only_video=True)

        audios: list[Stream] = [stream.abr for stream in filtro_audio]
        videos: list[Stream] = [stream.resolution for stream in filtro_video]

        ### REGISTRAR AS STREAMS
        self.qualidade_audio.clear()
        self.qualidade_video.clear()
        
        self.qualidade_audio.addItems(audios)
        self.qualidade_video.addItems(videos)
        
        ### RESETS
        self.input_pesquisa.clear()
        self.paginas.setCurrentWidget(self.pag_video)


    def baixar_video(self) -> None:
        """
        Baixa o vídeo selecionado e o salva no diretório definido.

        Se o diretório não existir, solicita que o usuário selecione um diretório.
        Primeiro, o programa baixa o vídeo e o áudio e os mescla em um arquivo único.
        Se ocorrer um erro durante o processo, exibe uma mensagem de erro e registra o erro no log.

        Notas:
            O diretório temporário é criado para armazenar os arquivos de vídeo e áudio durante o processo. 
            O arquivo de vídeo final é salvo no diretório definido pelo usuário.
        """
        if not self.diretorio_existe():
            return

        qualidade_video: str = self.qualidade_video.currentText()
        video: StreamQuery = self.video.streams.filter(mime_type='video/mp4', res=qualidade_video, only_video=True)

        qualidade_audio: str = self.qualidade_audio.currentText()
        audio: StreamQuery = self.video.streams.filter(mime_type='audio/mp4', abr=qualidade_audio, only_audio=True)

        if not os.path.exists(self.dir_temp):
            os.mkdir(self.dir_temp)

        def concluido() -> None:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Vídeo')
            msg.setText('O vídeo foi baixado com sucesso! Gostaria de acessar a pasta?')
            msg.addButton('Não', QMessageBox.NoRole) # == 0
            btn_padrao: QPushButton = msg.addButton('Sim', QMessageBox.YesRole) # == 1
            
            msg.setDefaultButton(btn_padrao)
            opcao: int = msg.exec()
            
            if opcao == 1: # 1 == 'Sim'
                os.startfile(self.dir_download)

            self.paginas.setCurrentWidget(self.pag_video)

        ### DEFINIR PÁGINA
        self.paginas.setCurrentWidget(self.pag_carregando)
        self.progresso.show()
        self.progresso.setValue(0)

        ### THREAD SEPARADA PARA EXECUÇÃO DO DOWNLOAD
        self.thread_video = QThread()
        self.worker_video = DownloadVideoWorker(video, audio, self.dir_download, self.dir_temp)
        self.worker_video.moveToThread(self.thread_video)

        ### REGISTRAR FUNÇÃO DE PROGRESSO
        self.video.register_on_progress_callback(self.worker_video.progress_callback)

        ### CONECTAR SLOTS E SIGNALS
        self.thread_video.started.connect(self.worker_video.run)
        self.worker_video.erro.connect(self.registrar_erro)
        
        self.worker_video.sucesso.connect(concluido)
        self.worker_video.terminado.connect(self.thread_video.quit)
        self.worker_video.terminado.connect(self.worker_video.deleteLater)
        self.thread_video.finished.connect(self.thread_video.deleteLater)
        self.worker_video.progresso.connect(self.definir_valor_progresso)
        
        self.thread_video.start()
       
        
    def baixar_audio(self) -> None:
        """
        Baixa o áudio selecionado e o salva no diretório definido pelo usuário.

        Se o diretório não existir, solicita que o usuário selecione um diretório.
        Se ocorrer um erro durante o processo, exibe uma mensagem de erro e registra o erro no log.
        """
        
        if not self.diretorio_existe():
            return
                
        qualidade_audio: str = self.qualidade_audio.currentText()
        audio: StreamQuery = self.video.streams.filter(mime_type='audio/mp4', abr=qualidade_audio, only_audio=True)

        ### DEFINIR PÁGINA
        self.paginas.setCurrentWidget(self.pag_carregando)
        self.progresso.show()
        self.progresso.setValue(0)
        
        def concluido():
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Áudio')
            msg.setText('O áudio foi baixado com sucesso! Gostaria de acessar a pasta?')
            msg.addButton('Não', QMessageBox.NoRole) # == 0
            btn_padrao: QPushButton = msg.addButton('Sim', QMessageBox.YesRole) # == 1
            
            msg.setDefaultButton(btn_padrao)
            opcao: int = msg.exec()
            
            if opcao == 1: # 1 == 'Sim'
                os.startfile(self.dir_download)

            self.paginas.setCurrentWidget(self.pag_video)

        ### THREAD SEPARADA PARA EXECUÇÃO DO DOWNLOAD
        self.thread_audio = QThread()
        self.worker_audio = DownloadAudioWorker(audio, self.dir_download)
        self.worker_audio.moveToThread(self.thread_audio)

        ### REGISTRAR FUNÇÃO DE PROGRESSO
        self.video.register_on_progress_callback(self.worker_audio.progress_callback)

        ### CONECTAR SLOTS E SIGNALS
        self.thread_audio.started.connect(self.worker_audio.run)
        self.worker_audio.progresso.connect(self.definir_valor_progresso)
        self.worker_audio.erro.connect(self.registrar_erro)
        self.worker_audio.sucesso.connect(concluido)
        
        self.worker_audio.terminado.connect(self.thread_audio.quit)
        self.worker_audio.terminado.connect(self.worker_audio.deleteLater)
        self.thread_audio.finished.connect(self.thread_audio.deleteLater)
        
        self.thread_audio.start()


    def definir_valor_progresso(self, value:int) -> None:
        self.progresso.setValue(value)


    def registrar_erro(self, erro:str, exception: Exception):
        erro_tecnico = False
        # FIXME: trocar essas frases genéricas 
        match erro:
            case 'regex':
                QMessageBox.critical(self, 'Pesquisa', 'Você não forneceu um link válido. Por favor, insira um link vindo do Youtube e tente novamente.')
            case 'download':
                QMessageBox.critical(self, 'Download', 'Ocorreu um erro ao baixar o vídeo.\nPor favor, tente novamente mais tarde.')
                erro_tecnico = True
            case 'render_video':
                QMessageBox.critical(self, 'Renderização', 'Ocorreu um erro ao renderizar o vídeo.\nPor favor, tente novamente mais tarde.')
                erro_tecnico = True
            
        self.paginas.setCurrentWidget(self.pag_video)

        if erro_tecnico:
            with open('error.log', 'a', encoding='utf-8') as file:
                file.write(str(exception))


class Signals(QObject):
    url = Signal(YouTube)
    erro = Signal(str, Exception)

    progresso = Signal(int)


class InfoUrlRunnable(QRunnable):
    def __init__(self, pesquisa:str, sinal: SignalInstance, erro: SignalInstance) -> None:
        super().__init__()

        self.pesquisa: str = pesquisa
        self.sinal: SignalInstance = sinal
        self.erro: SignalInstance = erro


    def run(self) -> None:
        try:
            video = YouTube(self.pesquisa)
            self.sinal.emit(video)

        except RegexMatchError as e:
            self.erro.emit('regex', e)

        except Exception as e:
            self.erro.emit('video_nao_encontrado', e)


class DownloadAudioWorker(QObject):
    progresso = Signal(int)
    erro = Signal(str, Exception)
    terminado = Signal()
    sucesso = Signal()


    def __init__(self, audio: StreamQuery, dir_download: str) -> None:
        super().__init__()
        self.audio: StreamQuery = audio
        self.dir_download: str = dir_download


    def progress_callback(self, stream: StreamQuery, _, bytes_restantes: int) -> None:
        tamanho_em_bytes: float = stream.filesize
        porcentagem = int(((tamanho_em_bytes - bytes_restantes) / tamanho_em_bytes) * 100)
        self.progresso.emit(porcentagem)


    def run(self) -> None:
        try:
            # Baixa o áudio no diretório de download fornecido pelo usuário
            self.audio.first().download(output_path=self.dir_download)
        except Exception as e:
            self.erro.emit('download', e)
        else:
            self.sucesso.emit()
        finally:
            self.terminado.emit()


class DownloadVideoWorker(QThread):
    progresso = Signal(int)
    erro = Signal(str, Exception)
    terminado = Signal()
    sucesso = Signal()


    def __init__(self, video: StreamQuery, audio: StreamQuery, dir_download: str, dir_temp: str) -> None:
        super().__init__()   
        self.video: StreamQuery = video
        self.audio: StreamQuery = audio
        self.dir_download: str = dir_download
        self.dir_temp: str = dir_temp


    def progress_callback(self, stream: StreamQuery, _, bytes_restantes: int) -> None:
        """Emite um sinal com a porcentagem atual do download do video."""
        tamanho_em_bytes: float = stream.filesize
        porcentagem = int(((tamanho_em_bytes - bytes_restantes) / tamanho_em_bytes) * 100)
        self.progresso.emit(porcentagem)


    def run(self) -> None:
        titulo: str = self.video.first().title
        try:
            video: str = self.video.first().download(self.dir_temp, titulo+'.mp4')
            audio: str = self.audio.first().download(self.dir_temp, titulo+'.mp3')

        except OSError as e:
            # Erro de nome de arquivo
            titulo = titulo.replace('|', '-')

            try:
                video: str = self.video.first().download(self.dir_temp, titulo+'.mp4')
                audio: str = self.audio.first().download(self.dir_temp, titulo+'.mp3')
            except Exception as e:
                print('Erro 2')
            
        except Exception as e:
            self.erro.emit('download', e)
            return

        logger = MyBarLogger(self.progresso)

        try:
            # Mescla o vídeo e o áudio baixados em um único arquivo
            video_clip = VideoFileClip(video)
            audio_clip = AudioFileClip(audio)
            final_clip: VideoFileClip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(titulo+'.mp4', codec='libx264', logger=logger)

        except Exception as e:
            self.erro.emit('render_video', e)

        else:
            # Move o novo arquivo para o diretório fornecido pelo usuário
            file_path: str = os.getcwd()
            os.rename(os.path.join(file_path, titulo+'.mp4'),
                    os.path.join(self.dir_download, titulo+'.mp4'))
            self.sucesso.emit()
            
        finally:
            video_clip.close()
            audio_clip.close()
            final_clip.close()
            # Remover arquivos temporários
            os.remove(video)
            os.remove(audio)
            os.rmdir(self.dir_temp)
            self.terminado.emit()
            

class MyBarLogger(ProgressBarLogger):
    def __init__(self, sinal: SignalInstance):
        super().__init__()
        self.sinal: SignalInstance = sinal
        
    
    def callback(self, **changes) -> None:
        """Toda vez que a mensagem do logger é atualizada, a função é chamada com o dicionário `changes`
        """
        
        for (parameter, value) in changes.items():
            print ('Parameter %s is now %s' % (parameter, value))

    
    def bars_callback(self, bar, _, value, old_value=None) -> None:
        """Printa a porcentagem atual do progresso. A função é chamada toda vez que o progresso atualizar.
        """
        
        porcentagem: float = (value / self.bars[bar]['total']) * 100
        self.sinal.emit(int(porcentagem))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    