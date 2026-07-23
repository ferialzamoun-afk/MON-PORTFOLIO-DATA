# 🍷 **P6 Amélioré : Optimisation de la Gestion des Données – Bottleneck Wine Shop**
**Amélioration du livrable P6 avec IA critique, documentation structurée et preuves détaillées pour une restitution métier plus lisible.**

> **🔹 Reproductible**   **📊 Traçable** | **🤖 IA Documentée** | **⚡ Optimisé (-56% cellules) + BC05 décisionnel strict**

**📅 Date** : Juillet 2026
**🏷️ Type** : Analyse Exploratoire / Data Cleaning / KPI Business / IA Assistée
**🔗 Liens** :

<table>
	<thead>
		<tr>
			<th>Ressource</th>
			<th>Lien</th>
		</tr>
	</thead>
	<tbody>
		<tr><td>🔗 Portfolio P13</td><td><a href="https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P13_portfolio/">Accéder</a></td></tr>
		<tr><td>📓 Notebook principal</td><td><a href="https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb">Accéder</a></td></tr>
		<tr><td>📁 Cahier des charges</td><td><a href="https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/02_cahier_des_charges_fonctionnel.html">Accéder</a></td></tr>
		<tr><td>📁 Veille technologique</td><td><a href="https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/01_veille_metier_technologique.html">Accéder</a></td></tr>
		<tr><td>📁 Journal IA</td><td><a href="https://github.com/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/docs/03_journal_ia_P13_partie_1.md">Accéder</a></td></tr>
		<tr><td>📁 Synthèse finale</td><td><a href="https://github.com/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/docs/06_synthese_finale_P13_partie_1.md">Accéder</a></td></tr>
		<tr><td>📘 Mode d'emploi dashboard</td><td><a href="https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/09_mode_emploi_dashboard.html">Accéder</a></td></tr>
		<tr><td>📊 Dataviz (25 visuels)</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/output/dataviz">Accéder</a></td></tr>
		<tr><td>🖼️ Captures Portfolio</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/output/captures">Accéder</a></td></tr>
	</tbody>
</table>

**Preuves détaillées et restitution métier** :

<table>
	<thead>
		<tr>
			<th>Preuve</th>
			<th>Accès</th>
		</tr>
	</thead>
	<tbody>
		<tr><td>Avant : Notebook initial</td><td><a href="https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P6_Optimisation_Bottleneck/">Voir</a></td></tr>
		<tr><td>Après : Notebook amélioré</td><td><a href="https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb">Voir</a></td></tr>
		<tr><td>Avant : Synthèse initiale</td><td>Non conservée dans le dépôt public</td></tr>
		<tr><td>Après : Synthèse finale enrichie</td><td><a href="https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/06_resultats.html">Voir</a></td></tr>
		<tr><td>Avant : Visuels HTML</td><td><a href="https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P6_Optimisation_Bottleneck/">Voir</a></td></tr>
		<tr><td>Après : Visuels PNG</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/output/dataviz">Voir</a></td></tr>
		<tr><td>Dashboard KPI pour le CODIR</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/output/captures">Voir</a></td></tr>
		<tr><td>Mode d'emploi utilisateur du dashboard</td><td><a href="https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/09_mode_emploi_dashboard.html">Voir</a></td></tr>
	</tbody>
</table>

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
>    - Réduire la taille du notebook (**148 → 65 cellules, -56%**) tout en ajoutant le renfort BC05.
>    - Conserver une exécution courte (**~1 min 30** sur la version enrichie).
>    - **Documenter chaque étape** (IA, contrôles qualité, décisions).
>    - Fournir un **dashboard KPI** clair pour la lecture CODIR.
>    - Montrer la trace **avant / après** entre le livrable initial et la version améliorée.
>    - Séparer la priorisation stricte (`critical_score`) de la surveillance statistique (`surveillance_score`).

> **Approche P13** :
> *"**Pandas pragmatique** (court terme, J+30) avec **Data Contracts formalisés** en vue d’une migration vers **Great Expectations v19+** (moyen terme)."*

---

