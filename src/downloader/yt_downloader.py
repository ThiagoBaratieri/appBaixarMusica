import re
import yt_dlp


def download_audio(youtube_url, output_path="downloads/"):
    """
    Faz o download do áudio de um vídeo do YouTube.

    Args:
        youtube_url (str): URL do vídeo do YouTube.
        output_path (str): Caminho para salvar o arquivo baixado (padrão: 'downloads/').

    Returns:
        str: Caminho do arquivo baixado.
    """
    
    # 1. Validar o link do YouTube
    padrao = r"^(https:\/\/(www\.)?youtube\.com\/watch\?v=[A-Za-z0-9_-]+|https:\/\/youtu\.be\/[A-Za-z0-9_-]+)$" # REGEX
    if not re.match(padrao, youtube_url):
        return "URL Inválida ou Inexistente. Forneça um link válido do youtube"

    
    # 2. Obter o vídeo com o pytube
    ydl_opts = {
        'format': 'bestaudio/best',  # Melhor qualidade de áudio disponível
        'extractaudio': True,  # Extrair apenas o áudio
        'audioquality': 1,  # Melhor qualidade
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Caminho e nome do arquivo
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        return f"Audio baixado com sucesso! Arquivo salvo em: {output_path}"
    except Exception as e:
        return f"Erro ao baixar audio: {e}"



print(download_audio("https://www.youtube.com/watch?v=BM-mnklMWCQ"))