import os
import sys
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QFileDialog
from pytube import YouTube, Stream, StreamQuery
from ui_pytube import Ui_MainWindow
from pytube.innertube import _default_clients

from ytvideo import YTVideo

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Youtube do Py')

        self.diretorio: str | None = self.buscar_diretorio()
        
        self.btn_pesquisar.clicked.connect(self.info_url)
        
        self.btn_baixar_video.clicked.connect(self.baixar_video)
        self.btn_baixar_audio.clicked.connect(self.baixar_audio)
        

    def buscar_diretorio(self) -> str | None:
        if os.path.exists('dados.json'):
            with open("dados.json", mode="r", encoding="utf-8") as f:
                dados = json.load(f)
                return dados['dir']
        
    
    def info_url(self) -> None:
        pesquisa: str = self.input_pesquisa.text()
        try:
            self.video = YouTube(pesquisa)
        except Exception as e:
            QMessageBox.critical(self, 'Erro', 'Ocorreu um erro ao tentar pesquisar seu vídeo.\nPor favor, tente novamente.')
            return

        # INFO
        duracao: int = self.video.length
        mins: int = duracao // 60
        secs: int = duracao % 60
        
        self.nome_video.setText(self.video.title)
        self.label_nome_autor.setText(f'Por: {self.video.author}') 
        self.label_duracao.setText(f'Duração: {mins:02}:{secs:02}')
        self.label_views.setText(f'Views: {self.video.views:,}')
        
        # STREAMS
        filtro_audio: StreamQuery = self.video.streams.filter(mime_type='audio/mp4')
        filtro_video: StreamQuery = self.video.streams.filter(mime_type='video/mp4') # filtro progressive não funciona

        audios: list[Stream] = [stream.abr for stream in filtro_audio]
        videos: list[Stream] = [stream.resolution for stream in filtro_video]
        videos.pop(0)
        
        self.qualidade_audio.addItems(audios)
        self.qualidade_video.addItems(videos)
    
        self.input_pesquisa.clear()
    
        
    def baixar_video(self):
        # TODO: fazer a função funcionar baixando o áudio e o vídeo para mesclar depois
        ...
       
        
    def baixar_audio(self):
        if not self.diretorio:
            QMessageBox.warning(self, 'Diretório', 'Você não tem uma pasta definida para salvar seus aúdios e vídeos! Por favor, selecione uma pasta na próxima janela ao clicar em "OK".')

            diretorio: str = QFileDialog.getExistingDirectory(self, 'Pasta')
            if diretorio:
                self.diretorio: str = diretorio
                with open("dados.json", mode="w", encoding="utf-8") as f:
                    json.dump({'dir': diretorio}, f)
            else:
                QMessageBox.critical(self, 'Diretório', 'Você não informou um diretório. Por favor, reinicie o procedimento e tente novamente.')
                return
                
        qualidade_audio: str = self.qualidade_audio.currentText()
        try:
            YTVideo.baixar_audio(self.video, qualidade_audio, self.diretorio)
        except Exception as e:
            self.loggar_erro(e)
            QMessageBox.critical(self, 'Erro','Ocorreu um erro ao baixar o áudio.\nPor favor, tente novamente.')
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Áudio')
            msg.setText('O áudio foi baixado com sucesso! Gostaria de acessar a pasta?')
            msg.addButton('Não', QMessageBox.NoRole) # == 0
            btn_padrao: QPushButton = msg.addButton('Sim', QMessageBox.YesRole) # == 1
            
            msg.setDefaultButton(btn_padrao)
            opcao: int = msg.exec()
            
            if opcao == 1: # 1 == Sim
                os.startfile(self.diretorio)


    def loggar_erro(self, e: Exception):
        with open('error.txt', 'w', encoding='utf-8') as f:
            f.write(e)

         
    def exibir_msg(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Áudio')
        msg.setText('O áudio foi baixado com sucesso! Gostaria de acessar a pasta?')
        
        msg.addButton('Não', QMessageBox.NoRole)
        btn_padrao: QPushButton = msg.addButton('Sim', QMessageBox.YesRole)
        
        msg.setDefaultButton(btn_padrao)
        opcao: int = msg.exec()
        
        # 0 == Não ; 1 == Sim
        if opcao == 1:
            print('Sim')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()