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
| **Bloc RNCP** | **Compétence** | **Description** | **Preuves** |
|---------------|---------------|----------------|-------------|
| **BC01** | **Structurer et gérer la base de données** | Création d’une **base d’analyse finale** (`base_acp_finale_2017.csv`) avec 139 pays et 16 variables candidates. | [Notebook 1, Section "Constitution de la base ACP"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb#Constitution-de-la-base-ACP) |
| **BC02** | **Identifier et collecter les données** | Utilisation de **sources multiples** (FAO, Banque Mondiale, etc.) pour les variables PESTEL+. | [Notebook 1, Section "Préparation des données"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb#Préparation-des-données) |
| **BC02** | **Extraire et agréger** | Nettoyage des données (gestion des `NaN`, normalisation, enrichissement). | [Notebook 1, Section "Nettoyage"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb#Nettoyage) + [scripts/data_manager.py](https://github.com/ferialzamoun-afk/P11/blob/main/scripts/data_manager.py) |
| **BC02** | **Explorer et pré-traiter** | **Feature Engineering** : Calcul de `faolex_text_diversity_score` (distance de Levenshtein normalisée). | [scripts/enrich_market_features_model.py](https://github.com/ferialzamoun-afk/P11/blob/main/scripts/enrich_market_features_model.py) |
| **BC02** | **Analyse univariée/multivariée** | **EDA** : Statistiques descriptives, corrélations entre variables PESTEL+. | [Notebook 1, Section "EDA"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb#EDA) |
| **BC03** | **Solution de visualisation** | **ACP** : Réduction de dimension (11 variables → 3 composantes principales, 89.90% de variance conservée). | [Notebook 2, Section "ACP"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#ACP) |
| **BC03** | **Créer un tableau de bord** | **Clustering** (CAH, KMeans) avec visualisations des profils de clusters. | [Notebook 2, Section "Clustering"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#Clustering) |
| **BC03** | **Reporting des tendances** | **Interprétation des clusters** : Identification de 2 groupes de pays (prioritaire/secondaire). | [Notebook 2, Section "Profils de clusters"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#Profils-de-clusters) |
| **BC04** | **Veille métier/technologique** | **Benchmark des méthodes** (CAH vs KMeans) et justification du choix de `k=2`. | [Notebook 2, Section "Choix du clustering"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#Choix-du-clustering) |
| **BC04** | **Formaliser le cahier des charges** | **Brief projet** et **documentation technique** complète. | [PROJECT_BRIEF.md](https://github.com/ferialzamoun-afk/P11/blob/main/PROJECT_BRIEF.md) + [docs/documentation_technique.md](https://github.com/ferialzamoun-afk/P11/blob/main/docs/documentation_technique.md) |
| **BC04** | **Organiser un projet data** | **Pipeline documenté** (notebooks + scripts + CI). | [docs/note_pipeline_preparation_nettoyage.md](https://github.com/ferialzamoun-afk/P11/blob/main/docs/note_pipeline_preparation_nettoyage.md) |
| **BC04** | **Gérer la documentation** | **100% des livrables documentés** (notebooks, scripts, tests). | [Dépôt GitHub](https://github.com/ferialzamoun-afk/P11) |
| **BC05** | **Analyses multivariées** | **ACP** : 11 variables actives → 3 composantes principales (89.90% de variance). | [Notebook 2, Section "ACP"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#ACP) |
| **BC05** | **Réduction de dimension** | **ACP** : Réduction de 16 variables → 3 dimensions principales. | [Notebook 2, Section "ACP"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#ACP) |
| **BC05** | **Tests statistiques** | **Silhouette Score** (~0.60) pour évaluer la qualité du clustering. | [Notebook 2, Section "Évaluation du clustering"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#Évaluation-du-clustering) |
| **BC05** | **Entraîner un modèle** | **KMeans** (k=2) et **CAH** pour segmenter les pays. | [Notebook 2, Section "Clustering"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#Clustering) |
| **BC05** | **Exploiter un modèle** | **Profil des clusters** : 16 pays prioritaires (Cluster A) vs autres. | [Notebook 2, Section "Profils de clusters"](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb#Profils-de-clusters) |

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
| **Métrique** | **Valeur** | **Interprétation** |
|--------------|------------|-------------------|
| **Nombre de pays analysés** | 139 | Base complète pour l’ACP et le clustering. |
| **Variables actives (ACP)** | 11 | Sélectionnées parmi 16 variables candidates. |
| **Variance conservée (ACP)** | 89.90% | 3 composantes principales suffisent. |
| **Nombre de clusters (KMeans)** | 2 | Solution optimale pour une **lecture métier simple**. |
| **Silhouette Score** | ~0.60 | Qualité **bonne** du clustering (proche de 1). |
| **Pays prioritaires (Cluster A)** | 16 | Marchés à **instruire rapidement**. |

### **🔹 Top 5 Pays à Approfondir**
| **Rang** | **Pays** | **Score Composite** | **Justification** |
|----------|----------|---------------------|------------------|
| 1 | **Suisse 🇨🇭** | ✅✅✅ | **Score maximal**, accord CAH/KMeans, dimensions ACP favorables. |
| 2 | **Dominique 🇩🇲** | ✅✅✅ | Proche de la Suisse en termes de **stabilité politique** et **demande bio**. |
| 3 | **Émirats Arabes Unis 🇦🇪** | ✅✅✅ | **Fort pouvoir d’achat** (GDP/capita), **importations élevées** de volailles. |
| 4 | **Belgique 🇧🇪** | ✅✅ | Marché **proche géographiquement**, **demande bio forte**. |
| 5 | **Autriche 🇦🇹** | ✅✅ | **Culture bio développée**, **réglementation favorable**. |

---
## **📂 Preuves et Livrables**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

| **Type** | **Lien** | **Description** |
|----------|----------|-----------------|
| **Notebook 1** | [Préparation & EDA (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb) | Préparation, nettoyage, feature engineering, ACP. |
| **Notebook 2** | [Clustering & Recommandations (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb) | ACP, CAH, KMeans, profils de clusters, recommandations. |
| **Scripts** | [scripts/](https://github.com/ferialzamoun-afk/P11/tree/main/scripts) | `data_manager.py` + `enrich_market_features_model.py`. |
| **Tests** | [tests/](https://github.com/ferialzamoun-afk/P11/tree/main/tests) | 16 tests unitaires (pytest) pour les fonctions critiques. |
| **CI/CD** | [.github/workflows/ci.yml](https://github.com/ferialzamoun-afk/P11/blob/main/.github/workflows/ci.yml) | Workflow GitHub Actions (ruff, pytest, smoke checks). |
| **Brief Projet** | [PROJECT_BRIEF.md](https://github.com/ferialzamoun-afk/P11/blob/main/PROJECT_BRIEF.md) | Contexte, objectifs, livrables. |
| **Documentation** | [docs/](https://github.com/ferialzamoun-afk/P11/tree/main/docs) | Documentation technique et note pipeline. |

---
## **🚀 Démarrage Rapide**
*(Pour reproduire le projet en local)*

```bash
# 1. Cloner le dépôt
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
jupyter notebook notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb

✅ Qualité Logicielle
(Bloc RNCP37837BC04 : Piloter un projet data)

Linting : ruff pour vérifier la qualité du code (scripts + tests).
Tests unitaires : 16 tests couvrant :

Normalisation des textes (test_data_prep.py).
Distance de Levenshtein et diversité (test_enrich_market_features_model.py).

Smoke checks : Vérification des fonctions critiques.
Validation des notebooks :

Structure JSON valide (nbformat).
Volume minimal de cellules code/markdown.
Absence d’erreurs enregistrées.

CI/CD : Workflow GitHub Actions pour automatiser les vérifications.

🎯 Mapping RNCP 37837

Blocs couverts par ce projet :

✅ BC01 : Structurer et gérer la base de données (base_acp_finale_2017.csv)
✅ BC02 : Identifier, collecter et analyser les données (nettoyage, EDA, feature engineering)
✅ BC03 : Visualiser des données et interpréter des résultats (ACP, clustering, graphiques)
✅ BC04 : Piloter un projet data (documentation, CI/CD, veille, organisation)
✅ BC05 : Spécialisation Statistiques (ACP, clustering, tests statistiques, réduction de dimension)