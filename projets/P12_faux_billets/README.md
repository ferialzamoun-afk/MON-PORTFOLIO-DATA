# 🎯 Projet P12 : Détection de Faux Billets par Machine Learning
**📅 Date** : Juillet 2026
**🏷️ Type** : Machine Learning / Classification / Analyse Statistique
**🔗 Lien** : [Notebook Jupyter complet](assets/notebook/p12_da_maj%2B%281%29.ipynb)   [Dépôt GitHub](https://github.com/ferialzamoun-afk/P12)

---
---

## **🎯 Contexte et Objectifs**
*(Bloc RNCP37837BC04 : Piloter un projet data)*
> **Contexte** :
> *"Projet réalisé pour l’**Organisation Nationale de Lutte contre le Faux-Monnayage (ONFM)**, en conformité avec les **standards EMV** (European Payments Council). La fraude aux faux billets représente un **enjeu financier et sécuritaire** pour les institutions bancaires, avec des pertes estimées à plusieurs millions d’euros par an en Europe."*

> **Objectifs** :
> - Développer un **modèle de classification binaire** pour distinguer les vrais des faux billets.
> - Atteindre un **recall de 100%** sur les faux billets (aucun faux négatif).
> - **Automatiser** la détection pour réduire la dépendance aux contrôles manuels.
> - **Documenter** le processus pour une réutilisation par l’ONFM.

---
---

## **📁 Structure du Dépôt**
```text
P12/
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
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Procfile
├── PROJECT_BRIEF.md
├── README.md
├── pytest.ini
├── requirements.txt
├── start.py
└── venv/
```

---
---

## **📚 Notebook Unique : Structure et Mapping RNCP**
*(Chaque section du notebook correspond à un bloc RNCP. Utilise des **ancres** dans le notebook pour faciliter la navigation.)*

### **📌 Lien vers le Notebook**
👉 **[Ouvrir le Notebook Jupyter complet](assets/notebook/p12_da_maj%2B%281%29.ipynb)**
*(Le notebook est organisé en **sections claires**, chacune liée à un bloc RNCP. Voici le détail :)*

---

### **🔹 [RNCP37837BC01] Structurer et gérer la base de données**
*(Non applicable à P12, car pas de base SQL. Mais si tu as utilisé un DataFrame Pandas comme "base de données temporaire", tu peux l’inclure.)*
> **⚠️ Note** :
> *"Ce projet n’utilise pas de base de données SQL, mais les données ont été **structurées en DataFrame Pandas** avec des relations entre les features (ex: liens entre les motifs et les labels)."*
> **Preuve** : [Section RNCP BC01 du notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc01)

---

### **🔹 [RNCP37837BC02] Identifier, collecter et analyser les données**
*(Ce bloc est **100% couvert** par ton notebook.)*

| **Compétence RNCP** | **Ce que j’ai fait** | **Section du Notebook** | **Preuve** |
|----------------------|-----------------------|-------------------------|------------|
| **Identifier et collecter** | Utilisation du **dataset ONFM** (images de billets + labels) en respectant les normes EMV. | [Section RNCP BC02](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) |
| **Extraire et agréger** | Nettoyage des données : gestion des **valeurs manquantes**, suppression des doublons. | [Section RNCP BC02](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) |
| **Explorer et pré-traiter** | **Feature Engineering** : sélection et préparation des variables pour la classification. | [Section RNCP BC02](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) |
| **Vérifier la cohérence** | Vérification de la **fiabilité des données** (statistiques descriptives, distributions). | [Section RNCP BC02](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) |
| **Traiter les données manquantes** | Imputation des valeurs manquantes (moyenne, médiane) et gestion des outliers. | [Section RNCP BC02](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) |
| **Analyse temporelle** | *Non applicable* (pas de séries temporelles dans P12). | - | - |
| **Analyse univariée/multivariée** | Analyse des **distributions** (histogrammes, boxplots) et **corrélations** entre features. | [Section RNCP BC02](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc02) |

---
---

### **🔹 [RNCP37837BC03] Visualiser des données et interpréter des résultats**
*(Ce bloc est **100% couvert** par les visualisations dans ton notebook.)*

| **Compétence RNCP** | **Ce que j’ai fait** | **Section du Notebook** | **Preuve** |
|----------------------|-----------------------|-------------------------|------------|
| **Solution de visualisation** | Création de **graphiques adaptés** (histogrammes, boxplots, matrice de corrélation) avec Matplotlib/Seaborn. | [Section RNCP BC03](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) |
| **Graphiques accessibles** | Respect des **bonnes pratiques** (titres, légendes, couleurs contrastées). | [Section RNCP BC03](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) |
| **Créer un tableau de bord** | *Non applicable* (pas de tableau de bord interactif dans P12). | - | - |
| **Reporting des tendances** | **Interprétation des graphiques** (ex: "La distribution des probabilités montre une séparation nette entre vrais et faux billets"). | [Section RNCP BC03](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) |
| **Récit des résultats** | **Synthèse narrative** des résultats dans le notebook (cellules Markdown). | [Section RNCP BC03](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) |
| **Présenter les résultats** | **Adaptation du contenu** pour un public technique (ONFM) et non-technique (slides séparés). | [Section RNCP BC03](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc03) + [Dépôt GitHub](https://github.com/ferialzamoun-afk/P12) |

---
---

### **🔹 [RNCP37837BC04] Piloter un projet data en respectant la réglementation**
*(Ce bloc est **couvert** par la documentation et la veille dans ton notebook.)*

| **Compétence RNCP** | **Ce que j’ai fait** | **Section du Notebook** | **Preuve** |
|----------------------|-----------------------|-------------------------|------------|
| **Veille métier/technologique** | Recherche sur les **standards EMV** et benchmark des outils de classification (Scikit-learn vs PyTorch). | [Section RNCP BC04](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) + [Note de veille EMV](assets/veille/recherche_standards_emv_detection_fraude.md) |
| **Expérimenter de nouvelles méthodes** | Comparaison de **plusieurs algorithmes** ; la **Logistic Regression** a été retenue après cross-validation. | [Section RNCP BC04](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) |
| **Identifier le besoin métier** | **Traduction des besoins ONFM** en objectifs techniques (détection automatique, conformité EMV). | [Section RNCP BC04](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) |
| **Formaliser le cahier des charges** | **Documentation complète** dans le notebook (objectifs, méthodologie, résultats). | [Section RNCP BC04](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) |
| **Organiser un projet data** | **Structuration du notebook** en sections claires (EDA, Modélisation, Évaluation). | [Notebook RNCP BC04](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) | [Dépôt GitHub](https://github.com/ferialzamoun-afk/P12) |
| **Ateliers de formation** | *Non applicable* (pas d’atelier dans P12). | - | - |
| **Gérer la documentation** | **Commentaires détaillés** dans le code et cellules Markdown explicatives. | [Notebook RNCP BC04](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) | [Dépôt GitHub](https://github.com/ferialzamoun-afk/P12) |
| **Adapter sa posture** | **Positionnement comme consultante** : explications claires pour l’ONFM. | [Section RNCP BC04](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc04) |

---
---

### **🔹 [RNCP37837BC05] Spécialisation Statistiques : Tests et Modèles d’apprentissage**
*(Ce bloc est **100% couvert** par ton notebook.)*

| **Compétence RNCP** | **Ce que j’ai fait** | **Section du Notebook** | **Preuve** |
|----------------------|-----------------------|-------------------------|------------|
| **Analyses multivariées** | Étude des **corrélations entre features** (matrice de corrélation). | [Section RNCP BC05](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) |
| **Réduction de dimension** | *Non applicable* (pas de PCA ou t-SNE dans P12). | - | - |
| **Tests statistiques** | **Validation croisée** et tests de robustesse (ex: test sur différents sous-ensembles). | [Section RNCP BC05](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) |
| **Feature Engineering (non supervisé)** | Sélection des **variables pertinentes** pour la classification. | [Section RNCP BC05](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) |
| **Entraîner un modèle** | **Classification binaire** avec Scikit-learn (Logistic Regression). | [Section RNCP BC05](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) |
| **Exploiter un modèle** | **Évaluation des performances** (matrice de confusion, métriques). | [Section RNCP BC05](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) |
| **Choisir un modèle adapté** | Justification du choix du modèle retenu après comparaison. | [Section RNCP BC05](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb#rncp-bc05) |
| **Analyse de séries temporelles** | *Non applicable* (pas de séries temporelles dans P12). | - | - |

---
---
---

## **📊 Méthodologie**
*(Bloc RNCP37837BC04 : Piloter un projet data)*
> **Étapes** :
> 1. **Contexte et Veille** : Recherche sur les standards EMV et les outils de détection de fraude ([note detaillee](assets/veille/recherche_standards_emv_detection_fraude.md), [documentation technique](assets/documentation/DOC_TECHNIQUE_PIPELINE_FAUX_BILLETS.md), [cahier des charges](assets/cahier_des_charges/PROJECT_BRIEF.md)).
> 2. **Chargement des données** : Import du dataset ONFM (images + labels).
> 3. **Nettoyage des données** : Gestion des valeurs manquantes, suppression des doublons.
> 4. **Feature Engineering** : Extraction de caractéristiques (motifs, hologrammes).
> 5. **Analyse Exploratoire (EDA)** : Statistiques descriptives, visualisations (histogrammes, matrice de corrélation).
> 6. **Modélisation** : Implémentation d’un modèle de classification binaire (Logistic Regression).
> 7. **Évaluation du Modèle** : Validation croisée, matrice de confusion, métriques (accuracy, recall, F1-score).
> 8. **Interprétation des Résultats** : Synthèse narrative et recommandations pour l’ONFM.

---
---
---

## **📈 Résultats**
*(Bloc RNCP37837BC03 et BC05 : Visualiser et Modéliser)*
> **Métriques** :
> - **Accuracy** : 88%
> - **Recall (Faux Billets)** : 100% *(Aucun faux billet non détecté)*
> - **F1-Score** : 0.91
> - **Précision** : 89%

> **Visualisations** :
> - **Matrice de confusion** : [Voir la visualisation dans le notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb)
>   *0 faux négatifs : tous les faux billets sont détectés.*
> - **Graphique de distribution des probabilités** : [Voir la visualisation dans le notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb)
>   *Séparation nette entre vrais (prob < 0.5) et faux billets (prob > 0.5).* 

---
---
---


| **Type** | **Lien** | **Description** |
|----------|----------|-----------------|
| **Notebook Jupyter** | [Notebook](assets/notebook/p12_da_maj%2B%281%29.ipynb) | Notebook complet avec **toutes les sections** (EDA, modélisation, évaluation). |
| **Dépôt GitHub** | [Dépôt P12](https://github.com/ferialzamoun-afk/P12) | Code source, README, et images (matrice de confusion, graphiques). |
| **Slides de présentation** | [Dépôt GitHub](https://github.com/ferialzamoun-afk/P12) | Présentation des résultats pour l’ONFM (public non-technique). |
| **Images** | [Dépôt P12](https://github.com/ferialzamoun-afk/P12) | Captures d’écran des visualisations (matrice de confusion, graphiques). |

---
---
---

## **🚀 Améliorations Futures**
> - Tester **XGBoost** ou d'autres variantes si un futur besoin métier le justifie.
> - Intégrer un **système de logging** pour le monitoring en production.
> - Explorer le **Deep Learning** (CNN) pour la détection d’images.
> - **Automatiser** le pipeline de détection (FastAPI + modèle déployé).

---
---
---
## **🎯 Mapping RNCP 37837**
> **Blocs couverts par ce projet** :
> - ✅ **BC02** : Identifier, collecter et analyser les données *(Nettoyage, Feature Engineering, EDA)*
> - ✅ **BC03** : Visualiser des données et interpréter des résultats *(Graphiques, matrice de confusion, interprétation)*
> - ✅ **BC04** : Piloter un projet data en respectant la réglementation *(Veille, documentation, posture consultante)*
> - ✅ **BC05** : Spécialisation Statistiques *(Modélisation, tests statistiques, feature engineering)*
> - ❌ **BC01** : Structurer et gérer la base de données *(Non applicable : pas de base SQL dans ce projet)*

## 👩‍💻 Auteur

Férial Zamoun  
Formation Data Analyst - GRETA Promo P5- 2025  
Objectif : Recherche CDI et poursuite en RNCP37744 -data-scientist-machine-learning (Septembre 2026)