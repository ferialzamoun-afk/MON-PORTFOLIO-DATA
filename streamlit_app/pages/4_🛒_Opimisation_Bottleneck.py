import streamlit as st
from pathlib import Path


st.title("🛒 Optimisation de gestion de données ERP ")

st.write("""
Cette page présente plusieurs analyses exploratoires en Python d'une base de rapprochements de données de plusieurs systèmes isolés
""")

# Chemin stable vers le README vitrine de US6
readme_path = (
    Path(__file__).resolve().parents[2]
    / "projets"
    / "US6_Optimisation_Bottleneck"
    / "README.md"
)

# Lire et afficher le README.md
if readme_path.exists():
    with readme_path.open("r", encoding="utf-8") as f:
        st.markdown(f.read(), unsafe_allow_html=True)
else:
    st.warning("README.md non trouve pour ce projet.")