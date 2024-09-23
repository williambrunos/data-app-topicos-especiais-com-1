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

    st.write("### Média de mortos por grupo de quilômetros das BRs")
    # Dividindo 'km' em 10 intervalos
    # Cast de km para int
    dados['km'] = dados['km'].apply(lambda x: x.replace(",", ".")).astype(float)
    dados = dados[dados['km'] >= 0]
    dados_grouped = dados.groupby('km')['mortos'].mean().reset_index()

    dados_grouped['km_bins'] = pd.cut(dados_grouped['km'], bins=10)
    # Calculando a média de 'mortos' para cada intervalo de 'km'
    media_mortos_por_bin = dados_grouped.groupby('km_bins')['mortos'].mean().reset_index()
    media_mortos_por_bin['km_bins_str'] = media_mortos_por_bin['km_bins'].apply(
        lambda x: f"{max(x.left, 0):.1f} - {x.right:.1f}")

    # Exibindo gráfico de barras
    st.bar_chart(media_mortos_por_bin, x='km_bins_str', y='mortos', horizontal=True,
                 x_label="Média de mortos",
                 y_label="Grupo da quilometragem")