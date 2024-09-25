import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt

def plot_modelagem(dados):
    dados_acuracia = pd.read_csv('./data/models_accuracy.csv')
    dados_feature_importance = pd.read_csv('./data/feature_importance.csv')

    st.write("## Predição da classificação do acidente")

    dados_acuracia_classificacao_acidente = dados_acuracia[dados_acuracia['prediction_feature'] == 'classificacao_acidente']
    st.bar_chart(dados_acuracia_classificacao_acidente, x='model', y='accuracy', horizontal=False, x_label="Acurácia", y_label="Modelo")

    dados_classificacao_acidente = dados_feature_importance[dados_feature_importance['prediction_feature'] == 'classificacao_acidente']
    plot_feature_importance(dados_classificacao_acidente, 'Classificação do Acidente')

    st.write("## Predição da quantidade de feridos")

    dados_acuracia_feridos_graves = dados_acuracia[dados_acuracia['prediction_feature'] == 'feridos_graves']
    st.bar_chart(dados_acuracia_feridos_graves, x='model', y='accuracy', horizontal=False, x_label="Acurácia", y_label="Modelo")

    dados_feridos_graves = dados_feature_importance[dados_feature_importance['prediction_feature'] == 'feridos_graves']
    plot_feature_importance(dados_feridos_graves, 'Feridos Graves')

    st.write("## Predição do tipo de pista")

    dados_acuracia_tipo_pista = dados_acuracia[dados_acuracia['prediction_feature'] == 'tipo_pista']
    st.bar_chart(dados_acuracia_tipo_pista, x='model', y='accuracy', horizontal=False, x_label="Acurácia", y_label="Modelo")

    dados_tipo_pista = dados_feature_importance[dados_feature_importance['prediction_feature'] == 'tipo_pista']
    plot_feature_importance(dados_tipo_pista, 'Tipo de Pista')

def plot_feature_importance(dados, target_name):
    fig = plt.figure(figsize=(10, 6))
    plt.barh(dados['feature'], dados['feature_importance'], color='skyblue')
    plt.xlabel('Importância')
    plt.title(f'Importância das Características ({target_name})')
    # plt.show()
    st.pyplot(fig)
