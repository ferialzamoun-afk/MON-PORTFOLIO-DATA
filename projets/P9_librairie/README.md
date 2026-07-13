# 📚 **P9 : Analyse des Ventes – Librairie Lapage**
**Projet d'analyse de données et de visualisation pour suivre la performance commerciale, comprendre les comportements clients et fournir des livrables exploitables par le CODIR.**

**📅 Date** : 04/2026
**🏷️ Type** : Analyse Statistique / Dashboard Streamlit / Pipeline CI
**🔗 Liens** :
- [🔗 Dépôt GitHub - Analyses](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies)
- [🌐 Dashboard Streamlit (Production)](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/)
- [📁 Code Source Dashboard](https://github.com/ferialzamoun-afk/P9-lapage-streamlit)
- [📓 Notebooks Jupyter](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/notebooks/analyses/)
- [📊 Exports KPI](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/lapage_project/outputs/)
- [📁 Documentation](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/docs/)
- [✅ Pipeline CI (GitHub Actions)](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/actions)

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

P9/
├── data/                                  # Jeux de données bruts et transformés
│   ├── raw/                               # Données sources (ventes, clients, produits)
│   └── processed/                         # Données nettoyées et agrégées
│
├── notebooks/                             # Analyses statistiques
│   ├── analyse_ventes.ipynb               # Analyse des performances commerciales
│   ├── analyse_clients.ipynb              # Segmentation et comportements clients
│   └── tests_statistiques.ipynb           # Tests et validations statistiques
│
├── src/                                   # Modules utilitaires
│   ├── kpi_calculator.py                  # Calcul des KPI (CA, panier moyen, etc.)
│   ├── data_loader.py                     # Chargement et préparation des données
│   └── export_utils.py                    # Export des KPI et figures
│
├── reutilisable (toutes phases)/          # Fonctions mutualisées
│   ├── data_loading.py                    # Fonctions de chargement génériques
│   ├── analysis_utils.py                  # Fonctions d’analyse réutilisables
│   └── visualization_utils.py             # Fonctions de visualisation (Matplotlib, Plotly)
│
├── Streamlit/                             # Application web
│   ├── app.py                             # Point d’entrée du dashboard
│   ├── pages/                             # Pages additionnelles (ex: analyse_clients.py)
│   └── assets/                            # Ressources (CSS, images)
│
├── reports/                               # Livrables
│   ├── figures/                           # Graphiques exportés (PNG, SVG)
│   ├── exports/                           # Exports Excel (KPI, rapports)
│   └── Presentation/                      # Présentations (PowerPoint, PDF)
│
├── tests/                                # Tests unitaires
│   └── test_app.py                        # Tests pour le dashboard Streamlit
│
├── requirements.txt                       # Dépendances Python
└── .github/workflows/
└── ci.yml                            # Pipeline CI (pytest)
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
| **BC03** | **Créer un tableau de bord** | **Dashboard multi-pages** pour le CODIR (performance commerciale, comportements clients). | [Streamlit/app.py](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/dashboard/) |
| **BC03** | **Reporting des tendances** | **Exports KPI** (Excel) et **figures de reporting** (PNG). | [outputs/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/lapage_project/outputs/) |
| **BC04** | **Veille métier/technologique** | **Benchmark des outils** (Streamlit vs Power BI) et **méthodologie documentée**. | [README.md](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/README.md) |
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
   - **Pipeline CI** : Tests automatisés (pytest) pour valider la cohérence des KPI.
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

**Captures d’écran** :
*(À ajouter si disponibles)*
```markdown
![Dashboard - Performance Commerciale](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/raw/main/lapage_project/outputs/dashboard_performance.png)
*Exemple : Évolution du CA mensuel et panier moyen.*

![Dashboard - Segmentation Clients](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/raw/main/lapage_project/outputs/dashboard_clients.png)
*Exemple : Segmentation RFM des clients Lapage.*

🔹 Exports KPI (Excel)

| Fichier | Description | Lien |
| --- | --- | --- |
| kpi_ventes.xlsx | CA, panier moyen, concentration des ventes | [lapage_project/outputs/kpi_ventes.xlsx](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/raw/main/lapage_project/outputs/kpi_ventes.xlsx) |
| kpi_clients.xlsx | Segmentation clients, fréquence d'achat | [lapage_project/outputs/kpi_clients.xlsx](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/raw/main/lapage_project/outputs/kpi_clients.xlsx) |
| kpi_produits.xlsx | Performance par catégorie de produits | [lapage_project/outputs/kpi_produits.xlsx](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/raw/main/lapage_project/outputs/kpi_produits.xlsx) |

🔹 Notebooks d’Analyse
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
| Dashboard Streamlit | [Production](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/) | Application web opérationnelle |
| Notebooks | [analyses/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/notebooks/analyses/) | Analyses statistiques (Marketing/BI) |
| Fonctions Réutilisables | [réutilisables/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/src/) | Modules Python mutualisés |
| Exports KPI | [outputs/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/lapage_project/outputs/) | Fichiers Excel (CA, clients, produits) |
| Figures | [outputs/](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/lapage_project/outputs/) | Graphiques statiques (PNG) |
| Pipeline CI | [GitHub Actions](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/actions) | Tests pytest automatisés |
| Tests | [tests/test_app.py](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/tests/test_app.py) | Suite de tests (100% des KPI validés) |

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







