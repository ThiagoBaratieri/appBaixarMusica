import re


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
    padrao = r"^(https:\/\/(www\.)?youtube\.com\/watch\?v=[A-Za-z0-9_-]+|https:\/\/youtu\.be\/[A-Za-z0-9_-]+)$"
    if not re.match(padrao, youtube_url):
        return "URL Inválida ou Inexistente. Forneça um link válido do youtube"

    
    # 2. Obter o vídeo com o pytube
    
    # 3. Selecionar apenas o áudio
    
    # 4. Salvar no diretório especificado

    return "Link válido, pronto para o download"

print(download_audio("https://www.youtube.com/watch?v=BzFxuDIEcUI"))