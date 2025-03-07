#Importation des Packages
import streamlit as st
import pandas as pd
import altair as alt

#Création de DataFrame
data = pd.read_csv('ventes.csv', sep=';')
data.head()