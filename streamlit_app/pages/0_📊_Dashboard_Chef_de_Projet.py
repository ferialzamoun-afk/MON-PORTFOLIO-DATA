import streamlit as st
import pandas as pd
from pathlib import Path
from collections import Counter
import re

st.set_page_config(page_title="Dashboard Chef de Projet Data", layout="wide")
st.title("📊 Dashboard Chef de Projet Data")

# --- Chargement des données ---
cv_path = Path("../cv_chef_de_projet_data.md")
projets_path = Path("../projets_data.md")

# Extraction des compétences clés du CV
def extract_competences_cles(cv_path):
    with open(cv_path, encoding='utf-8') as f:
        lines = f.readlines()
    competences_cles = []
    inside_comp = False
    for line in lines:
        if line.strip().lower().startswith('## compétences clés'):
            inside_comp = True
            continue
        if inside_comp:
            if line.strip().startswith('##') and not line.strip().lower().startswith('## compétences clés'):
                break
            if line.strip().startswith('- '):
                competences_cles.append(line.strip()[2:])
    return competences_cles

# Extraction des projets et compétences associées
def extract_projets(projets_path):
    with open(projets_path, encoding='utf-8') as f:
        projets_lines = f.readlines()
    projets = []
    current_proj = None
    current_desc = ""
    for i, line in enumerate(projets_lines):
        if line.strip().startswith('### '):
            if current_proj:
                projets.append(current_proj)
            current_proj = {'nom': line.strip()[4:], 'desc': '', 'competences': [], 'duree': None}
            current_desc = ""
        elif '**Compétences :**' in line:
            comp_line = line.split('**Compétences :**')[-1].strip()
            comp_list = [c.strip() for c in re.split(',|;', comp_line)]
            current_proj['competences'] = comp_list
        elif '**Durée :**' in line:
            duree = re.findall(r"[\d\.,]+", line)
            current_proj['duree'] = float(duree[0].replace(',', '.')) if duree else None
        elif line.strip() and not line.strip().startswith('**') and not line.strip().startswith('---'):
            current_desc += line.strip() + " "
            current_proj['desc'] = current_desc.strip()
    if current_proj:
        projets.append(current_proj)
    return projets

competences_cles = extract_competences_cles(cv_path)
projets = extract_projets(projets_path)

# --- KPIs ---
nb_projets = len(projets)
durees = [p['duree'] for p in projets if p['duree']]
duree_moy = sum(durees)/len(durees) if durees else 0

st.markdown("### Indicateurs clés")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Nombre de projets", nb_projets)
kpi2.metric("Durée moyenne (sem.)", f"{duree_moy:.2f}")
kpi3.metric("Compétences clés", len(competences_cles))

# --- Histogramme compétences clés vs projets ---
comp_counter = Counter()
for comp_cle in competences_cles:
    comp_cle_lower = comp_cle.lower()
    for proj in projets:
        if any(comp_cle_lower.split()[0] in c.lower() for c in proj['competences']):
            comp_counter[comp_cle] += 1

st.markdown("### Répartition des compétences clés sur les projets")
st.bar_chart(pd.DataFrame.from_dict(comp_counter, orient='index', columns=['Nombre de projets']))

# --- Liste des projets ---
st.markdown("### Détail des projets")
for proj in projets:
    with st.expander(proj['nom']):
        st.write(f"**Description :** {proj['desc']}")
        st.write(f"**Compétences mobilisées :** {', '.join(proj['competences'])}")
        st.write(f"**Durée estimée :** {proj['duree']} semaines" if proj['duree'] else "")
