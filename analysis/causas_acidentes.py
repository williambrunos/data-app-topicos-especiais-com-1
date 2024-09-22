import pandas as pd
import streamlit as st
import altair as alt


def plot_causas_acidentes(dados):
    st.write("### Top 10 principais causas de acidentes")

    tipos_acidentes = list(dados.dropna()['classificacao_acidente'].unique())
    tipos_acidentes.append('Todos')

    filtro = st.sidebar.selectbox("Selecione o tipo de acidente:", tipos_acidentes)

    if filtro == 'Todos':
        dados_filtrados = dados.copy()
    else:
        dados_filtrados = dados[dados['classificacao_acidente'] == filtro].copy()

    df_grouped = dados_filtrados['causa_acidente'].value_counts().head(10).reset_index()
    df_grouped.columns = ['Causa_acidente', 'Quantidade de Acidentes']

    # Usando Altair para plotar e evitar truncamento dos rótulos
    chart = alt.Chart(df_grouped).mark_bar().encode(
        x=alt.X('Quantidade de Acidentes:Q', title='Quantidade de Acidentes'),
        y=alt.Y('Causa_acidente:N', title='Causa do Acidente', sort='-x')
    ).properties(
        width=500,
        height=400
    ).configure_axis(
        labelFontSize=12,
        labelLimit=200
    )

    st.altair_chart(chart, use_container_width=True)