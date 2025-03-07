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

