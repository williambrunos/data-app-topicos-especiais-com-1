import streamlit as st
import pandas as pd


def plot_acidentes_por_br(dados):
    st.write("### Top 10 BRs com mais acidentes")

    tipos_acidentes = list(dados.dropna()['classificacao_acidente'].unique())
    tipos_acidentes.append('Todos')

    filtro = st.sidebar.selectbox("Selecione o tipo de acidente:",
                                  tipos_acidentes)

    if filtro == 'Todos':
        dados_filtrados = dados.copy()
    else:
        dados_filtrados = dados[dados['classificacao_acidente'] == filtro].copy()

    # Contar o número de acidentes por BR e ordenar em ordem decrescente
    top_brs = dados_filtrados['br'].value_counts().head(10).reset_index()
    top_brs.columns = ['BR', 'Quantidade de Acidentes']

    # Exibir o gráfico no Streamlit
    st.bar_chart(top_brs.set_index('BR'))
