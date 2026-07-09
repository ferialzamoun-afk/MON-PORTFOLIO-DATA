# P9 - Analyse des ventes Lapage

Projet d'analyse de donnees et de visualisation pour la librairie Lapage.

Objectif metier:
- suivre la performance commerciale (CA, panier, concentration),
- comprendre les comportements clients (segments, categories, frequence),
- fournir des livrables exploitables par le CODIR (notebooks, dashboard, exports KPI).

## Contenu du projet

- Analyses statistiques en notebooks (axes Marketing et BI ).
- Fonctions reutilisables pour la preparation des donnees et la visualisation.
- Dashboard Streamlit multi-pages.
- Exports de KPI (Excel) et figures de reporting.
- Pipeline CI avec tests pytest.

## Etat actuel

- Notebook et exports KPI: operationnels.
- Streamlit: operationnel en local.
- CI pytest: operationnelle.
- UX dashboard: version prototype, simplification orientee business en cours.

## Structure principale

- `data/` : jeux de donnees bruts et transformes.
- `notebooks/` : analyses et scripts de tests statistiques.
- `src/` : modules utilitaires (KPI, exports, gestion data).
- `reutilisable (toutes phases)/` : fonctions mutualisees (chargement, analyses, visualisations).
- `Streamlit/` : application web.
- `reports/` : livrables (figures, exports xlsx, presentations).
- `.github/workflows/ci.yml` : pipeline CI.

## Prerequis

- Python 3.11+
- pip

## Installation

Depuis `lapage_project`:

```bash
pip install -r requirements.txt
```

## Lancement local

### 1) Notebooks

```bash
cd notebooks
jupyter notebook
```

### 2) Dashboard Streamlit

Depuis `lapage_project`:

```bash
streamlit run Streamlit/app.py
```

## Tests

Depuis `lapage_project`:

```bash
python -m pytest tests/test_app.py -v --tb=short
```

La suite actuelle couvre:
- chargement des donnees,
- coherence des KPI de base,
- filtrage,
- coherence des metriques clients,
- filtrage multi-criteres du dashboard.

## Dashboard en ligne

- URL de production: https://sznbna247tbtpj2hkhexqe.streamlit.app/


## Fichiers generes et versioning

Le `.gitignore` racine exclut les artefacts generes:
- figures PNG sous `reports/figures/`,
- exports Excel sous `reports/`,
- livrables Word/PowerPoint sous `reports/Presentation/`,
- caches Python et checkpoints notebooks.

