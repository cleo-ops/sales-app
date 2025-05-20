# Importation des bibliothèques nécessaires
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns

# Titre de l'application
st.title("Visualisation des ventes 📊")

# Demander le nom de l'utilisateur
nom = st.text_input("Quel est votre prénom ?")

# Afficher un message de bienvenue
if nom:
    st.write(f"Bonjour {nom}, bienvenue dans l'application !")

# Chargement des données
st.subheader("Chargement des données")
fichier = st.file_uploader("Téléversez un fichier CSV", type="csv")

if fichier is not None:
    df = pd.read_csv(fichier)
    st.success("Fichier chargé avec succès !")
else:
    df = pd.read_csv("Warehouse_and_Retail_Sales.csv")
    st.info("Chargement du fichier local par défaut.")

# Aperçu des données
st.write("Aperçu des données :")
st.dataframe(df.head())

# Création d'une colonne de date
df["DATE"] = pd.to_datetime(df["YEAR"].astype(str) + "-" + df["MONTH"].astype(str) + "-01")

# Graphique des ventes mensuelles
st.subheader("Évolution des ventes au détail")

ventes_mensuelles = df.groupby("DATE")["RETAIL SALES"].sum().reset_index()

fig, ax = plt.subplots()
ax.plot(ventes_mensuelles["DATE"], ventes_mensuelles["RETAIL SALES"])
ax.set_xlabel("Date")
ax.set_ylabel("Ventes")
ax.set_title("Ventes mensuelles")
plt.xticks(rotation=45)
st.pyplot(fig)

# Heatmap des corrélations
st.subheader("Corrélation entre les variables numériques")

colonnes_numeriques = df.select_dtypes(include=["float64", "int64"])
matrice_corr = colonnes_numeriques.corr()

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(matrice_corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
ax.set_title("Matrice de corrélation")
st.pyplot(fig)

# Lien vers l'application déployée :
# https://ton-lien-streamlit.app
