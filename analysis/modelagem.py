import pandas as pd
import streamlit as st
import altair as alt

def plot_modelagem(dados):
    dados_acuracia = pd.read_csv('./data/models_accuracy.csv')
    dados_feature_importance = pd.read_csv('./data/feature_importance.csv')

    st.write("## Predição da classificação do acidente")

    dados_acuracia_classificacao_acidente = dados_acuracia[dados_acuracia['prediction_feature'] == 'classificacao_acidente']
    st.bar_chart(dados_acuracia_classificacao_acidente, x='model', y='accuracy', horizontal=False, x_label="Acurácia", y_label="Modelo")

    dados_classificacao_acidente = dados_feature_importance[dados_feature_importance['prediction_feature'] == 'classificacao_acidente']
    st.bar_chart(dados_classificacao_acidente, x='feature', y='feature_importance', horizontal=True, x_label="Importância da feature", y_label="Nome da feature")

    st.write("## Predição da quantidade de feridos")

    dados_acuracia_feridos_graves = dados_acuracia[dados_acuracia['prediction_feature'] == 'feridos_graves']
    st.bar_chart(dados_acuracia_feridos_graves, x='model', y='accuracy', horizontal=False, x_label="Acurácia", y_label="Modelo")

    dados_feridos_graves = dados_feature_importance[dados_feature_importance['prediction_feature'] == 'feridos_graves']
    st.bar_chart(dados_feridos_graves, x='feature', y='feature_importance', horizontal=True, x_label="Importância da feature", y_label="Nome da feature")

    st.write("## Predição do tipo de pista")

    dados_acuracia_tipo_pista = dados_acuracia[dados_acuracia['prediction_feature'] == 'tipo_pista']
    st.bar_chart(dados_acuracia_tipo_pista, x='model', y='accuracy', horizontal=False, x_label="Acurácia", y_label="Modelo")

    dados_tipo_pista = dados_feature_importance[dados_feature_importance['prediction_feature'] == 'tipo_pista']
    st.bar_chart(dados_tipo_pista, x='feature', y='feature_importance', horizontal=True, x_label="Importância da feature", y_label="Nome da feature")
