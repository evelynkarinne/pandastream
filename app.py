import streamlit as st
import pandas as pd

st.title("Sistema de Análise de Alunos")

arquivo = st.file_uploader(
    "Selecione um arquivo CSV",
    type=["csv"]
)

if arquivo is not None:

    df = pd.read_csv(arquivo)

    st.subheader("Dados")

    st.dataframe(df)

    st.subheader("Informações")

    st.write("Linhas e Colunas:", df.shape)

    st.write("Colunas:", list(df.columns))

    st.subheader("Estatísticas")

    st.dataframe(df.describe())

    if "nota" in df.columns:

        media = df["nota"].mean()

        st.metric(
            "Média das Notas",
            round(media, 2)
        )