## **📊 Structure du Projet**
| Élément | Contenu | Rôle |
|---|---|---|
| `README.md` | Ce fichier | Point d’entrée du livrable |
| `requirements.txt` | Dépendances Python | Reproductibilité de l’environnement |
| `notebooks/bottleneck_analyse_ameliore_final.ipynb` | Notebook final | Analyse principale, 65 cellules, exécution ~1:30 |
| `src/quality_checks.py` | Script Python | 18 contrôles de qualité des données |
| `src/stock_cleaning.py` | Script Python | Correction des anomalies de stock |
| `src/data_merging.py` | Script Python | Rapprochement ERP / Web / Liaison |
| `src/eda_analysis.py` | Script Python | Analyses exploratoires, Pareto, corrélations |
| `src/kpi_analysis.py` | Script Python | Calcul des KPI métier (CA, marges, rotation) |
| `02_cahier_des_charges_fonctionnel.html` | Documentation | Cahier des charges fonctionnel public |
| `01_veille_metier_technologique.html` | Documentation | Veille métier et technologique |
| `08_decisions.html` | Documentation | Décisions IA et arbitrages humains |
| `04_hypotheses.html` | Documentation | Hypothèses de travail |
| `05_tests.html` | Documentation | Tests et validations |
| `06_resultats.html` | Documentation | Résultats et recommandations |
| `09_mode_emploi_dashboard.html` | Documentation | Mode d'emploi dashboard |
| `output/dataviz/` | Graphiques HTML/PNG | 13 graphiques Phase II + 12 visuels BC05 |
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
✅ 25 visuels dans output/dataviz/ : 13 graphiques Phase II + 12 visuels BC05.
✅ Rapport de qualité : 18 contrôles + 7 Data Contracts validés.
✅ Temps total : ~1 minute 30 secondes sur la version enrichie (vs ~5 min initialement).

### **📊 Résultats Clés**
(Blocs RNCP37837BC02, BC03, BC05)
<table>
	<thead>
		<tr>
			<th>Bloc</th>
			<th>Élément</th>
			<th>Résultat</th>
			<th>Preuve</th>
		</tr>
	</thead>
	<tbody>
		<tr><td>Phase I</td><td>Données chargées</td><td>825 ERP + 1 513 Web + 825 Liaison</td><td>data_merging.py</td></tr>
		<tr><td>Phase I</td><td>Contrôles qualité</td><td>18 points validés (11 OK, 4 à vérifier, 2 à documenter, 1 corrigé)</td><td>quality_checks.py</td></tr>
		<tr><td>Phase I</td><td>Stocks corrigés</td><td>2 exceptions stock &lt; 0 identifiées et tracées</td><td>stock_cleaning.py</td></tr>
		<tr><td>Phase I</td><td>Rapprochement ERP/Web</td><td>714 / 1 513 matches (47,2%)</td><td>data_merging.py</td></tr>
		<tr><td>Phase II</td><td>CA total</td><td>143 680 EUR/mois (octobre 2026)</td><td>kpi_analysis.py</td></tr>
		<tr><td>Phase II</td><td>Produits avec CA</td><td>689</td><td>eda_analysis.py</td></tr>
		<tr><td>Phase II</td><td>Pareto 80%</td><td>Rang 435</td><td>courbe_pareto_80_20.html</td></tr>
		<tr><td>Phase II</td><td>Marge moyenne</td><td>47.32%</td><td>anomalies_prix_et_marges.html</td></tr>
		<tr><td>Phase II</td><td>Stock / Rotation</td><td>2.98 mois (moyenne)</td><td>distribution_stocks.html</td></tr>
		<tr><td>Phase II</td><td>Anomalies détectées</td><td>10 (3 prix invalides, 7 marges négatives)</td><td>anomalies_prix_et_marges.html</td></tr>
		<tr><td>BC05</td><td>Alertes immédiates</td><td>36 alertes statistiques (4,36%)</td><td>bc05_alertes_actionnables.csv</td></tr>
		<tr><td>BC05</td><td>Isolation Forest</td><td>25 alertes multivariées</td><td>bc05_iforest_alerts.csv</td></tr>
		<tr><td>BC05</td><td>K-Means</td><td>4 clusters produits</td><td>bc05_kmeans_scatter</td></tr>
		<tr><td>BC05</td><td>kNN</td><td>42 produits rares au seuil 95e percentile</td><td>bc05_knn_scatter</td></tr>
		<tr><td>BC05</td><td>Matrice décisionnelle stricte</td><td>825 produits : 1 critique, 172 à surveiller, 652 normaux</td><td>bc05_matrice_decisionnelle.csv</td></tr>
		<tr><td>Dataviz</td><td>Chiffre d’affaires par catégorie</td><td>Graphique de synthèse</td><td>HTML</td></tr>
		<tr><td>Dataviz</td><td>Courbe Pareto 80/20</td><td>Visualisation des ventes concentrées</td><td>HTML</td></tr>
		<tr><td>Dataviz</td><td>Anomalies prix et marges</td><td>Contrôle des valeurs aberrantes</td><td>HTML</td></tr>
		<tr><td>Dataviz</td><td>Distribution des stocks</td><td>Répartition des niveaux de stock</td><td>HTML</td></tr>
		<tr><td>Dataviz</td><td>Rotation mensuelle</td><td>Suivi de rotation</td><td>HTML</td></tr>
		<tr><td>Dataviz</td><td>Corrélations quantitatives</td><td>Relations entre variables</td><td>HTML</td></tr>
		<tr><td>Dataviz</td><td>Autres visuels</td><td>7 graphiques supplémentaires + 12 visuels BC05</td><td>output/dataviz/</td></tr>
	</tbody>
