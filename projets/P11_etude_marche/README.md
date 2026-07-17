# 🌍 **P11 : Étude Marché – Priorisation des Pays pour l’Export de Poulets Biologiques**
**📅 Date** : 06/2026
**🏷️ Type** : Analyse Exploratoire / Clustering / Recommandation Stratégique
**🔗 Liens** :
- [🔗 Dépôt GitHub](https://github.com/ferialzamoun-afk/P11)
- [📓 Notebook 1 : Préparation & EDA (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb)
- [📓 Notebook 2 : Clustering & Recommandations (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb)
- [📄 Brief Projet](https://github.com/ferialzamoun-afk/P11/blob/main/PROJECT_BRIEF.md)
- [📄 Documentation Technique](https://github.com/ferialzamoun-afk/P11/blob/main/docs/documentation_technique.md)

---

## **🎯 Contexte et Objectifs**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

> **Contexte** :
> *"Ce projet répond à une **mission confiée par le PDG de *La Poule Qui Chante***, entreprise spécialisée dans la production de poulets biologiques. Dans un contexte de **concurrence accrue** et de **demande croissante en produits bio**, l’objectif était d’identifier des **marchés porteurs** à l’export pour étendre l’activité de l’entreprise."*

> **Objectifs Business** :
> - Identifier des **groupements de pays** à cibler pour l’export de poulets biologiques.
> - Proposer une **première priorisation** des marchés (**Top 5 pays** à approfondir).
> - **Optimiser la stratégie d’export** en croisant des critères **PESTEL+** (Politique, Économique, Social, Technologique, Environnemental, Sanitaire, Réglementaire).

> **Domaine de compétence** : Projet **documenté**, avec **reproductibilité** et **qualité logicielle** (CI/CD, tests unitaires).

---

## **📊 Structure du Projet**
```text
P11/
├── .github/
├── data/
├── docs/
├── notebooks/
├── output/
├── scripts/
├── src/
├── tests/
├── .gitignore
├── get_cell_ids.py
├── modify_notebook_19k.py
├── PROJECT_BRIEF.md
├── pyproject.toml
├── README.md
├── requirements.txt
├── verify_19k.py
└── VERSION
```
> **Note** :
> - Les **données brutes** et fichiers intermédiaires lourds sont **exclus du dépôt** (via `.gitignore`).
> - La version GitHub est **allégée** pour une consultation optimale.

---

## **🔧 Compétences RNCP 37837 Demonstrées**

### **📌 Mapping des Blocs RNCP**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Bloc RNCP</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Compétence</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuves</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC01</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Structurer et gérer la base de données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Base d'analyse finale de 139 pays et 16 variables candidates.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb#Constitution-de-la-base-ACP">Notebook 1</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier et collecter les données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Sources multiples : FAO, Banque Mondiale et autres données PESTEL+.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb#Préparation-des-données">Préparation des données</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Extraire et agréger</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Nettoyage, normalisation et enrichissement des données.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb#Nettoyage">Nettoyage</a> + <a href="https://github.com/ferialzamoun-afk/P11/blob/main/scripts/data_manager.py">data_manager.py</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Explorer et pré-traiter</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Feature engineering via <code>faolex_text_diversity_score</code>.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11/blob/main/scripts/enrich_market_features_model.py">enrich_market_features_model.py</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse univariée / multivariée</td><td style="padding: 10px 12px; border: 1px solid #ddd;">EDA et corrélations entre variables PESTEL+.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb#EDA">EDA</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Solution de visualisation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">ACP : 11 variables vers 3 composantes, 89.90% de variance.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_2_clustering_visualisations_112025.ipynb#ACP">ACP</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Créer un tableau de bord</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Clustering CAH et KMeans avec profils de clusters.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_2_clustering_visualisations_112025.ipynb#Clustering">Clustering</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Reporting des tendances</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Interprétation de 2 groupes de pays, prioritaire et secondaire.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_2_clustering_visualisations_112025.ipynb#Profils-de-clusters">Profils de clusters</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Veille métier / technologique</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Benchmark CAH vs KMeans et justification de <code>k=2</code>.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_2_clustering_visualisations_112025.ipynb#Choix-du-clustering">Choix du clustering</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Formaliser le cahier des charges</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Brief projet et documentation technique complète.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11/blob/main/PROJECT_BRIEF.md">PROJECT_BRIEF.md</a> + <a href="https://github.com/ferialzamoun-afk/P11/blob/main/docs/documentation_technique.md">documentation_technique.md</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Organiser un projet data</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pipeline documenté : notebooks, scripts et CI.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11/blob/main/docs/note_pipeline_preparation_nettoyage.md">note_pipeline_preparation_nettoyage.md</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer la documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Livrables documentés : notebooks, scripts et tests.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11">Dépôt GitHub</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses multivariées</td><td style="padding: 10px 12px; border: 1px solid #ddd;">ACP : 11 variables actives vers 3 composantes principales.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#ACP">ACP</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Réduction de dimension</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Réduction de 16 variables à 3 dimensions principales.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#ACP">ACP</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Tests statistiques</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Silhouette score d'environ 0.60 pour évaluer le clustering.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#Évaluation-du-clustering">Évaluation du clustering</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Entraîner un modèle</td><td style="padding: 10px 12px; border: 1px solid #ddd;">KMeans k=2 et CAH pour segmenter les pays.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#Clustering">Clustering</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Exploiter un modèle</td><td style="padding: 10px 12px; border: 1px solid #ddd;">16 pays prioritaires dans le cluster A.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_2_clustering_visualisations_112025.ipynb#Profils-de-clusters">Profils de clusters</a></td></tr>
   </tbody>
</table>

---

## **📊 Méthodologie**
*(Blocs RNCP37837BC02, BC03, BC05)*

### **🔹 Étapes Clés**
1. **Préparation des données** *(BC02)* :
   - Nettoyage (gestion des `NaN`, doublons).
   - **Feature Engineering** : Calcul de `faolex_text_diversity_score` (distance de Levenshtein normalisée sur les textes FAOLEX).
   - **Constitution de la base ACP** : 139 pays × 16 variables → `base_acp_finale_2017.csv`.

2. **Analyse Exploratoire (EDA)** *(BC02, BC03)* :
   - Statistiques descriptives (moyenne, écart-type, etc.).
   - **Analyse PESTEL+** : Étude des 6 dimensions (Politique, Économique, Social, Technologique, Environnemental, Sanitaire, Réglementaire).
   - Visualisations des corrélations entre variables.

3. **Réduction de Dimension (ACP)** *(BC03, BC05)* :
   - **11 variables actives** → **3 composantes principales** (PC1, PC2, PC3).
   - **89.90% de variance conservée**.

4. **Clustering** *(BC03, BC05)* :
   - **KMeans** (k=2) et **CAH** pour segmenter les pays.
   - **Silhouette Score** : ~0.60 (qualité du clustering).
   - **Justification de k=2** : Les solutions avec k≥4 créent des micro-clusters **moins exploitables métiers**.

5. **Recommandations** *(BC03, BC04)* :
   - **Top 5 pays** : Suisse 🇨🇭, Dominique 🇩🇲, Émirats Arabes Unis 🇦🇪, Belgique 🇧🇪, Autriche 🇦🇹.
   - **Shortlist 3** : Suisse, Dominique, Émirats Arabes Unis.
   - **Pays recommandé** : **Suisse** (score composite optimal, accord CAH/KMeans, dimensions ACP favorables).

---

## **📈 Résultats et Métriques**
*(Blocs RNCP37837BC03, BC05)*

### **🔹 Indicateurs Techniques**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Métrique</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Valeur</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Interprétation</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Nombre de pays analysés</td><td style="padding: 10px 12px; border: 1px solid #ddd;">139</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Base complète pour l’ACP et le clustering.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Variables actives (ACP)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">11</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Sélectionnées parmi 16 variables candidates.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Variance conservée (ACP)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">89.90%</td><td style="padding: 10px 12px; border: 1px solid #ddd;">3 composantes principales suffisent.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Nombre de clusters (KMeans)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">2</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Solution optimale pour une lecture métier simple.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Silhouette Score</td><td style="padding: 10px 12px; border: 1px solid #ddd;">~0.60</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Qualité bonne du clustering.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Pays prioritaires (Cluster A)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">16</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Marchés à instruire rapidement.</td></tr>
   </tbody>
</table>

### **🔹 Top 5 Pays à Approfondir**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Rang</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Pays</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Score Composite</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Justification</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">1</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Suisse 🇨🇭</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅✅✅</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Score maximal, accord CAH/KMeans et dimensions ACP favorables.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">2</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Dominique 🇩🇲</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅✅✅</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Proche de la Suisse par stabilité politique et demande bio.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">3</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Émirats Arabes Unis 🇦🇪</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅✅✅</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Fort pouvoir d’achat et importations élevées de volailles.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">4</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Belgique 🇧🇪</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅✅</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Marché proche géographiquement avec forte demande bio.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">5</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Autriche 🇦🇹</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅✅</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Culture bio développée et réglementation favorable.</td></tr>
   </tbody>
</table>

---
## **📂 Preuves et Livrables**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Type</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Lien</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th></tr></thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebook 1</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb">Préparation & EDA</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Préparation, nettoyage, feature engineering et ACP.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebook 2</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb">Clustering & Recommandations</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">ACP, CAH, KMeans, profils de clusters et recommandations.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Scripts</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11/tree/main/scripts">scripts/</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;"><code>data_manager.py</code> et <code>enrich_market_features_model.py</code>.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Tests</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11/tree/main/tests">tests/</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">16 tests unitaires pour les fonctions critiques.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">CI/CD</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11/blob/main/.github/workflows/ci.yml">.github/workflows/ci.yml</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Workflow GitHub Actions : ruff, pytest, smoke checks.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Brief Projet</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11/blob/main/PROJECT_BRIEF.md">PROJECT_BRIEF.md</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Contexte, objectifs et livrables.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P11/tree/main/docs">docs/</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Documentation technique et note pipeline.</td></tr>
   </tbody>
</table>

---
## **🚀 Démarrage Rapide**
*(Pour reproduire le projet en local)*

<pre><code># 1. Cloner le dépôt
git clone https://github.com/ferialzamoun-afk/P11.git
cd P11

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Exécuter les tests (optionnel)
pip install pytest ruff nbformat nbconvert ipykernel
ruff check scripts/enrich_market_features_model.py tests --ignore E501,W293
pytest -q

# 4. Ouvrir les notebooks (dans l'ordre)
jupyter notebook notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb
jupyter notebook notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb</code></pre>

## **✅ Qualité Logicielle**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

- Linting : `ruff` pour vérifier la qualité du code (scripts + tests).
- Tests unitaires : 16 tests couvrant :

   - Normalisation des textes (`test_data_prep.py`).
   - Distance de Levenshtein et diversité (`test_enrich_market_features_model.py`).

- Smoke checks : Vérification des fonctions critiques.
- Validation des notebooks :

   - Structure JSON valide (`nbformat`).
   - Volume minimal de cellules code/markdown.
   - Absence d’erreurs enregistrées.

- CI/CD : Workflow GitHub Actions pour automatiser les vérifications.

## **🎯 Mapping RNCP 37837**

Blocs couverts par ce projet :

- ✅ BC01 : Structurer et gérer la base de données (`base_acp_finale_2017.csv`)
- ✅ BC02 : Identifier, collecter et analyser les données (nettoyage, EDA, feature engineering)
- ✅ BC03 : Visualiser des données et interpréter des résultats (ACP, clustering, graphiques)
- ✅ BC04 : Piloter un projet data (documentation, CI/CD, veille, organisation)
- ✅ BC05 : Spécialisation Statistiques (ACP, clustering, tests statistiques, réduction de dimension)