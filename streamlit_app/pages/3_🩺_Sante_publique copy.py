import streamlit as st
import os

import matplotlib.pyplot as plt

st.title("🛒 Requêtes SQL ")

st.write("""
Cette page présente une analyse de base immobilière dans SQL.
""")

# Déduire le chemin du dossier projet à partir du nom de la page
page_filename = os.path.basename(__file__)
projet_name = page_filename.split('_')[1]  # À adapter selon ta convention de nommage
projet_dir = f'../../projets/US{projet_name}_<nom_projet>/'  # À adapter selon ta structure
readme_path = os.path.join(projet_dir, 'README.md')

# Lire et afficher le README.md
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        st.markdown(f.read(), unsafe_allow_html=True)
else:
    st.warning("README.md non trouvé pour ce projet.")