</table>

### **🧭 Règle de décision BC05 retenue**

| Niveau | Score | Rôle |
|---|---|---|
| **Critique** | `critical_score >= 0.65` | IF + SHAP + impact business ; short-list actionnable CODIR |
| **À surveiller** | `surveillance_score >= 0.45` | IF + kNN + K-Means + SHAP + impact ; backlog d'investigation |
| **Normal** | Sous les seuils | Suivi standard |

Le kNN est un score non supervisé de rareté locale : il aide à ordonner les investigations, mais ne déclenche pas seul une urgence critique.

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
| Cellules notebook | 148 | 65 | -56% malgré le renfort BC05 |
| Temps d’exécution | ~5 min | ~1:30 min | ~70% plus rapide |
| Code cells | 105 | 28 | -73% |
| Markdown cells | 43 | 37 | Documentation renforcée |
| Erreurs/warnings | 1 major | 0 | ✅ |
| Contrôles qualité | Implicites | 18 explicites | ✅ |
| Data Contracts | 0 | 7 formalisés | ✅ |
| Checkpoints | 0 | 4 internes | ✅ |
| Documentation IA | 0 | 26 prompts tracés | ✅ |
| Alertes BC05 | 0 | 36 alertes + matrice 825 produits | ✅ |
| Modèles avancés | 0 | IF, SHAP, K-Means, kNN | ✅ |
| Reproductibilité | Chemins locaux | Chemins relatifs | ✅ |

### **📚 Documentation Complète**
(Bloc RNCP37837BC04 : Piloter un projet data)

Tous les 10 critères mission P13 Partie 1 sont documentés et tracés :
| Critère | Document | Lien |
| --- | --- | --- |
| Améliorer le livrable | Synthèse avant/après | [06_resultats](06_resultats.html) |
| IA critique & documentée | Journal IA / décisions | [08_decisions](08_decisions.html) |
| Tester plusieurs options | Benchmark outils (Pandas/GE/Soda/IF/SHAP/kNN) | [01_veille_metier_technologique](01_veille_metier_technologique.html) |
| Critères explicites | Tableau comparaison + méthodologie | [Notebook, Cellule 2](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb) |
| Justifier les choix | Chaque cellule commence par "Pourquoi ?" | [Notebook complet](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb) |
| Identifier les besoins métier | Cahier des charges complet | [02_cahier_des_charges_fonctionnel](02_cahier_des_charges_fonctionnel.html) |
| Cahier des charges | Document complet (CDC) | [02_cahier_des_charges_fonctionnel](02_cahier_des_charges_fonctionnel.html) |
| Organiser le projet | Hypothèses, tests, décisions | [04_hypotheses](04_hypotheses.html) + [05_tests](05_tests.html) |
| Outils de gestion | GitHub Projects Kanban | [Captures disponibles](output/captures/) |
| Intégrer les contraintes | 5 types documentés (délai, RGPD, budget, sobriété, conformité) | [08_decisions](08_decisions.html) |


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
| 1 mois de données (octobre 2026) | Snapshot, pas de tendance | Confirmer sur multi-mois | [06_resultats](06_resultats.html) |
| Corrélations ≠ causalité | Risque de faux signaux | Utiliser comme aide à la décision, pas comme preuve | [Notebook, Cellule 7](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb) |
| Outliers statistiques | Modèle IQR | Valider avec l’équipe métier (prix premium légitimes ?) | [anomalies_prix_et_marges.html](output/dataviz/anomalies_prix_et_marges.html) |
| Stock/Liaison manuels | Risque de désynchronisation | Investiguer 799 références Web sans match ERP | [data_merging.py](src/data_merging.py) |
| Pas d’historique | Données point-in-time | Intégrer l’historique pour analyser les tendances | [06_resultats](06_resultats.html) |

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

