import streamlit as st


def plot_acidentes_por_uf(dados):
    st.write("### Quantidade de acidentes por UF")

    tipos_acidentes = list(dados.dropna()['classificacao_acidente'].unique())
    tipos_acidentes.append("Todos")
    filtro = st.sidebar.selectbox("Selecione o tipo de acidente:",
                                  tipos_acidentes)

    if filtro == 'Todos':
        dados_filtrados = dados.copy()
    else:
        dados_filtrados = dados[dados['classificacao_acidente'] == filtro].copy()

    df_grouped = dados_filtrados.groupby('uf').size().reset_index(name='Quantidade')
    df_grouped = df_grouped.sort_values(by='Quantidade', ascending=False)

    # st.bar_chart(df_grouped, x="uf", y="Quantidade", horizontal=True)
    st.bar_chart(df_grouped.set_index('uf').sort_values('Quantidade'))
