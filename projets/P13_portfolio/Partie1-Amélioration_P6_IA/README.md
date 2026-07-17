# 🍷 **P6 Amélioré : Optimisation de la Gestion des Données – Bottleneck Wine Shop**
**Amélioration du livrable P6 avec IA critique, documentation structurée et preuves détaillées pour une restitution métier plus lisible.**

> **🔹 Reproductible**   **📊 Traçable** | **🤖 IA Documentée** | **⚡ Optimisé (-68% cells, -76% temps)**

**📅 Date** : Juillet 2026
**🏷️ Type** : Analyse Exploratoire / Data Cleaning / KPI Business / IA Assistée
**🔗 Liens** :
| Ressource | Lien |
|---|---|
| 🔗 Portfolio P13 | [Accéder](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/) |
| 📓 Notebook Principal | [Accéder](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amélioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb) |
| 📓 Notebook amélioré | [Accéder](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amélioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb) |
| 📁 Cahier des Charges | [Accéder](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amélioration_P6_IA/01_cahier_des_charges_P13_partie_1.md) |
| 📁 Veille Technologique | [Accéder](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amélioration_P6_IA/02_veille_technologique_P13_partie_1.md) |
| 📁 Journal IA | [Accéder](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amélioration_P6_IA/03_journal_ia_P13_partie_1.md) |
| 📁 Synthèse Finale | [Accéder](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amélioration_P6_IA/06_synthese_finale_P13_partie_1.md) |
| 📊 Dataviz (13 graphiques) | [Accéder](https://ferialzamoun-afk/P13/Partie_1/P6_ameliore_IA/output/dataviz/) |
| 🖼️ Captures Portfolio | [Accéder](https://ferialzamoun-afk/P13/Partie_1/P6_ameliore_IA/output/captures/) |

**Preuves détaillées et restitution métier** :
| Preuve | Accès |
|---|---|
| Avant : Notebook initial | [Voir le PDF](https://ferialzamoun-afk/P13/Partie_1/P6_initial/Template-Notebook-Bottleneck.pdf) |
| Après : Notebook amélioré | [Voir](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amélioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb) |
| Avant : Synthèse initiale | Non conservée dans le dépôt public |
| Après : Synthèse finale enrichie | [Voir](https://ferialzamoun-afk/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Amélioration_P6_IA/06_synthese_finale_P13_partie_1.md) |
| Avant : Visuels HTML | [Voir](https://ferialzamoun-afk/P6/images/) |
| Après : Visuels PNG | [Voir](https://ferialzamoun-afk/P13/Partie_1/P6_ameliore_IA/output/dataviz/) |
| Dashboard KPI pour le CODIR | [Voir](https://ferialzamoun-afk/P13/Partie_1/P6_ameliore_IA/output/captures/) |

---

## **🎯 Contexte et Objectifs**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

> **Contexte** :
> *"Projet réalisé pour **Bottleneck**, une boutique de vins en ligne avec un **ERP physique**, confrontée à des **incohérences entre 3 sources de données** (ERP, Web, Liaison). Ces incohérences entraînent un **manque de visibilité commerciale** et une **difficulté à prendre des décisions éclairées**."*

> **Objectifs Métier** :
> 1. **Réconcilier les données** : Fusionner les 3 sources (ERP, Web, Liaison) pour obtenir une **vue unifiée**.
> 2. **Identifier les anomalies** : Détecter les incohérences (prix invalides, marges négatives, ruptures de stock).
> 3. **Fournir des KPI au CODIR** :
>    - Chiffre d’affaires consolidé.
>    - Analyse Pareto (80% du CA).
>    - Recommandations pour optimiser les stocks et les marges.
> 4. **Préparer une restitution métier exploitable** :
>    - Réduire la taille du notebook (**-68% de cells**).
>    - Optimiser le temps d’exécution (**-76%**).
>    - **Documenter chaque étape** (IA, contrôles qualité, décisions).
>    - Fournir un **dashboard KPI** clair pour la lecture CODIR.
>    - Montrer la trace **avant / après** entre le livrable initial et la version améliorée.

> **Approche P13** :
> *"**Pandas pragmatique** (court terme, J+30) avec **Data Contracts formalisés** en vue d’une migration vers **Great Expectations v19+** (moyen terme)."*

---

## **📊 Structure du Projet**
| Élément | Contenu | Rôle |
|---|---|---|
| `README.md` | Ce fichier | Point d’entrée du livrable |
| `requirements.txt` | Dépendances Python | Reproductibilité de l’environnement |
| `notebooks/bottleneck_analyse_ameliore_final.ipynb` | Notebook final | Analyse principale, 49 cellules, exécution ~1:11 |
| `src/quality_checks.py` | Script Python | 18 contrôles de qualité des données |
| `src/stock_cleaning.py` | Script Python | Correction des anomalies de stock |
| `src/data_merging.py` | Script Python | Rapprochement ERP / Web / Liaison |
| `src/eda_analysis.py` | Script Python | Analyses exploratoires, Pareto, corrélations |
| `src/kpi_analysis.py` | Script Python | Calcul des KPI métier (CA, marges, rotation) |
| `docs/01_cahier_des_charges_P13_partie_1.md` | Documentation | Cahier des charges complet |
| `docs/02_veille_technologique_P13_partie_1.md` | Documentation | Benchmark Pandas vs GE vs Soda |
| `docs/03_journal_ia_P13_partie_1.md` | Documentation | 26 prompts IA documentés |
| `docs/04_plan_projet_P13_partie_1.md` | Documentation | Backlog, kanban, planning |
| `docs/05_matrice_indicateurs_P13_partie_1.md` | Documentation | Matrice des indicateurs |
| `docs/06_synthese_finale_P13_partie_1.md` | Documentation | Synthèse des résultats et recommandations |
| `docs/07_checklist_publication_github.md` | Documentation | Checklist de déploiement |
| `docs/13_great_expectations_strategy.md` | Documentation | Stratégie de migration vers GE v19+ |
| `output/dataviz/` | Graphiques HTML | 13 graphiques Plotly pour la restitution |
| `output/captures/` | Captures PNG | 6 à 8 captures portfolio |
---

## **🚀 Quickstart (Démarrage Rapide)**
*(Bloc RNCP37837BC04 : Organiser un projet data)*

### **📌 Prérequis**
- **Python 3.12.2+** *(vérification automatique dans le notebook)*
- **Virtual Environment** *(recommandé)*

### **📌 Installation**
```bash
# 1. Cloner le dépôt
git clone https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA.git
cd P6_ameliore_IA

# 2. Créer et activer l'environnement virtuel
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows (PowerShell)
source .venv/bin/activate  # Mac/Linux

# 3. Installer les dépendances
pip install -r requirements.txt
```

### **📌 Exécuter le Notebook**
```bash
# Ouvrir Jupyter Notebook
jupyter notebook notebooks/bottleneck_analyse_ameliore_final.ipynb

# OU exécuter directement (VS Code / Jupyter Lab)
# → Appuyer sur Shift+Enter pour chaque cellule
```
### **📌 Résultats Générés**

✅ Checkpoints à chaque phase (M00, Phase I, Phase II, Final).
✅ 13 graphiques Plotly dans output/dataviz/ (CA, Pareto, anomalies, stocks, corrélations).
✅ Rapport de qualité : 18 contrôles + 7 Data Contracts validés.
✅ Temps total : ~1 minute 11 secondes (vs ~5 min initialement).

### **📊 Résultats Clés**
(Blocs RNCP37837BC02, BC03, BC05)
| Bloc | Élément | Résultat | Preuve |
| --- | --- | --- | --- |
| Phase I | Données chargées | 825 (ERP) + 1 513 (Web) + 825 (Liaison) | data_merging.py |
| Phase I | Contrôles qualité | 18 points validés (11 OK, 4 à vérifier, 2 à documenter, 1 corrigé) | quality_checks.py |
| Phase I | Stocks corrigés | 2 exceptions (stock < 0) identifiées et tracées | stock_cleaning.py |
| Phase I | Rapprochement ERP/Web | 714 / 1 513 matches (47.2% → anomalies à investiguer) | data_merging.py |
| Phase II | CA total | 143 680 EUR/mois (octobre 2026) | kpi_analysis.py |
| Phase II | Produits avec CA | 689 | eda_analysis.py |
| Phase II | Pareto 80% | Rang 435 | courbe_pareto_80_20.html |
| Phase II | Marge moyenne | 47.32% | anomalies_prix_et_marges.html |
| Phase II | Stock / Rotation | 2.98 mois (moyenne) | distribution_stocks.html |
| Phase II | Anomalies détectées | 10 (3 prix invalides, 7 marges négatives) | anomalies_prix_et_marges.html |
| Dataviz | Chiffre d’affaires par catégorie | Graphique de synthèse | HTML |
| Dataviz | Courbe Pareto 80/20 | Visualisation des ventes concentrées | HTML |
| Dataviz | Anomalies prix et marges | Contrôle des valeurs aberrantes | HTML |
| Dataviz | Distribution des stocks | Répartition des niveaux de stock | HTML |
| Dataviz | Rotation mensuelle | Suivi de rotation | HTML |
| Dataviz | Corrélations quantitatives | Relations entre variables | HTML |
| Dataviz | Autres visuels | 7 graphiques supplémentaires | output/dataviz/ |

### **🔧 Méthodologie et Choix Technologiques**
(Blocs RNCP37837BC02, BC04)
📌 Contrôle Qualité : Pourquoi Pandas ?
(Bloc RNCP37837BC04 : Piloter un projet data)
| Critère | Pandas | Great Expectations | Soda Core |
| --- | --- | --- | --- |
| Temps d’implémentation | ⚡ Rapide (J+30 OK) | 🐢 Courbe d’apprentissage raide | 🐢 Dépendance externe |
| Reproductibilité | ✅ Native | ✅ OK | ⚠️ Config YAML complexe |
| Sobriété / Dépendances | ✅ Minimal | ⚠️ Lourd | ⚠️ Lourd |
| Audit Trail | ✅ Logs Pandas | ✅ Full | ⚠️ Limité |
| RGPD / Chemins | ✅ OK | ✅ OK | ⚠️ À vérifier |
Décision :

Court terme (J+30) : Pandas pragmatique + Data Contracts formalisés.
Moyen terme : Migration vers Great Expectations v19+ (voir roadmap).

### **📌 Reproductibilité & RGPD**
(Bloc RNCP37837BC04 : Gérer la documentation et formaliser les processus)

✅ Chemins relatifs robustes (../../../P6_initial/data/) → Portabilité garantie.
✅ Zéro données nominatives embarquées → Conformité RGPD.
✅ Vérification prérequis automatique (Cellule 1 du notebook).
✅ Timekeeper pour traçabilité des performances.

### **📌 Traçabilité IA**
(Bloc RNCP37837BC04 : Adapter sa posture de professionnel)

📌 26 prompts Claude documentés (essais 1-13).
📌 Journal IA complet : Objectif → Prompt → Résultat → Décision humaine → Limitations.
📌 Chaque décision majeure justifiée : Contraintes appliquées, alternatives testées.
→ Voir : Journal IA

### **📈 Améliorations Apportées au P6 Initial**
(Bloc RNCP37837BC04 : Organiser un projet data)
| Dimension | P6 Initial | P6 Amélioré | Gain |
| --- | --- | --- | --- |
| Cellules notebook | 148 | 49 | -68% |
| Temps d’exécution | ~5 min | 1:11 min | -76% |
| Code cells | 105 | 39 | -63% |
| Markdown cells | 43 | 8 | -81% |
| Erreurs/warnings | 1 major | 0 | ✅ |
| Contrôles qualité | Implicites | 18 explicites | ✅ |
| Data Contracts | 0 | 7 formalisés | ✅ |
| Checkpoints | 0 | 4 internes | ✅ |
| Documentation IA | 0 | 26 prompts tracés | ✅ |
| Reproductibilité | Chemins locaux | Chemins relatifs | ✅ |

### **📚 Documentation Complète**
(Bloc RNCP37837BC04 : Piloter un projet data)

Tous les 10 critères mission P13 Partie 1 sont documentés et tracés :
| Critère | Document | Lien |
| --- | --- | --- |
| Améliorer le livrable | Synthèse avant/après | [06_synthese_finale](docs/06_synthese_finale_P13_partie_1.md) |
| IA critique & documentée | Journal IA (26 prompts) | [03_journal_ia](docs/03_journal_ia_P13_partie_1.md) |
| Tester plusieurs options | Benchmark outils (Pandas/GE/Soda) | [02_veille_technologique](docs/02_veille_technologique_P13_partie_1.md) |
| Critères explicites | Tableau comparaison + méthodologie | [Notebook, Cellule 2](https://nbviewer.org/github/ferialzamoun-afk/P6_ameliore_IA/blob/main/notebooks/bottleneck_analyse_ameliore_final.ipynb#2.-M%C3%A9thodologie) |
| Justifier les choix | Chaque cellule commence par "Pourquoi ?" | [Notebook complet](https://nbviewer.org/github/ferialzamoun-afk/P6_ameliore_IA/blob/main/notebooks/bottleneck_analyse_ameliore_final.ipynb) |
| Identifier les besoins métier | Cahier des charges complet | [01_cahier_des_charges](docs/01_cahier_des_charges_P13_partie_1.md) |
| Cahier des charges | Document complet (CDC) | [01_cahier_des_charges](docs/01_cahier_des_charges_P13_partie_1.md) |
| Organiser le projet | Backlog, kanban, planning | [04_plan_projet](docs/04_plan_projet_P13_partie_1.md) |
| Outils de gestion | GitHub Projects Kanban | [Captures disponibles](output/captures/) |
| Intégrer les contraintes | 5 types documentés (délai, RGPD, budget, sobriété, conformité) | [04_plan_projet](docs/04_plan_projet_P13_partie_1.md) |

### **🛠️ Pour les Développeurs / Contributeurs**
(Bloc RNCP37837BC04 : Gérer la documentation et formaliser les processus)
📌 Environnement Local
# Setup
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate  # Mac/Linux
pip install -r requirements.txt

# Modifier / Tester
jupyter notebook
# ... éditer & exécuter les cellules

# Lint & Format (optionnel)
ruff check src/

### **📌 Modules Python**
| Module | Rôle | Lien |
| --- | --- | --- |
| quality_checks.py | 18 contrôles de données (structure, valeurs, doublons) | [Lien](src/quality_checks.py) |
| stock_cleaning.py | Corrections tracées des anomalies de stock | [Lien](src/stock_cleaning.py) |
| data_merging.py | Rapprochement ERP/Web/Liaison avec logging | [Lien](src/data_merging.py) |
| eda_analysis.py | Analyses exploratoires (Pareto, corrélations) | [Lien](src/eda_analysis.py) |
| kpi_analysis.py | Calcul des KPI métier (CA, marges, rotation) | [Lien](src/kpi_analysis.py) |

### **⚠️ Limites et Prudences**
(Bloc RNCP37837BC05 : Spécialisation Statistiques)
| Limite | Impact | Recommandation | Preuve |
| --- | --- | --- | --- |
| 1 mois de données (octobre 2026) | Snapshot, pas de tendance | Confirmer sur multi-mois | [06_synthese_finale](docs/06_synthese_finale_P13_partie_1.md) |
| Corrélations ≠ causalité | Risque de faux signaux | Utiliser comme aide à la décision, pas comme preuve | [Notebook, Cellule 7](notebooks/bottleneck_analyse_ameliore_final.ipynb) |
| Outliers statistiques | Modèle IQR | Valider avec l’équipe métier (prix premium légitimes ?) | [anomalies_prix_et_marges.html](output/dataviz/anomalies_prix_et_marges.html) |
| Stock/Liaison manuels | Risque de désynchronisation | Investiguer 799 références Web sans match ERP | [data_merging.py](src/data_merging.py) |
| Pas d’historique | Données point-in-time | Intégrer l’historique pour analyser les tendances | [06_synthese_finale](docs/06_synthese_finale_P13_partie_1.md) |

### **📞 Questions Fréquentes (FAQ)**
Q : Puis-je relancer le notebook sur mes données ?
✅ Oui ! Remplace data/erp.xlsx, data/web.xlsx, data/liaison.xlsx avec tes fichiers (même format attendu).
Q : Pourquoi Pandas et pas Great Expectations d’emblée ?
🔧 Délai court terme (J+30) + pragmatisme. Great Expectations v19+ est planifiée pour Q1 2027 (voir roadmap).
Q : Les résultats sont-ils fiables ?
⚠️ Snapshot 1 mois (octobre 2026). Valide les anomalies avec les équipes métier. Les limites sont documentées dans la synthèse finale.
Q : Comment contribuer ?
📌 Voir CONTRIBUTING.md (si applicable).

### **🔧 Compétences RNCP 37837 Demonstrées**
### **📌 Mapping des Blocs RNCP**
| Bloc RNCP | Compétence | Description | Preuves |
| --- | --- | --- | --- |
| BC01 | Structurer et gérer la base de données | Rapprochement de 3 sources (ERP, Web, Liaison) en une base unifiée. | [data_merging.py](src/data_merging.py) |
| BC01 | Gérer une base de données | Contrôles qualité (18 points) et Data Contracts (7 formalisés). | [quality_checks.py](src/quality_checks.py) |
| BC02 | Identifier et collecter les données | Utilisation des 3 sources Bottleneck (ERP, Web, Liaison). | [Notebook, Cellule 1](notebooks/bottleneck_analyse_ameliore_final.ipynb) |
| BC02 | Extraire et agréger | Nettoyage (stocks, prix) et rapprochement des données. | [stock_cleaning.py](src/stock_cleaning.py) + [data_merging.py](src/data_merging.py) |
| BC02 | Explorer et pré-traiter | EDA (Pareto, corrélations, anomalies). | [eda_analysis.py](src/eda_analysis.py) |
| BC02 | Analyse univariée/multivariée | Analyse Pareto (80% du CA sur 435 produits). | [courbe_pareto_80_20.html](output/dataviz/courbe_pareto_80_20.html) |
| BC03 | Solution de visualisation | 13 graphiques Plotly (CA, Pareto, anomalies, stocks). | [output/dataviz/](output/dataviz/) |
| BC03 | Créer un tableau de bord | Dashboard KPI Streamlit pour le CODIR, déjà illustré par la capture de restitution. | [Capture dashboard](output/captures/05_kpi_dashboard_phase2.png) |
| BC03 | Reporting des tendances | Exports HTML (Plotly) et synthèse écrite. | [output/dataviz/](output/dataviz/) + [06_synthese_finale](docs/06_synthese_finale_P13_partie_1.md) |
| BC04 | Veille métier/technologique | Benchmark Pandas vs GE vs Soda + roadmap migration. | [02_veille_technologique](docs/02_veille_technologique_P13_partie_1.md) |
| BC04 | Formaliser le cahier des charges | Cahier des charges complet (objectifs, contraintes, livrables). | [01_cahier_des_charges](docs/01_cahier_des_charges_P13_partie_1.md) |
| BC04 | Organiser un projet data | Backlog, kanban, planning (GitHub Projects). | [04_plan_projet](docs/04_plan_projet_P13_partie_1.md) + [captures](output/captures/) |
| BC04 | Gérer la documentation | 8 docs + 26 prompts IA + 13 graphiques documentés. | [docs/](docs/) |
| BC04 | Adapter sa posture | Journal IA (décisions humaines + limitations). | [03_journal_ia](docs/03_journal_ia_P13_partie_1.md) |
| BC05 | Analyses multivariées | Analyse Pareto + corrélations (prix, marges, stocks). | [eda_analysis.py](src/eda_analysis.py) |
| BC05 | Tests statistiques | Validation des KPI (cohérence, outliers). | [kpi_analysis.py](src/kpi_analysis.py) |


🎯 Mapping RNCP 37837

Blocs couverts par ce projet :

✅ BC01 : Structurer et gérer la base de données (rapprochement 3 sources, Data Contracts)
✅ BC02 : Identifier, collecter et analyser les données (nettoyage, EDA, KPI)
✅ BC03 : Visualiser des données et interpréter des résultats (13 graphiques Plotly, synthèse)
✅ BC04 : Piloter un projet data (documentation, CI, organisation, veille, posture consultante)
✅ BC05 : Spécialisation Statistiques (Pareto, corrélations, tests statistiques)