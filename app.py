#Importation des Packages
import streamlit as st
import pandas as pd
import altair as alt

#Création de DataFrame
data = pd.read_csv('ventes.csv', sep=';')
data.head()

#Structure de l'application
st.title("Analyse des Ventes")
st.subheader("Un aperçu rapide des données")
st.write(data.head())

#Visualisation graphique
x_axis = st.selectbox("Choisissez la colonne pour l'axe X", data.columns)
y_axis = st.selectbox("Choisissez la colonne pour l'axe Y", data.columns)
title = st.text_input("Titre du graphique", "Titre...")
chart = alt.Chart(data).mark_bar().encode(x=alt.X(x_axis, title=x_axis),y=alt.Y(y_axis, title=y_axis)).properties(title=title)
st.altair_chart(chart, use_container_width=True)

#Widget filtre de Produit
produits = data['Produit'].unique()
choix_produit = st.selectbox("Choisissez un produit :", produits)
df_filtre = data[data['Produit'] == choix_produit]
st.write(df_filtre)