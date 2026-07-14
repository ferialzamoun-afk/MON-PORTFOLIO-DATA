# 📊 **P8 : Analyse Comparée Étudiants OpenClassrooms vs INSEE**
**Analyse de la représentativité des étudiants par région, genre et groupe d’âge pour améliorer les stratégies de recrutement et d’inclusion.**

> **🔹 Données à jour**   **🔄 Pipeline contrôlé** | **📥 Exports automatisés** | **📈 Reporting en temps réel**

**📅 Date** : 03/2026 *(Dernière mise à jour : 24/03/2026 - v1.0)*
**🏷️ Type** : Data Pipeline / dbt / Snowflake / CI/CD / Streamlit
**🔗 Liens** :
- [🔗 Dépôt GitHub](https://github.com/ferialzamoun-afk/P8--DBT)
- [📄 Documentation Pipeline](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/CSV_EXPORT_VALUE_CHAIN.md)
- [📄 Guide Power BI](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/.github/workflows/POWER_BI_SETUP.md)
- [📄 Setup Manuel CI/CD](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/.github/workflows/MANUAL_WORKFLOW_SETUP.md)
- [📊 Artefacts GitHub Actions](https://github.com/ferialzamoun-afk/P8--DBT/actions) *(CSVs exportés)*
- [📓 Notebook Exploratoire](https://nbviewer.org/github/ferialzamoun-afk/P8--DBT/blob/main/analyse_csv_p8.ipynb) *(Analyses complémentaires)*

---

## **🎯 Contexte et Objectifs**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

> **Contexte** :
> *"Projet réalisé pour **OpenClassrooms** dans le cadre d’une **analyse data-driven** visant à évaluer la **représentativité de ses étudiants** par rapport à la population française (données INSEE). L’objectif est d’**identifier les lacunes de couverture** (région, genre, âge) pour **ajuster les stratégies de recrutement** et **améliorer l’inclusion**."*

> **Objectifs Analytiques** :
> 1. **Calculer le taux de pénétration** OpenClassrooms par région.
> 2. **Analyser les écarts de représentation** par genre (vs INSEE).
> 3. **Identifier les groupes d’âge sous-représentés** (20-24 ans, 25-29 ans, etc.).
> 4. **Produire des indicateurs de tendance annuels** (2022-2025).
> 5. **Délivrer des exports CSV** pour Power BI et reporting.

> **KPIs Clés** :
> | **Indicateur** | **Description** | **Source** |
> |---------------|----------------|------------|
> | `% femmes étudiants` | Pourcentage de femmes parmi les étudiants OC | Données OC |
> | `% femmes INSEE` | Pourcentage de femmes dans la population française | Données INSEE |
> | **Ratio étudiants/population** | Nombre d’étudiants OC / population totale par région | OC + INSEE |
> | **Écart par groupe d’âge** | Différence de représentation entre OC et INSEE | OC + INSEE |

---

## **🏗️ Architecture et Méthodologie**
*(Blocs RNCP37837BC01, BC02, BC04)*

### **📌 Stack Technique**
 | **Composant** | **Outil** | **Version** | **Rôle** |
 |---------------|-----------|-------------|----------|
 | **Data Pipeline** | dbt | 1.11.7 | Transformation des données (SQL) |
 | **Data Warehouse** | Snowflake | Cloud/SaaS | Stockage et requêtage |
 | **Orchestration** | GitHub Actions | CI/CD | Automatisation du pipeline |
 | **Visualisation** | Power BI / Streamlit | En développement | Dashboard interactif |
 | **Stockage exports** | GitHub Artifacts | 90 jours | Fichiers CSV générés |

---
### **📌 Modèle de Données (3 Couches)**
*(Bloc RNCP37837BC01 : Structurer et gérer la base de données)*
┌─────────────────────────────────────────┐
│          📊 MARTS (Tables d'export)         │
│  ├─ fct_export_unifie.csv                │ ← 633 lignes (2022-2025)
│  ├─ fct_profil_sociodem.csv               │ ← Profils sociodémographiques
│  └─ fct_summary_analysis.csv              │ ← Synthèse des indicateurs
└─────────────────┬───────────────────────┘
│
┌─────────────────────────────────────────┐
│      🔧 INTERMEDIATE (Transformations)     │
│  └─ int_etudiants_insee_joined.sql        │ ← Jointure complète OC + INSEE
└─────────────────┬───────────────────────┘
│
┌─────────────────────────────────────────┐
│        🧹 STAGING (Nettoyage)             │
│  ├─ stg_etudiants.sql                     │ ← Données OC nettoyées
│  └─ stg_insee_population.sql              │ ← Données INSEE agrégées
└─────────────────┬───────────────────────┘
│
┌─────────────────────────────────────────┐
│         📥 SOURCES (Données brutes)        │
│  ├─ raw_etudiants.csv                      │ ← Données OC 2022-2025
│  ├─ raw_insee_population.csv               │ ← Données INSEE 2022-2025
│  └─ raw_geo_ref.csv                        │ ← Référentiel géographique
└─────────────────────────────────────────┘
---
### **📌 Processus dbt (3 Étapes)**
*(Bloc RNCP37837BC02 : Identifier, collecter et analyser les données)*

#### **1️⃣ STAGING : Nettoyage & Harmonisation**
**Objectif** : Préparer les données brutes pour les rendre **cohérentes et exploitables**.
**Exemple de code** (`stg_etudiants.sql`) :
```sql
SELECT
  ANNÉE,
  REGION,               -- Harmonisation accents/DOM-TOM
  AGE_GROUP,            -- Normalisation "30 à 34 ans" → "30-34"
  GENDER,               -- Mapping H/F → M/F
  COUNT(*) as nb_etudiants
FROM raw_etudiants
WHERE annee >= 2022    -- Filtrage période
GROUP BY 1,2,3,4

Résultat : Données propres, sans anomalies, prêtes pour les jointures.

2️⃣ INTERMEDIATE : Jointures & Agrégations
Objectif : Fusionner les données OC et INSEE pour une analyse unifiée.
Exemple de code (int_etudiants_insee_joined.sql) :
WITH etudiants AS (
  SELECT ... FROM stg_etudiants
),
insee_agg AS (
  SELECT ... FROM stg_insee_population
)
SELECT
  e.year, e.region, e.age_group, e.gender,
  e.nb_etudiants,
  i.population_insee,
  CASE
    WHEN e.year IS NOT NULL THEN 'matched'
    WHEN i.year IS NOT NULL THEN 'insee_only'
    ELSE 'students_only'
  END as match_status
FROM etudiants e
FULL OUTER JOIN insee_agg i
  ON e.year = i.year
  AND e.region = i.region
  AND e.gender = i.gender
  AND e.age_group = i.age_group

  Résultat : Vue unifiée OC + INSEE, prête pour les calculs d’indicateurs.

3️⃣ MARTS : Indicateurs & Export
Objectif : Calculer les KPIs et générer les exports pour Power BI/Streamlit.
Exemple de code (fct_export_unifie.sql) :
SELECT
  year, region, age_group, gender,
  nb_etudiants,
  population_insee,
  ROUND(100.0 * nb_etudiants / NULLIF(population_insee, 0), 2) as penetration_pct,
  ROUND(100.0 * COUNT(CASE WHEN gender='F' THEN 1 END) / NULLIF(COUNT(*), 0), 2) as pct_femmes_etu,
  ROUND(100.0 * COUNT(CASE WHEN gender='F' THEN 1 END) / NULLIF(SUM(population_insee), 0), 2) as pct_femmes_insee
FROM int_etudiants_insee_joined
WHERE year BETWEEN 2022 AND 2025
GROUP BY 1,2,3,4
ORDER BY year DESC, region, age_group, gender

Résultat : 633 lignes prêtes pour Power BI, Streamlit ou Excel.

🔄 Pipeline CI/CD
(Bloc RNCP37837BC04 : Piloter un projet data)
📌 Déclenchement Automatique
✅ Push sur main ou develop (dossier P8--DBT/**).
✅ Pull Request vers main.
✅ Déclenchement manuel (workflow_dispatch).

📌 Workflow dbt-ci.yml (3 Jobs)
| Job | Objectif | Durée | Dépendances | Sorties |
| --- | --- | --- | --- | --- |
| lint-compile | Vérification syntaxique (dbt parse) | ~30 sec | Aucune | ✅/❌ |
| build | Exécution + tests des modèles | ~3-5 min | lint-compile | CSV, JSON, logs |
| export-csv | Génération du CSV final | ~45 sec | build | fct_export_unifie.csv |
Durée totale : ~5-8 minutes (bout en bout).

📌 Artefacts Disponibles
| Artefact | Format | Lieu | Usage |
| --- | --- | --- | --- |
| fct_export_unifie.csv | CSV | [GitHub Artifacts](https://github.com/ferialzamoun-afk/P8--DBT/actions) | Source principale pour Power BI/Streamlit |
| dbt artifacts | JSON | GitHub Artifacts | Lineage, tests, logs |
| Logs dbt | Text | [GitHub Actions UI](https://github.com/ferialzamoun-afk/P8--DBT/actions) | Debugging |
📌 Télécharger le CSV d’Export
Méthode 1 : Via GitHub UI

Aller dans Actions → Sélectionner le run (ex: dbt CI/CD #123).
Cliquer sur Artifacts → Télécharger marts-csv-<RUN_ID>.zip.
Extraire le fichier fct_export_unifie.csv.
Méthode 2 : Via CLI (GitHub CLI)
gh run download <RUN_ID> --repo ferialzamoun-afk/P8--DBT

📊 Résultats et Livrables
(Blocs RNCP37837BC03, BC05)
🔹 Indicateurs Clés (2022-2025)
| Indicateur | Valeur Moyenne | Tendance | Interprétation |
| --- | --- | --- | --- |
| Taux de pénétration OC | [À calculer] % | ✅ Stable | % étudiants OC / population totale |
| Écart femmes (OC vs INSEE) | [À calculer] % | ⚠️ À améliorer | % femmes étudiants - % femmes INSEE |
| Groupe d’âge le plus représenté | [20-24 ans] | ✅ Logique | Aligné sur la cible historique OC |
| Groupe d’âge sous-représenté | [40+ ans] | ⚠️ Priorité | Lacune à combler |

Exemple de données exportées (fct_export_unifie.csv) :
| year | region | age_group | gender | nb_etudiants | population_insee | penetration_pct | pct_femmes_etu | pct_femmes_insee |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025 | Île-de-France | 20-24 | F | 1200 | 2500000 | 0.048 | 52.3 | 51.1 |
| 2025 | Île-de-France | 20-24 | M | 1100 | 2500000 | 0.044 | 47.7 | 48.9 |
🔹 Visualisations (Streamlit/Power BI)
Dashboard en développement :

Carte choroplèthe : Taux de pénétration par région.
Bar charts : Comparaison % femmes (OC vs INSEE).
Heatmap : Région × Groupe d’âge (écarts de représentation).
Line charts : Tendances annuelles (2022-2025).
Lien Streamlit (à déployer) : [🌐 Dashboard Streamlit (Futur)](https://your-streamlit-app.com)

P8--DBT/
├── .github/
│   ├── workflows/
│   │   ├── dbt-ci.yml                     # Workflow principal CI/CD
│   │   ├── MANUAL_WORKFLOW_SETUP.md       # Guide de lancement manuel
│   │   ├── POWER_BI_SETUP.md              # Intégration Power BI
│   │   └── helpers/
│   │
├── dbt_project.yml                        # Configuration dbt
├── profiles.yml                           # Connexion Snowflake
├── models/
│   ├── staging/                           # Nettoyage brut
│   │   ├── stg_etudiants.sql
│   │   └── stg_insee_population.sql
│   ├── intermediate/                      # Transformations
│   │   └── int_etudiants_insee_joined.sql
│   └── marts/                             # Tables d'export
│       └── fct_export_unifie.sql
├── tests/                                 # Tests dbt
│   └── test_unique_stg_etudiants_grain.sql
├── src/                                   # Scripts/utilitaires
│   ├── enrich_insee_population.py
│   ├── extract_insee_population.py
│   └── build_pbi_unified_export.py
├── target/                                # Artifacts générés
├── data/                                  # Données (si configurées localement)
│   ├── raw/                               # Sources brutes
│   └── processed/                         # Données transformées
├── logs/                                  # Logs d'exécution
├── analyse_csv_p8.ipynb                   # Analyses exploratoires
├── README.md
├── CSV_EXPORT_VALUE_CHAIN.md              # Chaîne de valeur
└── .gitignore

---

🔧 Compétences RNCP 37837 Demonstrées
📌 Mapping des Blocs RNCP
Bloc RNCP,Compétence,Description,Preuves
BC01,Structurer et gérer la base de données,Modèle en 3 couches (STAGING → INTERMEDIATE → MARTS) avec dbt + Snowflake.,[models/](https://github.com/ferialzamoun-afk/P8--DBT/tree/main/models)
BC01,Gérer une base de données,Requêtes SQL pour le remplissage des tables (jointures, agrégations).,[fct_export_unifie.sql](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/models/marts/fct_export_unifie.sql)
BC02,Identifier et collecter les données,Utilisation de 2 sources principales (OpenClassrooms, INSEE).,[data/raw/](https://github.com/ferialzamoun-afk/P8--DBT/tree/main/data/raw)
BC02,Extraire et agréger,Nettoyage : Harmonisation des noms de régions, groupes d'âge, genres.,[stg_etudiants.sql](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/models/staging/stg_etudiants.sql)
BC02,Explorer et pré-traiter,Jointures complexes (FULL OUTER JOIN) pour fusionner OC + INSEE.,[int_etudiants_insee_joined.sql](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/models/intermediate/int_etudiants_insee_joined.sql)
BC02,Analyse univariée/multivariée,Calcul des KPIs (pénétration, écarts genre/âge).,[fct_export_unifie.sql](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/models/marts/fct_export_unifie.sql)
BC03,Solution de visualisation,Dashboard Streamlit (en développement) : Cartes, heatmaps, tendances.,[À déployer](https://your-streamlit-app.com)
BC03,Créer un tableau de bord,Intégration Power BI : Import du CSV pour visualisations.,[POWER_BI_SETUP.md](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/.github/workflows/POWER_BI_SETUP.md)
BC03,Reporting des tendances,Exports CSV pour Power BI/Excel.,[data/processed/](https://github.com/ferialzamoun-afk/P8--DBT/tree/main/data/processed)
BC04,Veille métier/technologique,Benchmark dbt + Snowflake vs autres outils (Airflow, etc.).,[CSV_EXPORT_VALUE_CHAIN.md](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/CSV_EXPORT_VALUE_CHAIN.md)
BC04,Formaliser le cahier des charges,Documentation complète (README, workflows, guides).,[Dépôt GitHub](https://github.com/ferialzamoun-afk/P8--DBT)
BC04,Organiser un projet data,Pipeline CI/CD (GitHub Actions) + modularité dbt.,[.github/workflows/dbt-ci.yml](https://github.com/ferialzamoun-afk/P8--DBT/blob/main/.github/workflows/dbt-ci.yml)
BC04,Gérer la documentation,100% des livrables documentés (modèles dbt, workflows, exports).,[Dépôt GitHub](https://github.com/ferialzamoun-afk/P8--DBT)
BC05,Analyses multivariées,Comparaison OC vs INSEE (genre, âge, région).,[analyse_csv_p8.ipynb](https://nbviewer.org/github/ferialzamoun-afk/P8--DBT/blob/main/analyse_csv_p8.ipynb)
BC05,Tests statistiques,Validation des données (unicité, cohérence).,[tests/](https://github.com/ferialzamoun-afk/P8--DBT/tree/main/tests)
🛠 Configuration et Exécution
(Bloc RNCP37837BC04 : Piloter un projet data)
📌 Prérequis

Python 3.11+
dbt-snowflake (pip install dbt-snowflake==1.11.3)
Snowflake Account (accès aux données)
GitHub CLI (optionnel, pour télécharger les artefacts)
📌 Setup Initial (Local)
# 1. Cloner le dépôt
git clone https://github.com/ferialzamoun-afk/P8--DBT.git
cd P8--DBT

# 2. Créer un environnement virtuel
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Installer dbt
pip install dbt-snowflake==1.11.3

# 4. Configurer les accès Snowflake
# → Modifier C:\Users\<USER>\.dbt\profiles.yml
# Exemple :
# P8_OPENCLASSROOMS:
#   target: dev_password
#   outputs:
#     dev_password:
#       type: snowflake
#       account: <SNOWFLAKE_ACCOUNT>
#       user: <SNOWFLAKE_USER>
#       password: <SNOWFLAKE_PASSWORD>
#       role: <SNOWFLAKE_ROLE>
#       warehouse: <SNOWFLAKE_WAREHOUSE>
#       database: <SNOWFLAKE_DATABASE>
#       schema: <SNOWFLAKE_SCHEMA>

# 5. Vérifier la connexion Snowflake
dbt debug --target dev_password
📌 Commandes Principales
| Commande | Description | Exemple |
| --- | --- | --- |
| Vérifier la connexion | Teste la connexion à Snowflake | dbt debug --target dev_password |
| Exécuter les modèles | Lance tous les modèles dbt | dbt run --target dev_password |
| Tester les données | Exécute les tests dbt | dbt test --select fct_export_unifie |
| Prévisualiser les résultats | Affiche les 10 premières lignes | dbt show --select fct_export_unifie --limit 10 |
| Générer la documentation | Crée la doc dbt | dbt docs generate && dbt docs serve |

📌 Lancer le Dashboard Streamlit (Local)
# Installer les dépendances
pip install -r requirements-streamlit.txt

# Lancer l'application
streamlit run streamlit_app.py
→ URL locale : http://localhost:8501

🔐 Configuration des Accès
(Bloc RNCP37837BC04 : Piloter un projet data)
📌 Secrets GitHub Requis
(À configurer dans Settings → Secrets and variables → Actions)
| Secret | Description | Exemple |
| --- | --- | --- |
| SNOWFLAKE_ACCOUNT | Compte Snowflake | xy12345 |
| SNOWFLAKE_USER | Utilisateur Snowflake | CI_USER |
| SNOWFLAKE_PASSWORD | Mot de passe | *** |
| SNOWFLAKE_ROLE | Rôle Snowflake | CI_ROLE |
| SNOWFLAKE_WAREHOUSE | Warehouse Snowflake | COMPUTE_WH |
| SNOWFLAKE_DATABASE | Base de données | P8_OPENCLASSROOMS |
| SNOWFLAKE_SCHEMA | Schéma | RAW_DATA |
📌 Permissions Snowflake
(À exécuter par un admin Snowflake)
sql
-- Accorder les permissions au rôle CI
GRANT USAGE ON DATABASE P8_OPENCLASSROOMS TO ROLE CI_ROLE;
GRANT USAGE ON SCHEMA RAW_DATA TO ROLE CI_ROLE;
GRANT CREATE TABLE ON SCHEMA RAW_DATA TO ROLE CI_ROLE;
GRANT INSERT, SELECT ON ALL TABLES IN SCHEMA RAW_DATA TO ROLE CI_ROLE;

🚦 États du Pipeline
| État | Signification | Action |
| --- | --- | --- |
| ✅ Passed | Workflow réussi | ✓ Export prêt à utiliser |
| 🟡 In Progress | Exécution en cours | ⏳ Attendre la fin |
| ❌ Failed | Erreur dbt/Snowflake | 🔧 Voir les logs |
| ⏭️ Skipped | Condition non remplie | (PR ou branche non ciblée) |

📈 Améliorations Futures

 Dashboard Streamlit interactif (déploiement sur Streamlit Cloud).
 Intégration Power BI via webhook (Power Automate).
 Modèles prédictifs (machine learning pour anticiper les tendances).
 API REST pour un accès programmatique aux données.
 Alertes Slack/Teams sur anomalies (ex: écarts > 20%).
 Versioning des exports (historique des données).

📅 Releases
| Version | Date | Changements |
| --- | --- | --- |
| v1.0 | 24/03/2026 | Export initial fct_export_unifie (633 lignes) |
| v0.9 | - | Configuration CI/CD GitHub Actions |
| v0.5 | - | Setup dbt + Snowflake |

📌 Mapping RNCP 37837

Blocs couverts par ce projet :

✅ BC01 : Structurer et gérer la base de données (modèle dbt en 3 couches, Snowflake)
✅ BC02 : Identifier, collecter et analyser les données (nettoyage, jointures, KPIs)
✅ BC03 : Visualiser des données et interpréter des résultats (Dashboard Streamlit/Power BI, exports CSV)
✅ BC04 : Piloter un projet data (CI/CD, documentation, organisation, veille)
✅ BC05 : Spécialisation Statistiques (analyses comparatives, tests statistiques, indicateurs)

