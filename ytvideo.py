from pytube import YouTube, Stream
from pytube.query import StreamQuery

class YTVideo:
    def baixar_audio(video:YouTube, qualidade:str, diretorio:str):
        filtro_audio: StreamQuery = video.streams.filter(mime_type='audio/mp4')
        
        audio: StreamQuery = filtro_audio.filter(abr=qualidade)
        
        audio.first().download(output_path=diretorio)
        
            
        
        