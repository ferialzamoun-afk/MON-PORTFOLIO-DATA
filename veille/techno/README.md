# 🔬 Veille Technologique — Ferial Zamoun
**Data Analyst — RNCP 37837 — 2024-2026**

> *Objectif : identifier les outils et méthodes les plus pertinents pour un profil Data Analyst en reconversion, en justifiant chaque choix par des critères concrets (adoption industrie, facilité de prise en main, intégration dans un pipeline data, valeur ajoutée CV).*

---

## 1. Langages & Environnements

| Outil | Usage dans mes projets | Pourquoi ce choix | Source de veille |
|-------|------------------------|-------------------|-----------------|
| **Python 3.11** | P6, P8, P9, P10, P11, P12, P13 | Standard de facto en Data Science. Écosystème Pandas/sklearn/Streamlit mature. | State of Data (Kaggle 2024), TIOBE Index |
| **SQL** | P3, P5, P8, P10 | Incontournable pour tout pipeline data. dbt repose entièrement sur SQL. | Sondages Stack Overflow 2023-2024 |
| **DAX** | P7, P10, P14 | Langage natif Power BI. Requis pour les calculs dans les modèles en étoile. | Documentation Microsoft, forums Power BI Community |

---

## 2. Manipulation & Analyse de Données

| Outil | Version utilisée | Usage | Critères de choix |
|-------|-----------------|-------|-------------------|
| **Pandas** | 2.x | Nettoyage, jointures, agrégations (P6, P9, P10, P11, P12) | Référence industrie, compatibilité sklearn/Streamlit |
| **NumPy** | 1.x | Calculs matriciels, statistiques (P11, P12) | Requis par sklearn et scipy |
| **SciPy** | 1.x | Tests statistiques (Shapiro-Wilk, Chi2, Mann-Whitney) — P9 | Bibliothèque de référence pour tests non-paramétriques |
| **Statsmodels** | — | Régressions, intervalles de confiance — P9, P12 | Complémentaire à sklearn pour l'inférence statistique |

**Sources** : documentation officielle, cours OC, Real Python, Towards Data Science.

---

## 3. Machine Learning

| Outil | Algorithmes utilisés | Projets | Justification |
|-------|---------------------|---------|---------------|
| **scikit-learn** | KMeans, PCA, LogisticRegression, RandomForest, KNN | P10, P11, P12 | Standard ML en Python. Pipeline sklearn reproductible. API unifiée fit/predict/transform. |
| **joblib / pickle** | Sérialisation modèles | P12 | Persistance du modèle pour déploiement FastAPI |

