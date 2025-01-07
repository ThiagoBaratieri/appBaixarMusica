import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'downloader')))

from downloader.yt_downloader import download_audio


# Titulo da pagina
st.title("Só baixa música boa")

# Instruções
st.write("Insira um link do youtube e escolha o formato do áudio para download")

# Insira o link
youtube_url = st.text_input("Link do YouTube:")

# Escolha o formato do audio
format_audio = st.selectbox("Escolha o formato do áudio:", ['mp3', 'wav', 'acc'])

# Botão de download
if st.button("Baixar Áudio"):
    if youtube_url:  # Verifica se o URL foi fornecido
        resultado = download_audio(youtube_url, format_audio=format_audio)
        st.success(resultado)  # Exibe o resultado na interface
    else:
        st.error("Por favor, insira um link do YouTube válido.")