<table>
	<thead>
		<tr>
			<th>Bloc RNCP</th>
			<th>Compétence</th>
			<th>Description</th>
			<th>Preuves</th>
		</tr>
	</thead>
	<tbody>
		<tr><td>BC01</td><td>Structurer et gérer la base</td><td>Rapprochement ERP, Web et Liaison en base unifiée.</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/src">src/data_merging.py</a></td></tr>
		<tr><td>BC01</td><td>Gérer une base de données</td><td>18 contrôles qualité + 7 Data Contracts.</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/src">src/quality_checks.py</a></td></tr>
		<tr><td>BC02</td><td>Identifier et collecter</td><td>Utilisation des 3 sources Bottleneck.</td><td><a href="https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb">Notebook</a></td></tr>
		<tr><td>BC02</td><td>Extraire et agréger</td><td>Nettoyage stocks/prix et rapprochement des données.</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/src">Scripts Python</a></td></tr>
		<tr><td>BC02</td><td>Explorer et pré-traiter</td><td>EDA, Pareto, corrélations, anomalies.</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/src">eda_analysis.py</a></td></tr>
		<tr><td>BC03</td><td>Visualiser</td><td>13 graphiques Phase II + 12 visuels BC05.</td><td><a href="https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA/output/dataviz">output/dataviz</a></td></tr>
		<tr><td>BC03</td><td>Créer un tableau de bord</td><td>Dashboard KPI Streamlit pour lecture CODIR.</td><td><a href="output/captures/05_kpi_dashboard_phase2.png">Capture dashboard</a></td></tr>
		<tr><td>BC03</td><td>Reporting des tendances</td><td>Exports visuels + synthèse écrite.</td><td><a href="06_resultats.html">06_resultats</a></td></tr>
		<tr><td>BC04</td><td>Veille métier/technologique</td><td>Benchmark Pandas, GE, Soda, IF, SHAP, K-Means, kNN.</td><td><a href="01_veille_metier_technologique.html">01_veille</a></td></tr>
		<tr><td>BC04</td><td>Formaliser le cahier des charges</td><td>Objectifs, contraintes et livrables.</td><td><a href="02_cahier_des_charges_fonctionnel.html">02_cahier</a></td></tr>
		<tr><td>BC04</td><td>Organiser un projet data</td><td>Hypothèses, tests, résultats et décisions.</td><td><a href="04_hypotheses.html">04_hypotheses</a> + <a href="05_tests.html">05_tests</a></td></tr>
		<tr><td>BC04</td><td>Gérer la documentation</td><td>Pages publiques, décisions IA, mode d'emploi dashboard.</td><td><a href="08_decisions.html">08_decisions</a> + <a href="09_mode_emploi_dashboard.html">09_mode_emploi</a></td></tr>
		<tr><td>BC05</td><td>Analyses multivariées</td><td>Isolation Forest, SHAP, K-Means, kNN, score strict et surveillance.</td><td><a href="06_resultats.html">06_resultats</a></td></tr>
		<tr><td>BC05</td><td>Tests statistiques</td><td>Validation KPI, outliers et matrice décisionnelle stricte.</td><td><a href="05_tests.html">05_tests</a></td></tr>
	</tbody>
</table>


🎯 Mapping RNCP 37837

Blocs couverts par ce projet :

✅ BC01 : Structurer et gérer la base de données (rapprochement 3 sources, Data Contracts)
✅ BC02 : Identifier, collecter et analyser les données (nettoyage, EDA, KPI)
✅ BC03 : Visualiser des données et interpréter des résultats (13 graphiques Plotly, synthèse)
✅ BC04 : Piloter un projet data (documentation, CI, organisation, veille, posture consultante)
✅ BC05 : Spécialisation Statistiques (Pareto, corrélations, tests statistiques)