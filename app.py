import streamlit as st
import pandas as pd

st.title("Sistema de Análise de Alunos")

'''arquivo = st.file_uploader(
    "Selecione um arquivo CSV",
    type=["csv"]
)'''

arquivo = "alunos.csv"

if arquivo is not None:

    df = pd.read_csv(arquivo,index_col="id")

    print(df)

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
    idade_minima = st.number_input(
    "Idade mínima",
    min_value=0,
    value=18
    )

    filtrado = df[df["idade"] >= idade_minima]
    st.dataframe(filtrado)