**Veille spécifique ML** :
- 📄 *Hands-On Machine Learning* (Aurélien Géron) — référence théorique
- 📄 Cours OC : Modèles de scoring, détection d'anomalies
- 🔗 Papers With Code — suivi des SOTA (état de l'art)

---

## 4. Visualisation & Reporting

| Outil | Projets | Forces identifiées | Limites connues |
|-------|---------|-------------------|-----------------|
| **Power BI Desktop** | P7, P10, P14 | Modèle en étoile natif, DAX puissant, partage via Power BI Service | Licence Pro requise pour partage, moins flexible que Tableau pour le custom |
| **Langage M (Power Query)** | P10 | Transformations ETL natives dans Power BI. Plus puissant que l'interface graphique pour logiques complexes. | Moins lisible que SQL pour les requêtes simples |
| **Streamlit** | P9, P8 (partiel) | Déploiement en production rapide (Streamlit Cloud), Python natif | Pas de drill-down natif, moins adapté aux très grands volumes |
| **Matplotlib / Seaborn** | P9, P10, P11, P12 | Visualisations exploratoires en notebook | Non interactif, sortie statique |
| **Plotly** | P9 (dashboard) | Graphiques interactifs dans Streamlit | Plus lourd à configurer que Seaborn |

**Critère de choix Power BI vs Streamlit** :
- Power BI → décideurs métier, reporting récurrent, données volumineuses sur SQL/Snowflake
- Streamlit → prototypage rapide, partage public gratuit, logique Python complexe

---

## 5. Data Engineering & Pipelines

| Outil | Version | Projets | Justification |
|-------|---------|---------|---------------|
| **dbt (data build tool)** | 1.11.3 | P8 | Standard de transformation SQL dans le cloud. Documente, teste et versionne les modèles. Adopté par 70%+ des entreprises avec Snowflake. |
| **Snowflake** | Cloud/SaaS | P8 | Cloud data warehouse leader (Gartner MQ 2024). Free trial pour prototypage. Compatibilité dbt native. |
| **GitHub Actions** | — | P8, P12 | CI/CD intégré à GitHub. Aucun outil tiers requis. 2000 min/mois gratuites. |
| **FastAPI** | 0.x | P12 | Framework API Python le plus adopté en 2024 (sondage JetBrains). Performance, validation Pydantic, docs Swagger auto. |

**Sources** :
- 📄 dbt documentation officielle (getdbt.com)
- 📰 Snowflake Summit 2024 — keynotes
- 📄 *Fundamentals of Data Engineering* (Reis & Housley, 2022)

---

## 6. Gouvernance des Données & Qualité

| Méthode / Outil | Projet | Description |
|----------------|--------|-------------|
| **Great Expectations** | P8 (veille) | Framework Python pour data quality. Création de "suites" de tests (expect_*) sur les données. Profiling automatique, documentation des contrats de données. Standard en production chez 1000+ entreprises (2024). Pattern implémenté manuellement dans P6/P13 (18 contrôles qualité). |
| **Data Contracts** | P13 | Contrats d'interface entre producteurs/consommateurs de données |
| **dbt tests** | P8 | Tests d'unicité, non-nullité, intégrité référentielle sur les modèles SQL |
| **Traçabilité IA (journalisation prompts)** | P13 | 26 prompts documentés avec contexte, décision, résultat — réponse aux exigences IA Act |

**Sources** :
- 📄 *Data Management Body of Knowledge* (DAMA-DMBOK)
- 📰 IA Act (EU, 2024) — exigences traçabilité systèmes IA
- 📄 Cours OC P13 — Gouvernance IA
- 🔗 [Great Expectations Documentation](https://docs.greatexpectations.io/) — Framework data quality

---

## 7. Contrôle de version & Collaboration

| Outil | Usage | Justification |
|-------|-------|---------------|
| **Git / GitHub** | Tous les projets | Standard universel. Historique, branches, reverts, CI/CD intégré. |
| **Conventional Commits** | P8, P12, P13 | Messages structurés (Fix:, Chore:, Docs:, Build:) pour traçabilité et changelogs automatiques. |
| **GitHub Pages + Jekyll** | MON-PORTFOLIO-DATA | Hébergement portfolio gratuit. Thème Cayman. |

---

## 8. Bases de données

| Outil | Projets | Usage |
|-------|---------|-------|
| **MySQL / MariaDB** | P3, P5 | Requêtes SQL analytiques, modélisation relationnelle |
| **PostgreSQL (concepts)** | P5 | Extension spatiale, types avancés |
| **Snowflake** | P8 | Cloud DWH — OLAP, colonnes compressées, warehouses on-demand |
| **MongoDB (veille)** | — | Veille sur le NoSQL — cf. `2026 W02 mongo.pdf` |

---

## 9. Environnements & DevOps

| Outil | Usage |
|-------|-------|
| **VS Code** | IDE principal (extensions Python, Jupyter, Git) |
| **Jupyter Lab / Notebook** | Explorations, EDA, livrables notebooks |
| **venv / pip** | Gestion des environnements Python |
| **Docker (veille)** | Conteneurisation — suivi des pratiques MLOps |

---

## 10. Ressources de Veille Utilisées

| Source | Type | Fréquence |
|--------|------|-----------|
| [Towards Data Science](https://towardsdatascience.com) | Blog technique | Hebdomadaire |
| [Stack Overflow Developer Survey](https://survey.stackoverflow.co/) | Sondage annuel | Annuel |
| [Kaggle State of Data Science](https://www.kaggle.com/kaggle-survey-2023) | Rapport | Annuel |
| [dbt Blog](https://www.getdbt.com/blog) | Blog spécialisé | Mensuel |
| [Snowflake Summit](https://www.snowflake.com/summit/) | Conférence | Annuel |
| [Papers With Code](https://paperswithcode.com) | Recherche ML | Ponctuel |
| [Real Python](https://realpython.com) | Tutoriels | Selon besoin |
| OpenClassrooms (cours + forum) | Formation | Continu |

---

*Dernière mise à jour : Juillet 2026*
