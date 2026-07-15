# 🎯 Proof Point : P8 — Égalité Femmes-Hommes

## 1️⃣ Contexte
Le projet vise à comparer la représentation des étudiants OpenClassrooms à celle de l’INSEE pour identifier des écarts de recrutement et d’inclusion.

## 2️⃣ Données
- **Sources** : OpenClassrooms + INSEE + référentiel géographique.
- **Qualité** : pipeline dbt et harmonisation des données pour production d’exports.
- **Limites** : plusieurs indicateurs restent marqués comme à calculer dans le README.

## 3️⃣ Démarche
- Pipeline dbt sur Snowflake.
- Architecture staging / intermediate / marts.
- GitHub Actions pour CI/CD et exports CSV pour Power BI / Streamlit.

## 4️⃣ Résultats + Impact
- Export unifié de 633 lignes.
- Trois couches de transformation documentées.
- Lecture métier : groupe 20-24 ans le plus représenté, 40+ comme groupe sous-représenté.

## 5️⃣ Limites & Pistes
- Dashboard Streamlit / Power BI à finaliser.
- Compléter les KPIs encore non calculés.
- Consolider le suivi dans un reporting plus automatisé.

**Référence** : [README projet](README.md)
