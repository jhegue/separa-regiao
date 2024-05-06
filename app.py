import streamlit as st
import pandas as pd
import zipfile
import os

st.title("Diretoria de Ensino")
uploaded_file = st.file_uploader("Escolha um arquivo Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    temp_pasta = "temp_excel_files"
    os.makedirs(temp_pasta, exist_ok=True)

    for de in df['de'].unique():
        df[df['de'] == de].to_excel(os.path.join(temp_pasta, f'{de}.xlsx'), index=False)

    caminho_zip = "diretorias.zip"
    
    with zipfile.ZipFile(caminho_zip, 'w') as zipf:
        for root, _, files in os.walk(temp_pasta):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.realpath(os.path.join(root, file), temp_pasta))

    st.success(f"Arquivo ZIP criado com sucesso! [Baixe aqui] ({caminho_zip})")

    [os.remove(os.path.join(temp_pasta, file)) for file in os.listdir(temp_pasta)]

    os.rmdir(temp_pasta)