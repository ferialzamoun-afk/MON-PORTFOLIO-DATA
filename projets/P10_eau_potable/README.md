# 🌊 **P10 : Dashboard Eau, Population et Gouvernance**
**Analyse décisionnelle pour les enjeux mondiaux d'accès à l'eau potable, de gouvernance politique et de mortalité liée à l'eau (WASH)**

**📅 Date** : 06/2026 *(Dernière mise à jour : 12/06/2026)*
**🏷️ Type** : Pipeline Data / Visualisation / Dashboard Power BI
**🔗 Liens** :
- [🔗 Dépôt GitHub](https://github.com/ferialzamoun-afk/P10)
- [📓 Notebook 01 : Inspection & Normalisation (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20données.ipynb)
- [📓 Notebook 02 : Préparation & Nettoyage (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/02%20-%20Pr%C3%A9paration%20et%20nettoyage%20des%20donn%C3%A9es.ipynb)
- [📓 Notebook 03 : Analyses & EDA (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/03%20-%20Analyses%20des%20groupements%20de%20pays%20-%20EDA%20Patrick%20-%20ACP-r%C3%A9ductions_dimensions-clustering%20.ipynb)
- [📊 Dashboard Power BI (Template)](https://github.com/ferialzamoun-afk/P10/raw/main/pbit/Dashboard_eau_v6.pbit)
- [📄 Blueprint complet](https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md)
- [📄 Glossaire métier](https://github.com/ferialzamoun-afk/P10/blob/main/docs/contexte_DWFA_glossaire_eau.md)

---

## **🎯 Contexte et Objectifs**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

> **Contexte** :
> *"Projet **DWFA (Data Work For Africa)** visant à créer un **dashboard Power BI interactif** pour analyser les **enjeux mondiaux d’accès à l’eau potable**, de **gouvernance politique** et de **mortalité liée à l’eau (WASH)**. Ce projet s’inscrit dans une démarche d’**aide à la décision** pour les acteurs publics et privés engagés dans l’amélioration de l’accès à l’eau.*

> **Objectifs Métier** :
> Le dashboard répond à **quatre besoins utilisateurs prioritaires** :
>   **Besoin** | **Indicateurs Clés** | **Visualisation** |
> |-----------|---------------------|------------------|
> | Comprendre la stabilité politique mondiale | Stabilité politique par pays/continent | Carte choroplèthe + bar chart |
> | Localiser les zones critiques WASH | Mortalité WASH, accès à l’eau potable | Carte du monde + ranking top N |
> | Identifier les priorités d’action publique | Scores métier (création, modernisation, gouvernance) | Matrice de priorisation |
> | Explorer les trajectoires nationales | Population rurale, accès eau, services "safely managed" | KPI + courbes temporelles + tableaux |

> **Niveaux de lecture** :
> 1. **Mondiale** : Disparités géographiques et comparaisons continentales.
> 2. **Métier** : Trois domaines d’action (création, modernisation, gouvernance).
> 3. **Nationale** : Analyse détaillée par pays avec trajectoires temporelles.

---

## **📊 Structure du Projet**
```text
P10/
├── api/
├── data/
├── docs/
├── notebooks/
├── output/
├── scripts/
├── source/
├── src/
├── tests/
├── veille/
├── Dockerfile
├── Procfile
├── PROJECT_BRIEF.md
├── README.md
├── pytest.ini
└── requirements.txt
```

---
## **🔧 Compétences RNCP 37837 Démontrées**

### **📌 Mapping des Blocs RNCP**
| **Bloc RNCP** | **Compétence** | **Description** | **Preuves** |
|---------------|---------------|----------------|-------------|
| **BC01** | **Structurer et gérer la base de données** | Création de **tables étoile Power BI** (`fact_dashboard_star_fr.csv`, `dim_pays_star_fr.csv`) et **marts analytiques** (csv_enrichis/). | [data/processed/pbi_star/](https://github.com/ferialzamoun-afk/P10/tree/main/data/processed/pbi_star) |
| **BC01** | **Gérer une base de données** | **Requêtes SQL implicites** via Pandas pour le remplissage des tables (ex: jointures pays-région). | [Notebook 02](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/02%20-%20Pr%C3%A9paration%20et%20nettoyage%20des%20donn%C3%A9es.ipynb) |
| **BC02** | **Identifier et collecter les données** | Utilisation de **5 sources de données** (Population, Régions, Stabilité politique, Mortalité WASH, Services eau). | [data/raw/](https://github.com/ferialzamoun-afk/P10/tree/main/data/raw) |
| **BC02** | **Extraire et agréger** | **Nettoyage** : Standardisation des noms de pays (`country_converter`), rattachement pays-région. | [Notebook 01](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20donn%C3%A9es.ipynb) |
| **BC02** | **Explorer et pré-traiter** | **Feature Engineering** : Calcul des scores `score_creation_services`, `score_modernisation_services`, `score_gouvernance`. | [Notebook 01](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20donn%C3%A9es.ipynb) |
| **BC02** | **Analyse univariée/multivariée** | **EDA** : Statistiques descriptives, corrélations entre indicateurs (ex: stabilité politique vs mortalité WASH). | [Notebook 03](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/03%20-%20Analyses%20des%20groupements%20de%20pays%20-%20EDA%20Patrick%20-%20ACP-r%C3%A9ductions_dimensions-clustering%20.ipynb) |
| **BC03** | **Solution de visualisation** | **Carte choroplèthe** (stabilité politique), **bar charts** (comparaisons continentales), **scatter plots** (création/modernisation). | [Dashboard Power BI](https://github.com/ferialzamoun-afk/P10/raw/main/pbit/Dashboard_eau_v6.pbit) |
| **BC03** | **Créer un tableau de bord** | **Dashboard Power BI complet** avec 3 pages (monde, domaines métier, nationale). | [Dashboard_eau_v6.pbit](https://github.com/ferialzamoun-afk/P10/raw/main/pbit/Dashboard_eau_v6.pbit) |
| **BC03** | **Reporting des tendances** | **KPI cards** (moyennes globales), **line plots** (trajectoires nationales), **matrice de priorisation**. | [Blueprint](https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md) |
| **BC04** | **Veille métier/technologique** | **Benchmark des outils** (Power BI vs Tableau) et **méthodologie documentée**. | [blueprint_P10_dashboard_eau.md](https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md) |
| **BC04** | **Formaliser le cahier des charges** | **Blueprint complet** avec besoins utilisateurs, indicateurs, et visuels. | [blueprint_P10_dashboard_eau.md](https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md) |
| **BC04** | **Organiser un projet data** | **Pipeline en 3 notebooks** + **modules réutilisables** (`src/`). | [Notebooks/](https://github.com/ferialzamoun-afk/P10/tree/main/notebooks) + [src/](https://github.com/ferialzamoun-afk/P10/tree/main/src) |
| **BC04** | **Gérer la documentation** | **100% des livrables documentés** (notebooks, scripts, glossaire, méthodologie). | [Dépôt GitHub](https://github.com/ferialzamoun-afk/P10) |
| **BC05** | **Analyses multivariées** | **Scoring composite** (création + modernisation + gouvernance) pour prioriser les pays. | [Notebook 03](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/03%20-%20Analyses%20des%20groupements%20de%20pays%20-%20EDA%20Patrick%20-%20ACP-r%C3%A9ductions_dimensions-clustering%20.ipynb) |
| **BC05** | **Réduction de dimension** | **Sélection des indicateurs** (5 sources → 3 domaines métier : création, modernisation, gouvernance). | [Notebook 01](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20donn%C3%A9es.ipynb) |

---
## **📊 Pipeline de Données**
*(Blocs RNCP37837BC01, BC02, BC04)*

### **🔹 Notebook 01 : Inspection, Normalisation et Construction Analytique**
**Objectif** : Qualifier les données sources, les harmoniser et construire les indicateurs de base.
**Étapes** :
1. **Chargement** des 5 fichiers source (Population, Régions, Stabilité politique, Mortalité WASH, Services eau).
2. **Cadrage** via **schéma canonique français** (`src/schema_fr.py`).
3. **Inspection de qualité** : Types, valeurs manquantes, granularités, cohérence pays.
4. **Préparation analytique** :
   - Standardisation des noms de pays (`country_converter`).
   - Rattachement pays-région.
5. **Construction des scores** :
   - `score_creation_services` = Accès à l’eau potable + urbanisation.
   - `score_modernisation_services` = Service basique vs "safely managed".
   - `score_gouvernance` = Stabilité politique + mortalité WASH + efficacité.
6. **Publication** : Marts analytiques (EN/FR) et **tables étoile Power BI**.

---

### **🔹 Notebook 02 : Formalisation en Couches et Gouvernance**
**Objectif** : Structurer le pipeline en **3 couches** reproductibles et auditer les contrats de publication.
**Couches** :
- **Staging** : Atterrissage contrôlé des données brutes.
- **Intermediate** : Transformations métier centralisées (harmonisation, enrichissement).
- **Marts** : Tables orientées consommation (Power BI, analyses).
**Sorties** :
- Dimensions : `country_region_reference`, `water_indicators_long`.
- Faits : `fact_dashboard_star_fr.csv`.

---
### **🔹 Notebook 03 : Analyses Métier et EDA**
**Objectif** : Exploiter les marts pour produire des analyses métier et des visualisations pour la soutenance.
**Domaines analysés** :
1. **Création de services** :
   - Scatter plot : **population urbaine vs accès à l’eau**.
2. **Modernisation de services** :
   - Évolution : **basique → safely managed**.
3. **Gouvernance** :
   - Stabilité politique vs **proxy d’efficacité** (score gouvernance).

---
## **📈 Résultats et Livrables**
*(Blocs RNCP37837BC03, BC05)*

### **🔹 Dashboard Power BI**
**Architecture** :
| **Page** | **Visuels** | **Filtres** |
|----------|------------|-------------|
| **Page 1 : Vue mondiale et continentale** | Carte choroplèthe (stabilité politique/mortalité WASH), bar chart par continent, KPI cards (moyennes globales), Top N pays | Année, région, action prioritaire |
| **Page 2 : Domaines métier** | Scatter plot (création), grouped bar chart (modernisation), scatter plot avec quadrants (gouvernance), carte de support | Année, région, seuil population |
| **Page 3 : Vue nationale** | KPI cards du pays, line plot (évolution démographique), line plot (trajectoire accès eau), tableau détaillé | Pays, année |

**Artefacts clés** :
| **Fichier** | **Description** | **Usage** |
|-------------|----------------|-----------|
| `Dashboard_eau_v6.pbit` | **Modèle Power BI complet** (template) | Visualisation directe |
| `fact_dashboard_star_fr.csv` | Table de faits (pays × année × indicateurs) | Power BI - visualisations |
| `dim_pays_star_fr.csv` | Dimension pays enrichie (région, indicateurs statiques) | Power BI - contexte |
| `csv_enrichis/fr/` | Marts analytiques français | Analyses complémentaires |

---
### **🔹 Indicateurs Clés**
| **Domaine** | **Indicateur** | **Source** | **Utilisation** |
|-------------|---------------|------------|----------------|
| **Stabilité politique** | `political_stability` | Banque Mondiale | Carte choroplèthe (Page 1) |
| **Mortalité WASH** | `mortality_rate_water` | OMS | Ranking top N (Page 1) |
| **Accès eau potable** | `basic_drinking_water` | OMS/UNICEF | Scatter plot (Page 2) |
| **Services "safely managed"** | `safely_managed_water` | OMS/UNICEF | Grouped bar chart (Page 2) |
| **Population rurale** | `rural_population` | Banque Mondiale | Line plot (Page 3) |

---
## **📂 Preuves et Documentation**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

| **Type** | **Lien** | **Description** |
|----------|----------|-----------------|
| **Dépôt GitHub** | [P10](https://github.com/ferialzamoun-afk/P10) | Code source, notebooks, scripts, données |
| **Notebook 01** | [Inspection & Normalisation (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20données.ipynb) | Qualification, nettoyage, scores |
| **Notebook 02** | [Préparation & Nettoyage (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/02%20-%20Pr%C3%A9paration%20et%20nettoyage%20des%20donn%C3%A9es.ipynb) | Pipeline en couches, tables étoile |
| **Notebook 03** | [Analyses & EDA (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/03%20-%20Analyses%20des%20groupements%20de%20pays%20-%20EDA%20Patrick%20-%20ACP-r%C3%A9ductions_dimensions-clustering%20.ipynb) | Analyses métier, visualisations |
| **Dashboard Power BI** | [Dashboard_eau_v6.pbit](https://github.com/ferialzamoun-afk/P10/raw/main/pbit/Dashboard_eau_v6.pbit) | Modèle complet (à ouvrir avec Power BI Desktop) |
| **Blueprint** | [blueprint_P10_dashboard_eau.md](https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md) | Détail des besoins et visuels |
| **Glossaire** | [contexte_DWFA_glossaire_eau.md](https://github.com/ferialzamoun-afk/P10/blob/main/docs/contexte_DWFA_glossaire_eau.md) | Définitions des indicateurs |
| **Méthodologie** | [resume_methodologique_pipeline...md](https://github.com/ferialzamoun-afk/P10/blob/main/docs/resume_methodologique_pipeline_notebooks_01_02_03.md) | Détails du pipeline |
| **QCM Soutenance** | [questions_pieges_soutenance_P10.md](https://github.com/ferialzamoun-afk/P10/blob/main/docs/questions_pieges_soutenance_P10.md) | Points critiques pour l'évaluation |

---
## **🛠 Configuration et Exécution**
*(Bloc RNCP37837BC04 : Organiser un projet data)*

### **📌 Prérequis**
- Python **3.12+**
- `pip` ou `conda`
- Jupyter Lab/Notebook
- Power BI Desktop *(pour ouvrir le `.pbit`)*

---
### **📌 Installation**
```bash
# 1. Cloner le dépôt
git clone https://github.com/ferialzamoun-afk/P10.git
cd P10

# 2. Créer et activer l'environnement virtuel (optionnel mais recommandé)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\Activate.ps1   # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

📌 Utilisation Programmatique
(Bloc RNCP37837BC04 : Gérer la documentation et formaliser les processus)
python
Copier

from src.data_manager import load_raw_data, publish_marts
from src.schema_fr import apply_schema_fr
from src.kpi_export import compute_scores

# Charger et transformer
data = load_raw_data()
data_fr = apply_schema_fr(data)
scores = compute_scores(data_fr)

# Publier les marts
publish_marts(scores, lang=['fr', 'en'])




⚠️ Qualité des Données et Audits
(Bloc RNCP37837BC02 : Identifier, collecter et analyser les données)
🔹 Points de Vigilance


  
    
      Problème
      Solution Appliquée
      Impact
    
  
  
    
      Mortalité WASH : Données disponibles surtout jusqu’à 2016
      Traitement des valeurs récentes avec prudence
      Éviter les analyses temporelles sur 2017+
    
    
      Hétérogénéité des noms de pays
      Standardisation via country_converter
      5 territoires exclus (Hong Kong, Macao, Taiwan, etc.)
    
    
      Granularité population
      Données annuelles validées (habitants)
      Cohérence des agrégations
    
    
      Couverture géographique
      193 pays attendus
      Lacunes ciblées par data_curation
    
  



🔹 Audits Effectués

✅ Validation des correspondances pays × région (12/06/2026).
✅ Suppression de 5 territoires créant des anomalies de classification.
✅ Vérification des totaux continentaux vs sommes nationales.
✅ Audit de concordance EN ↔ FR.

🔄 Maintenance et Mises à Jour
📌 Recalcul Complet

Placer les fichiers source dans data/raw/.
Exécuter les 3 notebooks dans l’ordre.
Les sorties seront publiées dans data/processed/.
📌 Enrichissements Possibles

Ajout de nouveaux indicateurs (climat, budget, etc.).
Extension régionale (sous-régions, bassins fluviaux).
Intégration de données en temps réel.
Versioning des modèles de score.

📌 Mapping RNCP 37837

Blocs couverts par ce projet :

✅ BC01 : Structurer et gérer la base de données (tables étoile Power BI, marts analytiques)
✅ BC02 : Identifier, collecter et analyser les données (pipeline, nettoyage, EDA, scores)
✅ BC03 : Visualiser des données et interpréter des résultats (Dashboard Power BI, graphiques)
✅ BC04 : Piloter un projet data (documentation, CI, organisation, veille)
❌ BC05 : Spécialisation Statistiques (Partiellement couvert via les scores composites, mais pas de modèles ML avancés)

