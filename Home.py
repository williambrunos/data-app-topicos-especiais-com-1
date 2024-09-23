import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from analysis.acidentes_por_uf import plot_acidentes_por_uf
from analysis.acidentes_por_br import plot_acidentes_por_br
from analysis.acidentes_por_clima import plot_acidentes_por_clima
from analysis.causas_acidentes import plot_causas_acidentes


def print_students():
    text = "Aluno - Matrícula:\n"

    students_names = [
        "Gabriel Vasconcelos Santos - 497688",
        "Izaias Machado Pessoa Neto - 497372",
        "Márcio Bruno Loiola Gomes - 473740",
        "Vinicius Costa dos Santos - 473003",
        "Vitor Hugo Muniz de Sousa Santos - 475767",
        "Wendel Manfrini de Andrade Mendes - 494899",
        "William Bruno Sales de Paula Lima - 497345"
    ]

    for i, student in enumerate(students_names):
        text += f"{i + 1}. {student}\n"

    st.write(text)


@st.dialog("Sobre o app")
def about_the_app():
    st.write("Este é um data app para análise de dados de acidentes de trânsito no Brasil.")
    
    st.write("O dataset utilizado foi o de [Acidentes 2024 (Agrupados por ocorrência)](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf) disponibilizado pela Polícia Rodoviária Federal no portal de dados abertos do governo.")

    st.write("### Equipe 02 - Trabalho 02 - Ciência de Dados | UFC 2024.1")

    print_students()

st.write("# Data App - Ciência de Dados | UFC 2024.1")

st.write("Este é um data app para análise de dados de acidentes de trânsito no Brasil. Para mais informações, clique no botão \"Sobre o app\" no menu lateral.")

st.write("## Dados DataTran 2024")

dados = pd.read_csv('./data/datatran2024_limpo.csv', sep=';')
st.write(dados)

factory_analise = {
    'Acidentes por unidade federativa': plot_acidentes_por_uf,
    'Acidentes por BR': plot_acidentes_por_br,
    'Acidentes por condição climática': plot_acidentes_por_clima,
    'Principais causas de acidentes': plot_causas_acidentes
}

st.sidebar.write("## Menu de opções sobre os dados")
option = st.sidebar.selectbox(
    'Escolha qual análise deseja visualizar',
    factory_analise.keys()
)

if option:
    factory_analise[option](dados)

if "about_the_app" not in st.session_state:
    if st.sidebar.button("Sobre o app"):
        about_the_app()
