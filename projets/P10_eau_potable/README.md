# 🌊 **P10 : Dashboard Eau, Population et Gouvernance**
**Analyse décisionnelle pour les enjeux mondiaux d'accès à l'eau potable, de gouvernance politique et de mortalité liée à l'eau (WASH)**

**📅 Date** : 06/2026 *(Dernière mise à jour : 12/06/2026)*
**🏷️ Type** : Pipeline Data / Visualisation / Dashboard Power BI
**🔗 Liens** :
- [🔗 Dépôt GitHub](https://github.com/ferialzamoun-afk/P10)
- [📓 Notebook 01 : Inspection & Normalisation (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20données.ipynb)
- [📓 Notebook 02 : Préparation & Nettoyage (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/02%20-%20Pr%C3%A9paration%20et%20nettoyage%20des%20donn%C3%A9es.ipynb)
- [📓 Notebook 03 : Analyses & EDA (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/03%20-%20Analyses%20des%20groupements%20de%20pays%20-%20EDA%20Patrick%20-%20ACP-r%C3%A9ductions_dimensions-clustering%20.ipynb)
- [📊 Télécharger le template Power BI (.pbit)](https://https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P10_eau_potable/assets/Zamoun_F%C3%A9rial_2_dashboard_112025.pbit)
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
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Bloc RNCP</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Compétence</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuves</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC01</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Structurer et gérer la base de données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Tables étoile Power BI et marts analytiques dédiés.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/tree/main/data/processed/pbi_star">data/processed/pbi_star/</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC01</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer une base de données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Jointures et alimentation des tables via Pandas.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/02%20-%20Pr%C3%A9paration%20et%20nettoyage%20des%20donn%C3%A9es.ipynb">Notebook 02</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier et collecter les données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Utilisation de 5 sources : population, régions, stabilité politique, mortalité WASH et services eau.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/tree/main/data/raw">data/raw/</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Extraire et agréger</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Nettoyage, standardisation des noms de pays et rattachement pays-région.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20donn%C3%A9es.ipynb">Notebook 01</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Explorer et pré-traiter</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Feature engineering des scores création, modernisation et gouvernance.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20donn%C3%A9es.ipynb">Notebook 01</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse univariée / multivariée</td><td style="padding: 10px 12px; border: 1px solid #ddd;">EDA et corrélations entre indicateurs métier.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/03%20-%20Analyses%20des%20groupements%20de%20pays%20-%20EDA%20Patrick%20-%20ACP-r%C3%A9ductions_dimensions-clustering%20.ipynb">Notebook 03</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Solution de visualisation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Carte choroplèthe, bar charts et scatter plots.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/raw/main/pbit/Dashboard_eau_v6.pbit">Téléchargement .pbit</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Créer un tableau de bord</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard Power BI complet sur 3 pages.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/raw/main/pbit/Dashboard_eau_v6.pbit">Téléchargement .pbit</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Reporting des tendances</td><td style="padding: 10px 12px; border: 1px solid #ddd;">KPI cards, line plots et matrice de priorisation.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md">Blueprint</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Veille métier / technologique</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Benchmark Power BI vs Tableau et méthodologie.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md">blueprint_P10_dashboard_eau.md</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Formaliser le cahier des charges</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Blueprint complet : besoins, indicateurs et visuels.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md">blueprint_P10_dashboard_eau.md</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Organiser un projet data</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pipeline en 3 notebooks et modules réutilisables.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/tree/main/notebooks">Notebooks</a> + <a href="https://github.com/ferialzamoun-afk/P10/tree/main/src">src/</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer la documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebooks, scripts, glossaire et méthodologie documentés.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10">Dépôt GitHub</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses multivariées</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Scoring composite pour prioriser les pays.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/03%20-%20Analyses%20des%20groupements%20de%20pays%20-%20EDA%20Patrick%20-%20ACP-r%C3%A9ductions_dimensions-clustering%20.ipynb">Notebook 03</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Réduction de dimension</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Sélection des indicateurs vers 3 domaines métier.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20donn%C3%A9es.ipynb">Notebook 01</a></td></tr>
   </tbody>
</table>

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
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Page</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Visuels</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Filtres</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Page 1 : Vue mondiale et continentale</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Carte choroplèthe, bar chart continent, KPI cards, Top N pays.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Année, région, action prioritaire.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Page 2 : Domaines métier</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Scatter plot création, grouped bar modernisation, scatter plot gouvernance, carte support.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Année, région, seuil population.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Page 3 : Vue nationale</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">KPI cards pays, line plots démographie et accès eau, tableau détaillé.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pays, année.</td></tr>
   </tbody>
</table>

**Artefacts clés** :
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Fichier</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Usage</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>Dashboard_eau_v6.pbit</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Modèle Power BI complet.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Visualisation directe.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>fact_dashboard_star_fr.csv</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Table de faits : pays, année, indicateurs.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Power BI et visualisations.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>dim_pays_star_fr.csv</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Dimension pays enrichie.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Contexte dans Power BI.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>csv_enrichis/fr/</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Marts analytiques français.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses complémentaires.</td></tr>
   </tbody>
</table>

---
### **🔹 Indicateurs Clés**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Domaine</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Indicateur</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Source</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Utilisation</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Stabilité politique</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>political_stability</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Banque Mondiale</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Carte choroplèthe, page 1.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Mortalité WASH</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>mortality_rate_water</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">OMS</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Ranking Top N, page 1.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Accès eau potable</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>basic_drinking_water</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">OMS/UNICEF</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Scatter plot, page 2.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Services safely managed</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>safely_managed_water</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">OMS/UNICEF</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Grouped bar chart, page 2.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Population rurale</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>rural_population</code></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Banque Mondiale</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Line plot, page 3.</td></tr>
   </tbody>
</table>

---
## **📂 Preuves et Documentation**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Type</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Lien</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Dépôt GitHub</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10">P10</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Code source, notebooks, scripts et données.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebook 01</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/01%20-%20Inspection%20des%20données.ipynb">Inspection & Normalisation</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Qualification, nettoyage et scores.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebook 02</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/02%20-%20Pr%C3%A9paration%20et%20nettoyage%20des%20donn%C3%A9es.ipynb">Préparation & Nettoyage</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pipeline en couches et tables étoile.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebook 03</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P10/blob/main/notebooks/03%20-%20Analyses%20des%20groupements%20de%20pays%20-%20EDA%20Patrick%20-%20ACP-r%C3%A9ductions_dimensions-clustering%20.ipynb">Analyses & EDA</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses métier et visualisations.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard Power BI</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/raw/main/pbit/Dashboard_eau_v6.pbit">Dashboard_eau_v6.pbit</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Modèle complet à ouvrir avec Power BI Desktop.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Blueprint</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/blob/main/docs/blueprint_P10_dashboard_eau.md">blueprint_P10_dashboard_eau.md</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Détail des besoins et visuels.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Glossaire</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/blob/main/docs/contexte_DWFA_glossaire_eau.md">contexte_DWFA_glossaire_eau.md</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Définitions des indicateurs.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Méthodologie</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/blob/main/docs/resume_methodologique_pipeline_notebooks_01_02_03.md">resume_methodologique_pipeline...</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Détails du pipeline.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">QCM Soutenance</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P10/blob/main/docs/questions_pieges_soutenance_P10.md">questions_pieges_soutenance_P10.md</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Points critiques pour l'évaluation.</td></tr>
   </tbody>
</table>

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
```

### **📌 Utilisation Programmatique**
*(Bloc RNCP37837BC04 : Gérer la documentation et formaliser les processus)*

```python
from src.data_manager import load_raw_data, publish_marts
from src.schema_fr import apply_schema_fr
from src.kpi_export import compute_scores

# Charger et transformer
data = load_raw_data()
data_fr = apply_schema_fr(data)
scores = compute_scores(data_fr)

# Publier les marts
publish_marts(scores, lang=['fr', 'en'])
```

### **⚠️ Qualité des Données et Audits**
*(Bloc RNCP37837BC02 : Identifier, collecter et analyser les données)*

#### **🔹 Points de Vigilance**

| Problème | Solution appliquée | Impact |
|----------|--------------------|--------|
| Mortalité WASH : Données disponibles surtout jusqu'à 2016 | Traitement des valeurs récentes avec prudence | Éviter les analyses temporelles sur 2017+ |
| Hétérogénéité des noms de pays | Standardisation via `country_converter` | 5 territoires exclus (Hong Kong, Macao, Taiwan, etc.) |
| Granularité population | Données annuelles validées (habitants) | Cohérence des agrégations |
| Couverture géographique | 193 pays attendus | Lacunes ciblées par `data_curation` |

#### **🔹 Audits Effectués**

✅ Validation des correspondances pays × région (12/06/2026).
✅ Suppression des écarts de structure entre les jeux EN et FR.
✅ Vérification des totaux de publication et des clés analytiques.
✅ Audit de concordance EN ↔ FR.

### **🔄 Maintenance et Mises à Jour**

#### **📌 Recalcul Complet**

- Placer les fichiers source dans `data/raw/`.
- Exécuter les 3 notebooks dans l'ordre.
- Les sorties seront publiées dans `data/processed/`.

#### **📌 Enrichissements Possibles**

- Ajout de nouveaux indicateurs (climat, budget, etc.).
- Extension régionale (sous-régions, bassins fluviaux).
- Intégration de données en temps réel.
- Versioning des modèles de score.

### **📌 Mapping RNCP 37837**

- ✅ BC01 : Structurer et gérer la base de données (tables étoile Power BI, marts analytiques)
- ✅ BC02 : Identifier, collecter et analyser les données (pipeline, nettoyage, EDA, scores)
- ✅ BC03 : Visualiser des données et interpréter des résultats (Dashboard Power BI, graphiques)
- ✅ BC04 : Piloter un projet data (documentation, CI, organisation, veille)
- ❌ BC05 : Spécialisation Statistiques (partiellement couvert via les scores composites, mais pas de modèles ML avancés)

