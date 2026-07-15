# 🍷 **P6 Amélioré : Optimisation de la Gestion des Données – Bottleneck Wine Shop**
**Amélioration du livrable P6 avec IA critique, documentation complète et traçabilité totale pour une analyse décisionnelle optimisée.**

> **🔹 Reproductible**   **📊 Traçable** | **🤖 IA Documentée** | **⚡ Optimisé (-68% cells, -76% temps)**

**📅 Date** : Juillet 2026
**🏷️ Type** : Analyse Exploratoire / Data Cleaning / KPI Business / IA Assistée
**🔗 Liens** :
- [🔗 Dépôt GitHub](https://github.com/ferialzamoun-afk/P6_ameliore_IA)
- [📓 Notebook Principal (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P6_ameliore_IA/blob/main/notebooks/bottleneck_analyse_ameliore_final.ipynb)
- [📓 Notebook Production](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/notebooks/bottleneck_analyse_ameliore_final.ipynb)
- [📁 Cahier des Charges](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/01_cahier_des_charges_P13_partie_1.md)
- [📁 Veille Technologique](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/02_veille_technologique_P13_partie_1.md)
- [📁 Journal IA](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/03_journal_ia_P13_partie_1.md)
- [📁 Synthèse Finale](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/06_synthese_finale_P13_partie_1.md)
- [📊 Dataviz (13 graphiques)](https://github.com/ferialzamoun-afk/P6_ameliore_IA/tree/main/output/dataviz)
- [🖼️ Captures Portfolio](https://github.com/ferialzamoun-afk/P6_ameliore_IA/tree/main/output/captures)

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
> 4. **Améliorer le livrable initial** :
>    - Réduire la taille du notebook (**-68% de cells**).
>    - Optimiser le temps d’exécution (**-76%**).
>    - **Documenter chaque étape** (IA, contrôles qualité, décisions).

> **Approche P13** :
> *"**Pandas pragmatique** (court terme, J+30) avec **Data Contracts formalisés** en vue d’une migration vers **Great Expectations v19+** (moyen terme)."*

---

## **📊 Structure du Projet**
```text
P6/
├── .github/
├── dashboard_deploy/
├── data/
├── images/
├── notebooks/
├── output/
├── png/
├── .gitignore
├── DASHBOARD_README.md
├── DOCUMENT_EXECUTIF.md
├── main.py
├── PHASE2_README.md
├── README.md
├── requirements.txt
├── run_analysis.py
├── streamlit_app.py
├── STREAMLIT_README.md
└── SYNTHESE_GLOBALE.md
```
---

## **🚀 Quickstart (Démarrage Rapide)**
*(Bloc RNCP37837BC04 : Organiser un projet data)*

### **📌 Prérequis**
- **Python 3.12.2+** *(vérification automatique dans le notebook)*
- **Virtual Environment** *(recommandé)*

### **📌 Installation**
```bash
# 1. Cloner le dépôt
git clone https://github.com/ferialzamoun-afk/P6_ameliore_IA.git
cd P6_ameliore_IA

# 2. Créer et activer l'environnement virtuel
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows (PowerShell)
source .venv/bin/activate  # Mac/Linux

# 3. Installer les dépendances
pip install -r requirements.txt

📌 Exécuter le Notebook
# Ouvrir Jupyter Notebook
jupyter notebook notebooks/bottleneck_analyse_ameliore_final.ipynb

# OU exécuter directement (VS Code / Jupyter Lab)
# → Appuyer sur Shift+Enter pour chaque cellule
📌 Résultats Générés

✅ Checkpoints à chaque phase (M00, Phase I, Phase II, Final).
✅ 13 graphiques Plotly dans output/dataviz/ (CA, Pareto, anomalies, stocks, corrélations).
✅ Rapport de qualité : 18 contrôles + 7 Data Contracts validés.
✅ Temps total : ~1 minute 11 secondes (vs ~5 min initialement).

📊 Résultats Clés
(Blocs RNCP37837BC02, BC03, BC05)
🔹 Phase I : Préparation & Qualité des Données
| Étape | Résultat | Preuve |
| --- | --- | --- |
| Données chargées | 825 (ERP) + 1 513 (Web) + 825 (Liaison) | [data_merging.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/data_merging.py) |
| Contrôles qualité | 18 points validés (11 OK, 4 à vérifier, 2 à documenter, 1 corrigé) | [quality_checks.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/quality_checks.py) |
| Stocks corrigés | 2 exceptions (stock < 0) identifiées et tracées | [stock_cleaning.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/stock_cleaning.py) |
| Rapprochement ERP/Web | 714 / 1 513 matches (47.2% → anomalies à investiguer) | [data_merging.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/data_merging.py) |
🔹 Phase II : KPI Business
| KPI | Valeur | Interprétation | Preuve |
| --- | --- | --- | --- |
| CA total | 143 680 EUR/mois (octobre 2026) | ✅ Revenue consolidée | [kpi_analysis.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/kpi_analysis.py) |
| Produits avec CA | 689 | ✅ Diversité du catalogue | [eda_analysis.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/eda_analysis.py) |
| Pareto 80% | Rang 435 | ⚠️ Catalogue large, pas fortement concentré | [courbe_pareto_80_20.html](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/courbe_pareto_80_20.html) |
| Marge moyenne | 47.32% | ✅ Saine | [anomalies_prix_et_marges.html](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/anomalies_prix_et_marges.html) |
| Stock / Rotation | 2.98 mois (moyenne) | ⚠️ À optimiser (92 ruptures de stock détectées) | [distribution_stocks.html](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/distribution_stocks.html) |
| Anomalies détectées | 10 (3 prix invalides, 7 marges négatives) | 🚨 À investiguer | [anomalies_prix_et_marges.html](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/anomalies_prix_et_marges.html) |
🔹 Dataviz Générées (13 fichiers Plotly)
(Bloc RNCP37837BC03 : Visualiser des données et interpréter des résultats)
- [📊 Chiffre d’affaires par catégorie](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/chiffre_affaires_par_categorie.html)
- [📈 Courbe Pareto 80/20](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/courbe_pareto_80_20.html)
- [⚠️ Anomalies prix et marges](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/anomalies_prix_et_marges.html)
- [📦 Distribution des stocks](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/distribution_stocks.html)
- [🔄 Rotation mensuelle](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/rotation_mensuelle.html)
- [🔗 Corrélations quantitatives](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/correlations_quantitatives.html)
- *(+ 7 autres graphiques disponibles dans [output/dataviz/](https://github.com/ferialzamoun-afk/P6_ameliore_IA/tree/main/output/dataviz))*

🔧 Méthodologie et Choix Technologiques
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
📌 Reproductibilité & RGPD
(Bloc RNCP37837BC04 : Gérer la documentation et formaliser les processus)

✅ Chemins relatifs robustes (../../../P6_initial/data/) → Portabilité garantie.
✅ Zéro données nominatives embarquées → Conformité RGPD.
✅ Vérification prérequis automatique (Cellule 1 du notebook).
✅ Timekeeper pour traçabilité des performances.

📌 Traçabilité IA
(Bloc RNCP37837BC04 : Adapter sa posture de professionnel)

📌 26 prompts Claude documentés (essais 1-13).
📌 Journal IA complet : Objectif → Prompt → Résultat → Décision humaine → Limitations.
📌 Chaque décision majeure justifiée : Contraintes appliquées, alternatives testées.
→ Voir : Journal IA
📈 Améliorations Apportées au P6 Initial
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

📚 Documentation Complète
(Bloc RNCP37837BC04 : Piloter un projet data)

Tous les 10 critères mission P13 Partie 1 sont documentés et tracés :
| Critère | Document | Lien |
| --- | --- | --- |
| Améliorer le livrable | Synthèse avant/après | [06_synthese_finale](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/06_synthese_finale_P13_partie_1.md) |
| IA critique & documentée | Journal IA (26 prompts) | [03_journal_ia](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/03_journal_ia_P13_partie_1.md) |
| Tester plusieurs options | Benchmark outils (Pandas/GE/Soda) | [02_veille_technologique](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/02_veille_technologique_P13_partie_1.md) |
| Critères explicites | Tableau comparaison + méthodologie | [Notebook, Cellule 2](https://nbviewer.org/github/ferialzamoun-afk/P6_ameliore_IA/blob/main/notebooks/bottleneck_analyse_ameliore_final.ipynb#2.-M%C3%A9thodologie) |
| Justifier les choix | Chaque cellule commence par "Pourquoi ?" | [Notebook complet](https://nbviewer.org/github/ferialzamoun-afk/P6_ameliore_IA/blob/main/notebooks/bottleneck_analyse_ameliore_final.ipynb) |
| Identifier les besoins métier | Cahier des charges complet | [01_cahier_des_charges](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/01_cahier_des_charges_P13_partie_1.md) |
| Cahier des charges | Document complet (CDC) | [01_cahier_des_charges](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/01_cahier_des_charges_P13_partie_1.md) |
| Organiser le projet | Backlog, kanban, planning | [04_plan_projet](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/04_plan_projet_P13_partie_1.md) |
| Outils de gestion | GitHub Projects Kanban | [Captures disponibles](https://github.com/ferialzamoun-afk/P6_ameliore_IA/tree/main/output/captures) |
| Intégrer les contraintes | 5 types documentés (délai, RGPD, budget, sobriété, conformité) | [04_plan_projet](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/04_plan_projet_P13_partie_1.md) |

🛠️ Pour les Développeurs / Contributeurs
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

📌 Modules Python
| Module | Rôle | Lien |
| --- | --- | --- |
| quality_checks.py | 18 contrôles de données (structure, valeurs, doublons) | [Lien](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/quality_checks.py) |
| stock_cleaning.py | Corrections tracées des anomalies de stock | [Lien](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/stock_cleaning.py) |
| data_merging.py | Rapprochement ERP/Web/Liaison avec logging | [Lien](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/data_merging.py) |
| eda_analysis.py | Analyses exploratoires (Pareto, corrélations) | [Lien](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/eda_analysis.py) |
| kpi_analysis.py | Calcul des KPI métier (CA, marges, rotation) | [Lien](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/kpi_analysis.py) |

⚠️ Limites et Prudences
(Bloc RNCP37837BC05 : Spécialisation Statistiques)
| Limite | Impact | Recommandation | Preuve |
| --- | --- | --- | --- |
| 1 mois de données (octobre 2026) | Snapshot, pas de tendance | Confirmer sur multi-mois | [06_synthese_finale](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/06_synthese_finale_P13_partie_1.md) |
| Corrélations ≠ causalité | Risque de faux signaux | Utiliser comme aide à la décision, pas comme preuve | [Notebook, Cellule 7](https://nbviewer.org/github/ferialzamoun-afk/P6_ameliore_IA/blob/main/notebooks/bottleneck_analyse_ameliore_final.ipynb#7.-Audit) |
| Outliers statistiques | Modèle IQR | Valider avec l’équipe métier (prix premium légitimes ?) | [anomalies_prix_et_marges.html](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/anomalies_prix_et_marges.html) |
| Stock/Liaison manuels | Risque de désynchronisation | Investiguer 799 références Web sans match ERP | [data_merging.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/data_merging.py) |
| Pas d’historique | Données point-in-time | Intégrer l’historique pour analyser les tendances | [06_synthese_finale](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/06_synthese_finale_P13_partie_1.md) |

📞 Questions Fréquentes (FAQ)
Q : Puis-je relancer le notebook sur mes données ?
✅ Oui ! Remplace data/erp.xlsx, data/web.xlsx, data/liaison.xlsx avec tes fichiers (même format attendu).
Q : Pourquoi Pandas et pas Great Expectations d’emblée ?
🔧 Délai court terme (J+30) + pragmatisme. Great Expectations v19+ est planifiée pour Q1 2027 (voir roadmap).
Q : Les résultats sont-ils fiables ?
⚠️ Snapshot 1 mois (octobre 2026). Valide les anomalies avec les équipes métier. Les limites sont documentées dans la synthèse finale.
Q : Comment contribuer ?
📌 Voir CONTRIBUTING.md (si applicable).

🔧 Compétences RNCP 37837 Demonstrées
📌 Mapping des Blocs RNCP
| Bloc RNCP | Compétence | Description | Preuves |
| --- | --- | --- | --- |
| BC01 | Structurer et gérer la base de données | Rapprochement de 3 sources (ERP, Web, Liaison) en une base unifiée. | [data_merging.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/data_merging.py) |
| BC01 | Gérer une base de données | Contrôles qualité (18 points) et Data Contracts (7 formalisés). | [quality_checks.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/quality_checks.py) |
| BC02 | Identifier et collecter les données | Utilisation des 3 sources Bottleneck (ERP, Web, Liaison). | [Notebook, Cellule 1](https://nbviewer.org/github/ferialzamoun-afk/P6_ameliore_IA/blob/main/notebooks/bottleneck_analyse_ameliore_final.ipynb#1.-Chargement-des-donn%C3%A9es) |
| BC02 | Extraire et agréger | Nettoyage (stocks, prix) et rapprochement des données. | [stock_cleaning.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/stock_cleaning.py) + [data_merging.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/data_merging.py) |
| BC02 | Explorer et pré-traiter | EDA (Pareto, corrélations, anomalies). | [eda_analysis.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/eda_analysis.py) |
| BC02 | Analyse univariée/multivariée | Analyse Pareto (80% du CA sur 435 produits). | [courbe_pareto_80_20.html](https://github.com/ferialzamoun-afk/P6_ameliore_IA/raw/main/output/dataviz/courbe_pareto_80_20.html) |
| BC03 | Solution de visualisation | 13 graphiques Plotly (CA, Pareto, anomalies, stocks). | [output/dataviz/](https://github.com/ferialzamoun-afk/P6_ameliore_IA/tree/main/output/dataviz) |
| BC03 | Créer un tableau de bord | Dashboard Streamlit (en développement pour le CODIR). | (À déployer) |
| BC03 | Reporting des tendances | Exports HTML (Plotly) et synthèse écrite. | [output/dataviz/](https://github.com/ferialzamoun-afk/P6_ameliore_IA/tree/main/output/dataviz) + [06_synthese_finale](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/06_synthese_finale_P13_partie_1.md) |
| BC04 | Veille métier/technologique | Benchmark Pandas vs GE vs Soda + roadmap migration. | [02_veille_technologique](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/02_veille_technologique_P13_partie_1.md) |
| BC04 | Formaliser le cahier des charges | Cahier des charges complet (objectifs, contraintes, livrables). | [01_cahier_des_charges](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/01_cahier_des_charges_P13_partie_1.md) |
| BC04 | Organiser un projet data | Backlog, kanban, planning (GitHub Projects). | [04_plan_projet](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/04_plan_projet_P13_partie_1.md) + [captures](https://github.com/ferialzamoun-afk/P6_ameliore_IA/tree/main/output/captures) |
| BC04 | Gérer la documentation | 8 docs + 26 prompts IA + 13 graphiques documentés. | [docs/](https://github.com/ferialzamoun-afk/P6_ameliore_IA/tree/main/docs) |
| BC04 | Adapter sa posture | Journal IA (décisions humaines + limitations). | [03_journal_ia](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/03_journal_ia_P13_partie_1.md) |
| BC05 | Analyses multivariées | Analyse Pareto + corrélations (prix, marges, stocks). | [eda_analysis.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/eda_analysis.py) |
| BC05 | Tests statistiques | Validation des KPI (cohérence, outliers). | [kpi_analysis.py](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/src/kpi_analysis.py) |


🎯 Mapping RNCP 37837

Blocs couverts par ce projet :

✅ BC01 : Structurer et gérer la base de données (rapprochement 3 sources, Data Contracts)
✅ BC02 : Identifier, collecter et analyser les données (nettoyage, EDA, KPI)
✅ BC03 : Visualiser des données et interpréter des résultats (13 graphiques Plotly, synthèse)
✅ BC04 : Piloter un projet data (documentation, CI, organisation, veille, posture consultante)
✅ BC05 : Spécialisation Statistiques (Pareto, corrélations, tests statistiques)


