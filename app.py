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

#Saisie du taux de TVA 
taux_tva = st.slider("Choisir le taux de TVA (%)", min_value=0, max_value=100, value=15)

#Calcul de la TVA
if st.button("Générer la TVA"):
    data['TVA'] = data['Prix unitaire en euros'] * data['Quantité vendue'] * (taux_tva/100)
    st.write(data)

#Convertissage du DataFrame en CSV
csv = data.to_csv(index=False)

#Création du bouton pour télécharger le CSV
st.download_button(label="Télécharger le fichier CSV avec TVA", data=csv, file_name="produits_avec_tva.csv", mime="text/csv")