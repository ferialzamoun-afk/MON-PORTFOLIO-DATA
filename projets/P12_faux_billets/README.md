# # 🎯 Projet P12 : Détection de Faux Billets par Machine Learning
**📅 Date** : Juillet 2026
**🏷️ Type** : Machine Learning / Classification / Analyse Statistique
**🔗 Lien** : [Notebook Jupyter complet](https://github.com/ferialzamoun-afk/P12/blob/main/projets/P12_faux_billets/assets/p12_da_maj%20(1).ipynb)   [Dépôt GitHub](https://github.com/ferialzamoun-afk/P12)

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

## **📚 Notebook Unique : Structure et Mapping RNCP**
*(Chaque section du notebook correspond à un bloc RNCP. Utilise des **ancres** dans le notebook pour faciliter la navigation.)*

### **📌 Lien vers le Notebook**
👉 **[Ouvrir le Notebook Jupyter complet](projets\P12_faux_billets\assets\p12_da_maj+(1).ipynb)**
*(Le notebook est organisé en **sections claires**, chacune liée à un bloc RNCP. Voici le détail :)*

---

### **🔹 [RNCP37837BC01] Structurer et gérer la base de données**
*(Non applicable à P12, car pas de base SQL. Mais si tu as utilisé un DataFrame Pandas comme "base de données temporaire", tu peux l’inclure.)*
> **⚠️ Note** :
> *"Ce projet n’utilise pas de base de données SQL, mais les données ont été **structurées en DataFrame Pandas** avec des relations entre les features (ex: liens entre les motifs et les labels)."*
> **Preuve** : [Section "1. Chargement et Structuration des Données" du notebook](#1.-Chargement-et-Structuration-des-Données)

---

### **🔹 [RNCP37837BC02] Identifier, collecter et analyser les données**
*(Ce bloc est **100% couvert** par ton notebook.)*
 | **Compétence RNCP** | **Ce que j’ai fait** | **Section du Notebook** | **Preuve** |
 |----------------------|-----------------------|-------------------------|------------|
 | **Identifier et collecter** | Utilisation du **dataset ONFM** (images de billets + labels) en respectant les normes EMV. | [Section "1. Chargement des données"](#1.-Chargement-des-données) | [Notebook](#1.-Chargement-des-données) |
 | **Extraire et agréger** | Nettoyage des données : gestion des **valeurs manquantes**, suppression des doublons. | [Section "2. Nettoyage des données"](#2.-Nettoyage-des-données) | [Notebook](#2.-Nettoyage-des-données) |
 | **Explorer et pré-traiter** | **Feature Engineering** : Extraction de caractéristiques (motifs, hologrammes, taille) à partir des images. | [Section "3. Feature Engineering"](#3.-Feature-Engineering) | [Notebook](#3.-Feature-Engineering) |
 | **Vérifier la cohérence** | Vérification de la **fiabilité des données** (statistiques descriptives, distributions). | [Section "4. Analyse Exploratoire (EDA)"](#4.-Analyse-Exploratoire-(EDA)) | [Notebook](#4.-Analyse-Exploratoire-(EDA)) |
 | **Traiter les données manquantes** | Imputation des valeurs manquantes (moyenne, médiane) et gestion des outliers. | [Section "2. Nettoyage des données"](#2.-Nettoyage-des-données) | [Notebook](#2.-Nettoyage-des-données) |
 | **Analyse temporelle** | *Non applicable* (pas de séries temporelles dans P12). | - | - |
 | **Analyse univariée/multivariée** | Analyse des **distributions** (histogrammes, boxplots) et **corrélations** entre features. | [Section "4. Analyse Exploratoire (EDA)"](#4.-Analyse-Exploratoire-(EDA)) | [Notebook](#4.-Analyse-Exploratoire-(EDA)) |

---
---

### **🔹 [RNCP37837BC03] Visualiser des données et interpréter des résultats**
*(Ce bloc est **100% couvert** par les visualisations dans ton notebook.)*
 | **Compétence RNCP** | **Ce que j’ai fait** | **Section du Notebook** | **Preuve** |
 |----------------------|-----------------------|-------------------------|------------|
 | **Solution de visualisation** | Création de **graphiques adaptés** (histogrammes, boxplots, matrice de corrélation) avec Matplotlib/Seaborn. | [Section "4. Analyse Exploratoire (EDA)"](#4.-Analyse-Exploratoire-(EDA)) | [Notebook](#4.-Analyse-Exploratoire-(EDA)) |
 | **Graphiques accessibles** | Respect des **bonnes pratiques** (titres, légendes, couleurs contrastées). | [Section "4. Analyse Exploratoire (EDA)"](#4.-Analyse-Exploratoire-(EDA)) | [Notebook](#4.-Analyse-Exploratoire-(EDA)) |
 | **Créer un tableau de bord** | *Non applicable* (pas de tableau de bord interactif dans P12). | - | - |
 | **Reporting des tendances** | **Interprétation des graphiques** (ex: "La distribution des probabilités montre une séparation nette entre vrais et faux billets"). | [Section "5. Interprétation des Résultats"](#5.-Interprétation-des-Résultats) | [Notebook](#5.-Interprétation-des-Résultats) |
 | **Récit des résultats** | **Synthèse narrative** des résultats dans le notebook (cellules Markdown). | [Section "5. Interprétation des Résultats"](#5.-Interprétation-des-Résultats) | [Notebook](#5.-Interprétation-des-Résultats) |
 | **Présenter les résultats** | **Adaptation du contenu** pour un public technique (ONFM) et non-technique (slides séparés). | [Section "5. Interprétation des Résultats"](#5.-Interprétation-des-Résultats) | [Notebook](#5.-Interprétation-des-Résultats) + [Slides](lien) |

---
---

### **🔹 [RNCP37837BC04] Piloter un projet data en respectant la réglementation**
*(Ce bloc est **couvert** par la documentation et la veille dans ton notebook.)*
 | **Compétence RNCP** | **Ce que j’ai fait** | **Section du Notebook** | **Preuve** |
 |----------------------|-----------------------|-------------------------|------------|
 | **Veille métier/technologique** | Recherche sur les **standards EMV** et benchmark des outils de classification (Scikit-learn vs PyTorch). | [Section "0. Contexte et Veille"](#0.-Contexte-et-Veille) | [Notebook](#0.-Contexte-et-Veille) |
 | **Expérimenter de nouvelles méthodes** | Test de **différents algorithmes** (Logistic Regression, Random Forest) pour comparer les performances. | [Section "6. Expérimentations"](#6.-Expérimentations) | [Notebook](#6.-Expérimentations) |
 | **Identifier le besoin métier** | **Traduction des besoins ONFM** en objectifs techniques (détection automatique, conformité EMV). | [Section "0. Contexte et Veille"](#0.-Contexte-et-Veille) | [Notebook](#0.-Contexte-et-Veille) |
 | **Formaliser le cahier des charges** | **Documentation complète** dans le notebook (objectifs, méthodologie, résultats). | [Section "0. Contexte et Objectifs"](#0.-Contexte-et-Objectifs) | [Notebook](#0.-Contexte-et-Objectifs) |
 | **Organiser un projet data** | **Structuration du notebook** en sections claires (EDA, Modélisation, Évaluation). | [Notebook complet](#) | [Notebook](lien) |
 | **Ateliers de formation** | *Non applicable* (pas d’atelier dans P12). | - | - |
 | **Gérer la documentation** | **Commentaires détaillés** dans le code et cellules Markdown explicatives. | [Notebook complet](#) | [Notebook](lien) |
 | **Adapter sa posture** | **Positionnement comme consultante** : explications claires pour l’ONFM. | [Section "5. Interprétation des Résultats"](#5.-Interprétation-des-Résultats) | [Notebook](#5.-Interprétation-des-Résultats) |

---
---

### **🔹 [RNCP37837BC05] Spécialisation Statistiques : Tests et Modèles d’apprentissage**
*(Ce bloc est **100% couvert** par ton notebook.)*
 | **Compétence RNCP** | **Ce que j’ai fait** | **Section du Notebook** | **Preuve** |
 |----------------------|-----------------------|-------------------------|------------|
 | **Analyses multivariées** | Étude des **corrélations entre features** (matrice de corrélation). | [Section "4. Analyse Exploratoire (EDA)"](#4.-Analyse-Exploratoire-(EDA)) | [Notebook](#4.-Analyse-Exploratoire-(EDA)) |
 | **Réduction de dimension** | *Non applicable* (pas de PCA ou t-SNE dans P12). | - | - |
 | **Tests statistiques** | **Validation croisée** et tests de robustesse (ex: test sur différents sous-ensembles). | [Section "7. Évaluation du Modèle"](#7.-Évaluation-du-Modèle) | [Notebook](#7.-Évaluation-du-Modèle) |
 | **Feature Engineering (non supervisé)** | Sélection des **variables pertinentes** (motifs, hologrammes) pour la classification. | [Section "3. Feature Engineering"](#3.-Feature-Engineering) | [Notebook](#3.-Feature-Engineering) |
 | **Entraîner un modèle** | **Classification binaire** avec Scikit-learn (Logistic Regression). | [Section "6. Modélisation"](#6.-Modélisation) | [Notebook](#6.-Modélisation) |
 | **Exploiter un modèle** | **Évaluation des performances** (matrice de confusion, métriques). | [Section "7. Évaluation du Modèle"](#7.-Évaluation-du-Modèle) | [Notebook](#7.-Évaluation-du-Modèle) |
 | **Choisir un modèle adapté** | Justification du choix de la **Logistic Regression** (simplicité, efficacité sur ce dataset). | [Section "6. Modélisation"](#6.-Modélisation) | [Notebook](#6.-Modélisation) |
 | **Analyse de séries temporelles** | *Non applicable* (pas de séries temporelles dans P12). | - | - |

---
---
---

## **📊 Méthodologie**
*(Bloc RNCP37837BC04 : Piloter un projet data)*
> **Étapes** :
> 1. **Contexte et Veille** : Recherche sur les standards EMV et les outils de détection de fraude.
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
> - **Matrice de confusion** :
>   ![Matrice de confusion](images/matrice_confusion_P12.png)
>   *0 faux négatifs : tous les faux billets sont détectés.*
> - **Graphique de distribution des probabilités** :
>   ![Distribution des probabilités](images/distribution_probabilites_P12.png)
>   *Séparation nette entre vrais (prob < 0.5) et faux billets (prob > 0.5).*

---
---
---

## **📂 Preuves et Livrables**
 | **Type** | **Lien** | **Description** |
 |----------|----------|-----------------|
 | **Notebook Jupyter** | [Lien vers le notebook](lien) | Notebook complet avec **toutes les sections** (EDA, modélisation, évaluation). |
 | **Dépôt GitHub** | [Lien vers le dépôt](lien) | Code source, README, et images (matrice de confusion, graphiques). |
 | **Slides de présentation** | [Lien vers les slides](lien) | Présentation des résultats pour l’ONFM (public non-technique). |
 | **Images** | [Dossier `/images`](lien) | Captures d’écran des visualisations (matrice de confusion, graphiques). |

---
---
---

## **🚀 Améliorations Futures**
> - Tester **XGBoost/Random Forest** pour améliorer la précision.
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