import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from analysis.acidentes_por_uf import plot_acidentes_por_uf
from analysis.acidentes_por_br import plot_acidentes_por_br
from analysis.acidentes_por_clima import plot_acidentes_por_clima
from analysis.causas_acidentes import plot_causas_acidentes

st.sidebar.markdown("Bem vindo ao data app do Data Tran 2024")
st.write("# Data App - Tópicos especiais em computação 1 \n"
         "## Dados DataTran 2024")

dados = pd.read_csv('./data/datatran2024_limpo.csv', sep=';')

factory_analise = {
    'Acidentes por unidade federativa': plot_acidentes_por_uf,
    'Acidentes por BR': plot_acidentes_por_br,
    'Acidentes por condição climática': plot_acidentes_por_clima,
    'Principais causas de acidentes': plot_causas_acidentes
}

st.sidebar.markdown("## Escolha no checkbox abaixo qual a análise desejada :smile:")
option = st.sidebar.selectbox(
    'Escolha qual análise deseja',
    factory_analise.keys()
)

if option:
    factory_analise[option](dados)

st.write("### Obrigado!!")
