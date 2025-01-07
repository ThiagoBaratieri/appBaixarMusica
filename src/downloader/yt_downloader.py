import os
import re
import yt_dlp

def validar_url(youtube_url):
    """
    Valida se o link fornecido é um link válido do YouTube.
    
    Args:
        youtube_url (str): URL do vídeo do YouTube.
    
    Returns:
        bool: True se o link for válido, False caso contrário.
    """

    padrao = r"^(https:\/\/(www\.)?youtube\.com\/watch\?v=[A-Za-z0-9_-]+|https:\/\/youtu\.be\/[A-Za-z0-9_-]+)$" # Regex
    return re.match(padrao, youtube_url) is not None


def criar_diretorio(diretorio):
    """
    Verifica se o diretório existe. Se não, cria o diretório.
    
    Args:
        diretorio (str): Caminho do diretório a ser verificado/criado.
    """

    if not os.path.exists(diretorio):
        os.makedirs(diretorio)


def download_audio(youtube_url, output_path="downloads/", format_audio="mp3"):
    """
    Faz o download do áudio de um vídeo do YouTube.

    Args:
        youtube_url (str): URL do vídeo do YouTube.
        output_path (str): Caminho para salvar o arquivo baixado (padrão: 'downloads/').

    Returns:
        str: Caminho do arquivo baixado.
    """

    # Validar URL
    if not validar_url(youtube_url):
        return "URL Inválida ou Inexistente. Forneça um link válido do youtube"
  
    # Criar diretorio se ele nao existir
    criar_diretorio(output_path)

    output_template = f'{output_path}%(title)s.{format_audio}'

    # Config para download do audio
    ydl_opts = {
        'format': 'bestaudio/best',  # Melhor qualidade de áudio disponível
        'extractaudio': True,  # Extrair apenas o áudio
        'audioquality': 1,  # Melhor qualidade
        'outtmpl': output_template,  # Caminho e nome do arquivo

    }

    # Verificar se o arquivo ja existe antes de baixa-lo
    nome_arquivo = f"{output_path}/{yt_dlp.YoutubeDL(ydl_opts).extract_info(youtube_url, download=False)['title']}.{format_audio}"
    if os.path.exists(nome_arquivo):
        return "Este audio ja foi baixado anteriormente"


    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Iniciando Download...")
            ydl.download([youtube_url])
        return f"Audio baixado com sucesso! Arquivo salvo em: {output_path}"
    except Exception as e:
        return f"Erro ao baixar audio: {e}"


# Testando o código
url = "https://www.youtube.com/watch?v=BM-mnklMWCQ"
resultado = download_audio(url)
print(resultado)