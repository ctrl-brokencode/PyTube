import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from pytube import YouTube
from ui_pytube import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Youtube do Py')
        
        self.video: YouTube = None
        
        self.btn_pesquisar.clicked.connect(self.pesquisar)
        
        self.btn_baixar_video.clicked.connect(self.baixar_video)
        self.btn_baixar_audio.clicked.connect(self.baixar_audio)
        
    
    def pesquisar(self):
        pesquisa = self.input_pesquisa.text()
        
        if pesquisa.startswith('https'):
            self.info_url(pesquisa)
        else:
            print('Você forneceu uma pesquisa.')
            
    
    def info_url(self, url:str):
        self.video = YouTube(url=url)
        self.nome_video.setText(self.video.title)
        self.label_nome_autor.setText(f'Por: {self.video.author}') 
        self.label_duracao.setText(f'Duração: {self.video.length}') # TODO: tratar os segundos para que sejam minutos
        self.label_views.setText(f'Views: {self.video.views}')
        self.input_pesquisa.clear()
        
        
    def baixar_video(self):
        filtro = self.video.streams.filter(progressive=True)
        if len(filtro) == 1:
            print(filtro.get_highest_resolution().filesize_mb)
            filtro.get_highest_resolution().download()
            print('Vídeo baixado!')
        # TODO: dar um jeito de colocar um else, provavelmente um dropdown no app
       
        
    def baixar_audio(self):
        self.video.streams.get_audio_only().download()
        print('Áudio baixado!')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()