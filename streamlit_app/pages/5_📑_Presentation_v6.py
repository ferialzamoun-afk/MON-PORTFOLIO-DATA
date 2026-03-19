import streamlit as st
import os
import glob
import subprocess



st.title("📑 Présentation du projet")
st.write("Sélectionnez un sous-projet et un document à afficher.")

# --- Dossier racine des sous-projets ---
projects_root = os.path.join("..", "projets")


# --- Filtrer les projets qui ont au moins un PDF dans un dossier assets (même en sous-dossier) ---
projects_raw = []
assets_paths = {}
for d in os.listdir(projects_root):
    project_path = os.path.join(projects_root, d)
    if os.path.isdir(project_path):
        # Cherche tous les dossiers "assets" dans le projet (récursif)
        found_assets = glob.glob(os.path.join(project_path, '**', 'assets'), recursive=True)
        for assets_path in found_assets:
            pdfs = [f for f in os.listdir(assets_path) if f.lower().endswith('.pdf')]
            if pdfs:
                projects_raw.append(d)
                assets_paths[d] = assets_path
                break  # On ne prend que le premier dossier assets trouvé avec PDF

# Transformation en noms lisibles
def format_project_name(folder_name):
    parts = folder_name.split("_")
    us_code = parts[0].upper()
    title = " ".join(parts[1:]).capitalize()
    return f"{us_code} – {title}"

# Liste affichée dans le menu déroulant
projects_display = ["— Choisir un projet —"] + [format_project_name(d) for d in projects_raw]

# Menu déroulant lisible
selected_display = st.selectbox("Choisissez un sous-projet :", projects_display)

# Si l'utilisateur n'a rien choisi → on arrête là
if selected_display == "— Choisir un projet —":
    st.info("Veuillez sélectionner un sous-projet.")
    st.stop()

# Retrouver le vrai nom du dossier correspondant
selected_project = projects_raw[projects_display.index(selected_display) - 1]
selected_project

# Dossier assets du sous-projet sélectionné (trouvé dynamiquement)
assets_dir = assets_paths[selected_project]

# Lister les PDF du sous-projet
pdf_files = [f for f in os.listdir(assets_dir) if f.lower().endswith(".pdf")]

# Menu déroulant pour choisir un PDF
selected_pdf = st.selectbox("Choisissez un document :", pdf_files)

# Chemin complet du PDF
pdf_path = os.path.join(assets_dir, selected_pdf)

# Lecture du PDF
with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()

# Bouton de téléchargement
st.download_button(
    label=f"📄 Télécharger : {selected_pdf}",
    data=pdf_bytes,
    file_name=selected_pdf,
    mime="application/pdf"
)


# Affichage du PDF
st.subheader("Aperçu du document")
import base64
pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="900" type="application/pdf"></iframe>'
st.components.v1.html(pdf_display, height=900)

st.write("Taille du PDF :", len(pdf_bytes), "octets")

