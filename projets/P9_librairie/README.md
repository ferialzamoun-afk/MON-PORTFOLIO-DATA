# 📚 **P9 : Analyse des Ventes – Librairie Lapage**
**Projet d'analyse de données et de visualisation pour suivre la performance commerciale, comprendre les comportements clients et fournir des livrables exploitables par le CODIR.**

**📅 Date** : 04/2026
**🏷️ Type** : Analyse Statistique / Dashboard Streamlit
**🔗 Liens** :
- [🔗 Dépôt GitHub - Analyses](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies)
- [🌐 Dashboard Streamlit (Production)](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/)
- [📁 Code Source Dashboard](https://github.com/ferialzamoun-afk/P9-lapage-streamlit)
- [📓 Notebooks Jupyter](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/notebooks/analyses/)
- [📁 Documentation](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/docs/)
- [✅ Workflow Tests (pytest)](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml)

---

## **🎯 Contexte et Objectifs**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

> **Contexte** :
> *"Projet réalisé pour la **librairie Lapage**, dans le cadre d’une **analyse data-driven** visant à optimiser la performance commerciale et la stratégie client. La librairie cherche à **comprendre ses données de vente** pour prendre des décisions éclairées en matière de **marketing, gestion des stocks et expérience client**."*

> **Objectifs Métier** :
> - **Suivre la performance commerciale** :
>   - Chiffre d’affaires (CA), panier moyen, concentration des ventes.
>   - Analyse des **tendances temporelles** (mensuelles, saisonnières).
> - **Comprendre les comportements clients** :
>   - Segmentation des clients (fréquence d’achat, catégories préférées).
>   - Identification des **segments clés** (ex: clients réguliers vs occasionnels).
> - **Fournir des livrables exploitables** :
>   - **Notebooks** d’analyse statistique (axes Marketing et BI).
>   - **Dashboard Streamlit** multi-pages pour le CODIR.
>   - **Exports KPI** (Excel) et **figures de reporting**.

> **Public Cible** :
> - **CODIR** (Comité de Direction) : Tableaux de bord et rapports synthétiques.
> - **Équipes Marketing/BI** : Notebooks et analyses détaillées.

---

## **📊 Structure du Projet**
```text
P9/
├── api/
├── dashboard/
├── data/
├── docs/
├── graphiques/
├── models/
├── multi-pages/
├── notebooks/
├── reports/
├── src/
├── Streamlit/
├── tests/
├── ACP.md
├── packages.yml
├── profiles.yml
├── PROJECT_BRIEF.md
├── README.md
└── requirements.txt
```

### **🔹 Données Sources (`data/raw/`)**

[Dépôt GitHub - Données](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/data/raw)

```
data/raw/
├── customers.csv                          # Clients (ID, genre, âge, etc.)
├── products.csv                           # Produits (ID, catégorie, prix, etc.)
└── Transactions.csv                       # Transactions (date, client, produit, montant)
```

### **🔹 Figures de Reporting (`reports/figures/`)**

[Dépôt GitHub - Figures](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/reports/figures)

```
reports/figures/
├── ca_mensuel.png                         # CA mensuel (tendance)
├── evolution_du_ca_mensuel.png            # Évolution du CA (série temporelle)
├── ca_par_categorie.png                   # CA par catégorie de produits
├── btob_btoc_pie.png                      # Répartition B2B/B2C
├── lorenz_ca.png                          # Courbe de Lorenz (concentration)
├── pareto_clients.png                     # Courbe de Pareto clients
├── segmentation_ca_boxplot.png            # Segmentation CA par client
├── fig3_repartition_categorie.png         # Répartition catégories
├── fig9_clients_actifs.png                # Clients actifs
├── fig10_volume_transactions_produits.png # Volume transactions
├── julie_42_scatter_age_ca.png            # Scatter: Âge vs CA
├── julie_43_scatter_freq.png              # Scatter: Fréquence d'achat
├── julie_44_scatter_panier.png            # Scatter: Panier moyen
├── julie_45_boxplot_categ.png             # Boxplot catégories
└── ... (31 fichiers PNG au total)
```
---
## **🔧 Compétences RNCP 37837 Demonstrées**

### **📌 Mapping des Blocs RNCP**
| **Bloc RNCP** | **Compétence** | **Description** | **Preuves** |
|---------------|---------------|----------------|-------------|
| **BC01** | **Structurer et gérer la base de données** | **Pipeline de données** : Transformation des données brutes (`data/raw/`) en données exploitables (`data/processed/`). | [src/data_loader.py](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/src/data_loader.py) |
| **BC02** | **Identifier et collecter les données** | Utilisation des **données de vente Lapage** (CA, panier, fréquence clients). | [data/raw/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/data/raw) |
| **BC02** | **Extraire et agréger** | **Nettoyage et agrégation** : Calcul du CA, panier moyen, concentration des ventes. | [02_Analyses_Marketing.ipynb](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb) |
| **BC02** | **Explorer et pré-traiter** | **Feature Engineering** : Segmentation clients (fréquence, catégories, etc.). | [01_Exploration_EDA.ipynb](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/01_Exploration_EDA.ipynb) |
| **BC02** | **Analyse univariée/multivariée** | **Analyse des tendances** (CA par mois, panier par segment client). | [02_Analyses_Marketing.ipynb](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb) |
| **BC03** | **Solution de visualisation** | **Dashboard Streamlit** : Visualisations interactives (CA, panier, segments clients). | [Dashboard en ligne](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/) |
| **BC03** | **Créer un tableau de bord** | **Dashboard multi-pages** pour le CODIR (performance commerciale, comportements clients). | [Streamlit/app.py](https://github.com/ferialzamoun-afk/P9-lapage-streamlit/blob/main/Streamlit/app.py) |
| **BC04** | **Veille métier/technologique** | **Benchmark des outils** (Streamlit vs Power BI) et **méthodologie documentée**. | [Dépôt GitHub](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies) |
| **BC04** | **Formaliser le cahier des charges** | **Documentation complète** (notebooks, dashboard, exports). | [Dépôt GitHub](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies) |
| **BC04** | **Organiser un projet data** | **Pipeline CI** (tests pytest) et **structure modulaire** (src/, reutilisable/). | [.github/workflows/ci.yml](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml) |
| **BC04** | **Gérer la documentation** | **100% des livrables documentés** (notebooks, scripts, dashboard). | [Dépôt GitHub](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies) |
| **BC05** | **Analyses multivariées** | **Segmentation clients** (fréquence × CA × catégories). | [02_Analyses_Marketing.ipynb](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb) |
| **BC05** | **Tests statistiques** | **Validation des KPI** (cohérence, filtrage multi-critères). | [tests/test_app.py](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/tests/test_app.py) |

---
## **📊 Méthodologie**
*(Blocs RNCP37837BC02, BC03, BC05)*

### **🔹 Pipeline de Données**
1. **Collecte et nettoyage** *(BC02)* :
   - Chargement des données de vente (CA, panier, clients).
   - Nettoyage : gestion des valeurs manquantes, doublons, incohérences.

2. **Analyse exploratoire** *(BC02, BC05)* :
   - **Performance commerciale** : CA mensuel, panier moyen, concentration des ventes.
   - **Comportements clients** : Segmentation (fréquence d’achat, catégories préférées).

3. **Visualisation et Reporting** *(BC03)* :
   - **Dashboard Streamlit** : Vues interactives pour le CODIR.
   - **Exports Excel** : KPI et rapports pour les équipes métiers.
   - **Figures** : Graphiques statiques (PNG) pour les présentations.

4. **Tests et Validation** *(BC04, BC05)* :
   - **Pipeline CI** : Tests automatisés ([pytest](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml)) pour valider la cohérence des KPI.
   - **Validation manuelle** : Vérification des résultats avec les équipes Lapage.

---
## **📈 Résultats et Livrables**
*(Blocs RNCP37837BC03, BC04)*

### **🔹 Dashboard Streamlit**
**URL de production** : [https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/)
**Fonctionnalités** :
- **Page 1 : Performance Commerciale** :
  - CA mensuel/annuel (graphique en aires ou barres).
  - Panier moyen par segment client.
  - Concentration des ventes (top 20% produits/clients).
- **Page 2 : Comportements Clients** :
  - Segmentation des clients (fréquence d’achat, CA moyen).
  - Catégories de produits les plus achetées.
  - Analyse RFM (Récence, Fréquence, Monétaire).
- **Page 3 : Reporting KPI** :
  - Tableau de bord des **KPI clés** (CA, panier, taux de rétention).
  - Export des données en **Excel** (bouton de téléchargement).


*Exemple : Segmentation RFM des clients Lapage.*

### **🔹 Tests & Déploiement**

| Composant | Lien | Description |
| --- | --- | --- |
| **Tests (pytest)** | [ci.yml - Workflow](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml) | Validation automatisée des KPI et cohérence des données |
| **Dashboard Streamlit** | [Code Source](https://github.com/ferialzamoun-afk/P9-lapage-streamlit) | Repository avec application Streamlit déployée |

### **🔹 Notebooks d'Analyse
| Notebook | Objectif | Lien (nbviewer) |
| --- | --- | --- |
| analyse_ventes.ipynb | Analyse des performances commerciales (CA, panier) | [02_Analyses_Marketing.ipynb](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb) |
| analyse_clients.ipynb | Segmentation et comportements clients | [01_Exploration_EDA.ipynb](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/01_Exploration_EDA.ipynb) + [02_Analyses_Marketing.ipynb](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb) |
| tests_statistiques.ipynb | Validation des KPI et tests statistiques | [03_Analyses_Statistiques.ipynb](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/03_Analyses_Statistiques.ipynb) |

📂 Preuves et Documentation
(Bloc RNCP37837BC04 : Piloter un projet data)
| Type | Lien | Description |
| --- | --- | --- |
| Dépôt GitHub | [P9_analyses_ventes_librairies](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies) | Code source, notebooks, dashboard, tests |
| **Données Brutes** | [data/raw/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/data/raw) | customers.csv, products.csv, Transactions.csv |
| Dashboard Streamlit | [Production](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/) | Application web opérationnelle |
| Notebooks | [analyses/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/notebooks/analyses/) | Analyses statistiques (Marketing/BI) |
| **Figures & Graphiques** | [reports/figures/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/reports/figures) | 31 PNG (CA, segmentation, analyses) |
| Fonctions Réutilisables | [réutilisables/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/src/) | Modules Python mutualisés |
| Tests & CI | [Workflow (pytest)](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml) | Validation automatisée des KPI |

🛠 Configuration et Exécution
(Bloc RNCP37837BC04 : Organiser un projet data)
📌 Prérequis

Python 3.11+
pip

📌 Installation
bash
Copier

# Depuis le dossier racine du projet (lapage_project)
pip install -r requirements.txt

📌 Lancement Local
1. Notebooks
cd notebooks
jupyter notebook

→ Ouvre Jupyter dans ton navigateur, puis exécute les notebooks dans l’ordre.
2. Dashboard Streamlit
# Depuis le dossier racine (lapage_project)
streamlit run Streamlit/app.py
→ Le dashboard sera accessible sur http://localhost:8501.
📌 Tests
# Depuis le dossier racine (lapage_project)
python -m pytest tests/test_app.py -v --tb=short
Couverture des tests :

Chargement des données.
Cohérence des KPI de base (CA, panier, fréquence).
Filtrage multi-critères du dashboard.
(Bloc RNCP37837BC02 : Identifier, collecter et analyser les données)
🔹 Points de Vigilance
| Problème | Solution Appliquée | Impact |
| --- | --- | --- |
| Données manquantes | Imputation par moyenne/médiane | Éviter les biais dans les analyses |
| Doublons | Suppression via drop_duplicates() | Données propres pour les KPI |
| Incohérences CA | Vérification des totaux (CA = somme des ventes) | Fiabilité des indicateurs |
| Segments clients | Validation via RFM (Récence, Fréquence, Monétaire) | Pertinence de la segmentation |

🔹 Audits Effectués

✅ Cohérence des KPI : CA = somme(ventes), panier moyen = CA / nombre de transactions.
✅ Filtrage multi-critères : Tests pytest pour valider les filtres du dashboard.
✅ Validation des segments : Vérification que la segmentation RFM couvre 100% des clients.

🔄 Maintenance et Mises à Jour
📌 Recalcul Complet

Placer les nouvelles données dans data/raw/.
Exécuter les notebooks dans l’ordre :
jupyter notebook notebooks/analyse_ventes.ipynb
jupyter notebook notebooks/analyse_clients.ipynb

Les sorties (KPI, figures) seront générées dans reports/.
📌 Enrichissements Possibles

Ajout de données : Intégrer des données externes (ex: tendances marché du livre).
Nouveaux KPI : Taux de rétention, panier moyen par catégorie.
Amélioration UX : Simplification du dashboard (version business).
Automatisation : Planification des mises à jour (ex: mensuelles).

📌 Mapping RNCP 37837

Blocs couverts par ce projet :

✅ BC01 : Structurer et gérer la base de données (pipeline de données, tables nettoyées)
✅ BC02 : Identifier, collecter et analyser les données (nettoyage, EDA, segmentation)
✅ BC03 : Visualiser des données et interpréter des résultats (Dashboard Streamlit, exports KPI)
✅ BC04 : Piloter un projet data (documentation, CI, organisation, veille)
✅ BC05 : Spécialisation Statistiques (analyses multivariées, tests statistiques, RFM)







