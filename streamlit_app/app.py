import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Portfolio Data Analyst",
    page_icon="📊",
    layout="wide"
)

# --- HEADER ---
st.title("📊 Portfolio Data Analyst")
st.write("Bienvenue dans mon application Streamlit qui présente mes projets data en format portfolio.")

st.markdown("---")

# --- INTRO ---
st.header("🎯 Objectif de l'application")
st.write("""
Cette application présente mes projets réalisés dans le cadre de ma formation et de mon développement professionnel.
Vous pouvez naviguer entre les analyses via le menu de gauche et accéder aux dépôts complets via les liens ci-dessous.
""")

col_link_1, col_link_2 = st.columns(2)
with col_link_1:
    st.link_button(
        "🔗 Voir le dépôt P6",
        "https://github.com/ferialzamoun-afk/OC-P6_Optimisation_des_donnees_dune_boutique_en_Python"
    )
with col_link_2:
    st.link_button(
        "🔗 Voir le dépôt SOC Monitoring",
        "https://github.com/ferialzamoun-afk/soc-data-anomaly-monitoring"
    )

# --- APERCU DES PROJETS ---
st.header("📁 Aperçu des projets")

cols = st.columns(4)

with cols[0]:
    st.subheader("🛒 Analyse e-commerce")
    st.write("Exploration des ventes, tendances, segmentation clients.")
with cols[1]:
    st.subheader("🗄️ Requêtes SQL")
    st.write("Extraction et analyse de données via SQL.")
with cols[2]:
    st.subheader("🩺 Étude santé publique")
    st.write("Analyse statistique et visualisations.")
with cols[3]:
    st.subheader("🛡️ Audit & Détection d'anomalies")
    st.markdown("✨ Accès rapide au dashboard")
    st.link_button(
        "Ouvrir le dashboard",
        "https://soc-data-anomaly-monitoring-of3oufewjpbvav6ekbs6wr.streamlit.app/"
    )
    st.caption("Dashboard Streamlit public")

st.markdown("---")

st.info("Utilisez le menu latéral pour accéder aux projets.")
