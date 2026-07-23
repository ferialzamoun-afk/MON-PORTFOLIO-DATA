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

## **📊 Structure du Projet**
```text
P8--DBT/
├── .github/
├── data/
├── macros/
├── models/
├── output/
├── snapshots/
├── tests/
├── .gitignore
├── .user.yml
├── CSV_EXPORT_VALUE_CHAIN.md
├── analyse_csv_p8.ipynb
├── dbt_project.yml
├── package-lock.yml
├── packages.yml
├── profiles.yml
├── README.md
├── requirements.txt
└── Synthese_etudiants.md
```

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

```text
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
```

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
```

Résultat : Données propres, sans anomalies, prêtes pour les jointures.

#### **2️⃣ INTERMEDIATE : Jointures & Agrégations**
**Objectif** : Fusionner les données OC et INSEE pour une analyse unifiée.
**Exemple de code** (`int_etudiants_insee_joined.sql`) :

```sql
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
```

Résultat : Vue unifiée OC + INSEE, prête pour les calculs d’indicateurs.

#### **3️⃣ MARTS : Indicateurs & Export**
**Objectif** : Calculer les KPIs et générer les exports pour Power BI/Streamlit.
**Exemple de code** (`fct_export_unifie.sql`) :

```sql
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
```

Résultat : 633 lignes prêtes pour Power BI, Streamlit ou Excel.

## **🔄 Pipeline CI/CD**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

### **📌 Déclenchement Automatique**
- ✅ Push sur `main` ou `develop` (dossier `P8--DBT/**`).
- ✅ Pull Request vers `main`.
- ✅ Déclenchement manuel (`workflow_dispatch`).

### **📌 Workflow `dbt-ci.yml` (3 Jobs)**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
  <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Job</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Objectif</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Durée</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Dépendances</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Sorties</strong></th></tr></thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">lint-compile</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Vérification syntaxique via <code>dbt parse</code>.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">~30 sec</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Aucune</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅/❌</td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">build</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Exécution des modèles et des tests.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">~3-5 min</td><td style="padding: 10px 12px; border: 1px solid #ddd;">lint-compile</td><td style="padding: 10px 12px; border: 1px solid #ddd;">CSV, JSON, logs</td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">export-csv</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Génération du CSV final.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">~45 sec</td><td style="padding: 10px 12px; border: 1px solid #ddd;">build</td><td style="padding: 10px 12px; border: 1px solid #ddd;">fct_export_unifie.csv</td></tr>
  </tbody>
</table>

Durée totale : ~5-8 minutes (bout en bout).

### **📌 Artefacts Disponibles**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
  <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Artefact</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Format</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Lieu</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Usage</strong></th></tr></thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">fct_export_unifie.csv</td><td style="padding: 10px 12px; border: 1px solid #ddd;">CSV</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/actions">GitHub Artifacts</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Source principale pour Power BI et Streamlit.</td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">dbt artifacts</td><td style="padding: 10px 12px; border: 1px solid #ddd;">JSON</td><td style="padding: 10px 12px; border: 1px solid #ddd;">GitHub Artifacts</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Lineage, tests et logs.</td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Logs dbt</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Text</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/actions">GitHub Actions UI</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Debugging.</td></tr>
  </tbody>
</table>

### **📌 Télécharger le CSV d'Export**
Méthode 1 : via GitHub UI

- Aller dans `Actions` puis sélectionner le run (ex: `dbt CI/CD #123`).
- Cliquer sur `Artifacts` puis télécharger `marts-csv-<RUN_ID>.zip`.
- Extraire le fichier `fct_export_unifie.csv`.

Méthode 2 : via CLI (GitHub CLI)

```bash
gh run download <RUN_ID> --repo ferialzamoun-afk/P8--DBT
```

## **📊 Résultats et Livrables**
*(Blocs RNCP37837BC03, BC05)*

### **🔹 Indicateurs Clés (2022-2025)**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
  <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Indicateur</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Valeur Moyenne</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Tendance</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Interprétation</strong></th></tr></thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Taux de pénétration OC</td><td style="padding: 10px 12px; border: 1px solid #ddd;">2,3 %</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Stable</td><td style="padding: 10px 12px; border: 1px solid #ddd;">% étudiants OC / population totale.</td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Écart femmes (OC vs INSEE)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">31% versus 51%</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ À améliorer</td><td style="padding: 10px 12px; border: 1px solid #ddd;">% femmes étudiantes - % femmes INSEE.</td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Groupe d’âge le plus représenté</td><td style="padding: 10px 12px; border: 1px solid #ddd;">20-24 ans</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Logique</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Aligné sur la cible historique OC.</td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Groupe d’âge sous-représenté</td><td style="padding: 10px 12px; border: 1px solid #ddd;">40+ ans</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ Priorité</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Lacune à combler.</td></tr>
  </tbody>
</table>

Exemple de données exportées (`fct_export_unifie.csv`) :
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
  <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">year</th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">region</th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">age_group</th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">gender</th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">nb_etudiants</th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">population_insee</th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">penetration_pct</th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">pct_femmes_etu</th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;">pct_femmes_insee</th></tr></thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">2025</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Île-de-France</td><td style="padding: 10px 12px; border: 1px solid #ddd;">20-24</td><td style="padding: 10px 12px; border: 1px solid #ddd;">F</td><td style="padding: 10px 12px; border: 1px solid #ddd;">1200</td><td style="padding: 10px 12px; border: 1px solid #ddd;">2500000</td><td style="padding: 10px 12px; border: 1px solid #ddd;">0.048</td><td style="padding: 10px 12px; border: 1px solid #ddd;">52.3</td><td style="padding: 10px 12px; border: 1px solid #ddd;">51.1</td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">2025</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Île-de-France</td><td style="padding: 10px 12px; border: 1px solid #ddd;">20-24</td><td style="padding: 10px 12px; border: 1px solid #ddd;">M</td><td style="padding: 10px 12px; border: 1px solid #ddd;">1100</td><td style="padding: 10px 12px; border: 1px solid #ddd;">2500000</td><td style="padding: 10px 12px; border: 1px solid #ddd;">0.044</td><td style="padding: 10px 12px; border: 1px solid #ddd;">47.7</td><td style="padding: 10px 12px; border: 1px solid #ddd;">48.9</td></tr>
  </tbody>
</table>

### **🔹 Visualisations (Streamlit/Power BI)**
Dashboard en développement :

- Carte choroplèthe : taux de pénétration par région.
- Bar charts : comparaison % femmes (OC vs INSEE).
- Heatmap : région × groupe d’âge (écarts de représentation).
- Line charts : tendances annuelles (2022-2025).
- Lien Streamlit (à déployer) : [🔗 Dépôt GitHub](https://github.com/ferialzamoun-afk/P8--DBT)

---

## **🔧 Compétences RNCP 37837 Demonstrées**

### **📌 Mapping des Blocs RNCP**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
  <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Bloc RNCP</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Compétence</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuves</strong></th></tr></thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC01</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Structurer et gérer la base de données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Modèle en 3 couches : staging, intermediate et marts avec dbt + Snowflake.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/tree/main/models">models/</a></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC01</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer une base de données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Requêtes SQL pour les jointures et agrégations de remplissage.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/blob/main/models/marts/fct_export_unifie.sql">fct_export_unifie.sql</a></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier et collecter les données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Deux sources principales : OpenClassrooms et INSEE.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/tree/main/data/raw">data/raw/</a></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Extraire et agréger</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Harmonisation des régions, groupes d'âge et genres.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/blob/main/models/staging/stg_etudiants.sql">stg_etudiants.sql</a></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Explorer et pré-traiter</td><td style="padding: 10px 12px; border: 1px solid #ddd;">FULL OUTER JOIN pour fusionner les jeux OC et INSEE.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/blob/main/models/intermediate/int_etudiants_insee_joined.sql">int_etudiants_insee_joined.sql</a></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse univariée / multivariée</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Calcul des KPI : pénétration et écarts genre/âge.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/blob/main/models/marts/fct_export_unifie.sql">fct_export_unifie.sql</a></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Solution de visualisation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard Streamlit en développement : cartes, heatmaps et tendances.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT">Dépôt GitHub</a></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Créer un tableau de bord</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Intégration Power BI via import du CSV exporté.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/blob/main/.github/workflows/POWER_BI_SETUP.md">POWER_BI_SETUP.md</a></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Reporting des tendances</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Exports CSV pour Power BI et Excel.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/tree/main/data/processed">data/processed/</a></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Veille métier / technologique</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Benchmark dbt + Snowflake vs autres outils.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/blob/main/CSV_EXPORT_VALUE_CHAIN.md">CSV_EXPORT_VALUE_CHAIN.md</a></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Formaliser le cahier des charges</td><td style="padding: 10px 12px; border: 1px solid #ddd;">README, workflows et guides documentent le projet.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT">Dépôt GitHub</a></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Organiser un projet data</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pipeline CI/CD GitHub Actions et modularité dbt.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/blob/main/.github/workflows/dbt-ci.yml">dbt-ci.yml</a></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer la documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Modèles dbt, workflows et exports documentés.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT">Dépôt GitHub</a></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses multivariées</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Comparaison OC vs INSEE par genre, âge et région.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P8--DBT/blob/main/analyse_csv_p8.ipynb">analyse_csv_p8.ipynb</a></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Tests statistiques</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Validation de l'unicité et de la cohérence des données.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P8--DBT/blob/main/notebook/analyse_csv_p8.ipynb">tests/</a></td></tr>
  </tbody>
</table>

---
## **🛠 Configuration et Exécution**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

### **📌 Prérequis**
- Python 3.11+
- dbt-snowflake
- Un environnement Snowflake prive ou equivalent pour rejouer le pipeline complet
- GitHub CLI (optionnel, pour recuperer des artefacts)

### **📌 Setup Initial (Local)**
```bash
# 1. Cloner le dépôt
git clone https://github.com/ferialzamoun-afk/P8--DBT.git
cd P8--DBT

# 2. Créer un environnement virtuel
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Installer dbt
pip install dbt-snowflake==1.11.3
```

### **🔐 Configuration des accès**
- Les parametres d'acces cloud et les secrets CI/CD ne sont pas publies dans ce portfolio.
- La configuration locale doit etre injectee hors depot via un gestionnaire de secrets, des variables d'environnement ou un fichier `profiles.yml` non versionne.
- Les habilitations Snowflake, noms d'environnements et scripts d'administration restent volontairement hors de la documentation publique.

### **📌 Commandes Principales**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
  <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Commande</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Exemple</strong></th></tr></thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Vérifier la configuration locale</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Teste le profil dbt disponible sur la machine.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>dbt debug</code></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Exécuter les modèles</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Lance tous les modèles dbt.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>dbt run</code></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Tester les données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Exécute les tests dbt.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>dbt test --select fct_export_unifie</code></td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Prévisualiser les résultats</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Affiche les 10 premières lignes.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>dbt show --select fct_export_unifie --limit 10</code></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Générer la documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Crée la documentation dbt.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>dbt docs generate</code></td></tr>
  </tbody>
</table>

### **📌 Lancer le Dashboard Streamlit (Local)**
```bash
# Installer les dépendances
pip install -r requirements-streamlit.txt

# Lancer l'application
streamlit run streamlit_app.py
```

URL locale attendue : `http://localhost:8501`

### **🔐 Politique de publication**
- Aucun secret, mot de passe, identifiant de compte, role ou script d'administration n'est conserve dans ce depot public.
- Les parametres d'acces au warehouse et a la CI restent geres dans des espaces prives separes du portfolio.
- Le repository documente l'architecture, les commandes dbt et les livrables, sans exposer la configuration de securite.

### **🚦 États du Pipeline**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
  <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>État</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Signification</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Action</strong></th></tr></thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Passed</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Workflow réussi</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Export prêt à utiliser.</td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">🟡 In Progress</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Exécution en cours</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Attendre la fin.</td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">❌ Failed</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Erreur dbt ou Snowflake</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Voir les logs.</td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">⏭️ Skipped</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Condition non remplie</td><td style="padding: 10px 12px; border: 1px solid #ddd;">PR ou branche non ciblée.</td></tr>
  </tbody>
</table>

### **📈 Améliorations Futures**

- Dashboard Streamlit interactif (déploiement sur Streamlit Cloud).
- Intégration Power BI via webhook (Power Automate).
- Modèles prédictifs (machine learning pour anticiper les tendances).
- API REST pour un accès programmatique aux données.
- Alertes Slack/Teams sur anomalies (ex: écarts > 20%).
- Versioning des exports (historique des données).

### **📅 Releases**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
  <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Version</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Date</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Changements</strong></th></tr></thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">v1.0</td><td style="padding: 10px 12px; border: 1px solid #ddd;">24/03/2026</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Export initial <code>fct_export_unifie</code> : 633 lignes.</td></tr>
    <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">v0.9</td><td style="padding: 10px 12px; border: 1px solid #ddd;">-</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Configuration CI/CD GitHub Actions.</td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">v0.5</td><td style="padding: 10px 12px; border: 1px solid #ddd;">-</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Setup dbt + Snowflake.</td></tr>
  </tbody>
</table>

### **📌 Mapping RNCP 37837**

Blocs couverts par ce projet :

- ✅ BC01 : Structurer et gérer la base de données (modèle dbt en 3 couches, Snowflake)
- ✅ BC02 : Identifier, collecter et analyser les données (nettoyage, jointures, KPIs)
- ✅ BC03 : Visualiser des données et interpréter des résultats (Dashboard Streamlit/Power BI, exports CSV)
- ✅ BC04 : Piloter un projet data (CI/CD, documentation, organisation, veille)
- ✅ BC05 : Spécialisation Statistiques (analyses comparatives, tests statistiques, indicateurs)

