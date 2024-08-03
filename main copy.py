import os
import sys
import json
import traceback

from moviepy.editor import VideoFileClip, AudioFileClip
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QFileDialog
from pytube import YouTube, Stream, StreamQuery
from ui_pytube import Ui_MainWindow
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Youtube do Py')

        self.dir_download: str | None = self.buscar_diretorio()
        self.dir_temp: str = os.getcwd() + r'\temp'
        
        self.btn_pesquisar.clicked.connect(self.info_url)
        
        self.btn_baixar_video.clicked.connect(self.baixar_video)
        self.btn_baixar_audio.clicked.connect(self.baixar_audio)
        

    def buscar_diretorio(self) -> str | None:
        """
        Verifica se existe um diretório informado no arquivo 'dados.json'.

        Retorna: 
            str: O diretório informado pelo usuário, se encontrado.
            None: Se nenhum diretório for fornecido ou se o arquivo 'dados.json' não existir.
        
        Notas:
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
        Se o usuário selecionar um diretório, este é salvo no arquivo 'dados.json' e retorna True.
        Se o usuário não selecionar um diretório, exibe uma mensagem de erro e retorna False.

        Retorna:
            bool: True se um diretório válido estiver definido. Caso contrário, False.

        Notas:
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
        Pega o texto fornecido pelo usuário na caixa de texto de pesquisa.
        Caso seja um link do Youtube válido, busca as informações e as exibe na página.
        Alterna para a página de carregamento e volta para a página de vídeo assim que este for carregado.
        """
        pesquisa: str = self.input_pesquisa.text()
        if not pesquisa:
            return

        self.qthread = QThread()
        self.worker = Worker(pesquisa=pesquisa)

        self.worker.moveToThread(self.qthread)

        # Conectar Sinais e Slots
        self.qthread.started.connect(self.worker.info_url)
        self.worker.terminado.connect(self.qthread.quit)
        self.worker.terminado.connect(self.worker.deleteLater)
        self.qthread.finished.connect(self.qthread.deleteLater)

        self.worker.url.connect(self.informacoes_video)

        self.qthread.start()

        self.paginas.setCurrentWidget(self.pag_carregando)


    def informacoes_video(self, video:YouTube | str):
        if type(video) is str:
            if video == 'regex_search':
                QMessageBox.warning(self, 'Erro', 'Você não forneceu um link válido.')
            else:
                QMessageBox.critical(self, 'Erro', 'Ocorreu um erro ao tentar pesquisar seu vídeo.\nPor favor, tente novamente.')
                self.loggar_erro(video)
            return

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
        
        self.qualidade_audio.addItems(audios)
        self.qualidade_video.addItems(videos)
    
        self.input_pesquisa.clear()
        self.paginas.setCurrentWidget(self.pag_video)


    def baixar_video(self) -> None:
        """
        Baixa o vídeo selecionado e o salva no diretório definido.

        Se o diretório não existir, solicita que o usuário selecione um diretório.
        Baixa o vídeo em duas partes (vídeo e áudio) e as mescla em um arquivo único.
        Se ocorrer um erro durante o processo, exibe uma mensagem de erro e registra o erro no log.

        Notas:
            O diretório temporário é criado para armazenar os arquivos de vídeo e áudio durante o processo. 
            O arquivo de vídeo final é salvo no diretório definido pelo usuário.
        """
        if not self.diretorio_existe():
            return

        qualidade_video: str = self.qualidade_video.currentText()
        video_stream: StreamQuery = self.video.streams.filter(mime_type='video/mp4', res=qualidade_video, only_video=True)

        qualidade_audio: str = self.qualidade_audio.currentText()
        audio_stream: StreamQuery = self.video.streams.filter(mime_type='audio/mp4', abr=qualidade_audio, only_audio=True)

        if not os.path.exists(self.dir_temp):
            os.mkdir(self.dir_temp)

        titulo: str = video_stream.first().title
        
        try:
            # Baixa o vídeo e o áudio separadamente no diretório temporário
            video: str = video_stream.first().download(self.dir_temp, titulo+'.mp4')
            audio: str = audio_stream.first().download(self.dir_temp, titulo+'.mp3')
        except Exception as e:
            self.loggar_erro(e)
            QMessageBox.critical(self, 'Erro', 'Ocorreu um erro ao baixar o vídeo.\nPor favor, tente novamente mais tarde.')

        try:
            # Mescla o vídeo e o áudio baixados em um único arquivo
            video_clip = VideoFileClip(video)
            audio_clip = AudioFileClip(audio)

            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(titulo+'.mp4', codec="libx264")

            video_clip.close()
            audio_clip.close()
            final_clip.close()
        except Exception as e:
            self.loggar_erro(e)
            # Remover arquivos temporários
            os.remove(video)
            os.remove(audio)
            os.rmdir(self.dir_temp)
            QMessageBox.critical(self, 'Erro', 'Ocorreu um erro ao baixar o vídeo.\nPor favor, tente novamente mais tarde.')

        # Remover arquivos temporários
        os.remove(video)
        os.remove(audio)
        os.rmdir(self.dir_temp)

        # Move o novo arquivo para o diretório fornecido pelo usuário
        file_path: str = os.getcwd()
        os.rename(rf'{file_path}\{titulo}.mp4', rf'{self.dir_download}\{titulo}.mp4')

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
       
        
    def baixar_audio(self) -> None:
        """
        Baixa o áudio selecionado e o salva no diretório definido pelo usuário.

        Se o diretório não existir, solicita que o usuário selecione um diretório.
        """
        
        if not self.diretorio_existe():
            return
                
        qualidade_audio: str = self.qualidade_audio.currentText()
        audio: StreamQuery = self.video.streams.filter(mime_type='audio/mp4', abr=qualidade_audio, only_audio=True)
        
        try:
            # Baixa o áudio no diretório de download fornecido pelo usuário
            audio.first().download(output_path=self.dir_download)
        except Exception as e:
            self.loggar_erro(e)
            QMessageBox.critical(self, 'Erro', 'Ocorreu um erro ao baixar o áudio.\nPor favor, tente novamente mais tarde.')
        
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


    def loggar_erro(self, e: Exception) -> None:
        """
        Grava o erro em um arquivo para debug.
        """
        with open('error.txt', 'w', encoding='utf-8') as file:
            file.write(str(e))

        with open("erro.log", "a", encoding='utf-8') as f:
            f.write(f"Erro: {e}\n")
            f.write(traceback.format_exc() + "\n")


class Worker(QObject):
    progresso = Signal(str) # Sinal que vai emitir o progresso atual
    terminado = Signal() # Sinal que vai emitir quando o processo encerrar
    url = Signal(YouTube) # Sinal que vai emitir o objeto Youtube

    def __init__(self, *, pesquisa:str = None) -> None:
        super().__init__()
    
        self.pesquisa: str = pesquisa

    
    def info_url(self):
        try:
            video = YouTube(self.pesquisa)
            self.url.emit(video)

        except Exception as e:
            if str(e).startswith('regex_search'):
                self.url.emit('regex_search')
            else:
                self.url.emit('erro')
        self.terminado.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    