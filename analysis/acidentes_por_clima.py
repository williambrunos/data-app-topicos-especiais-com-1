import streamlit as st


def plot_acidentes_por_clima(dados):
    st.write("### Quantidade de acidentes por condição metereológica")

    tipos_acidentes = list(dados.dropna()['classificacao_acidente'].unique())
    tipos_acidentes.append("Todos")
    filtro = st.sidebar.selectbox("Selecione o tipo de acidente:",
                                  tipos_acidentes)

    if filtro == 'Todos':
        dados_filtrados = dados.copy()
    else:
        dados_filtrados = dados[dados['classificacao_acidente'] == filtro].copy()

    df_grouped = dados_filtrados.groupby('condicao_metereologica').size().reset_index(name='Quantidade de acidentes')

    st.bar_chart(df_grouped,
                 x='condicao_metereologica',
                 y='Quantidade de acidentes',
                 x_label="Condição metereológica",
                 y_label="Quantidade de acidentes",
                 horizontal=True)
