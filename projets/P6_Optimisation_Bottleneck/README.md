# 🍷 **P6 Amélioré : Optimisation de la Gestion des Données – Bottleneck Wine Shop**
**Amélioration du livrable P6 avec IA critique, documentation complète et traçabilité totale pour une analyse décisionnelle optimisée.**

> **🔹 Reproductible**   **📊 Traçable** | **🤖 IA Documentée** | **⚡ Optimisé (-68% cells, -76% temps)**

**📅 Date** : Juillet 2026
**🏷️ Type** : Analyse Exploratoire / Data Cleaning / KPI Business / IA Assistée
**🔗 Liens** :
- [🔗 Portfolio P13](https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/projets/P13_portfolio/)
- [📓 Notebook Principal](notebooks/bottleneck_analyse_ameliore_final.ipynb)
- [📓 Notebook Production](notebooks/bottleneck_analyse_ameliore_final.ipynb)
- [📁 Cahier des Charges](docs/01_cahier_des_charges_P13_partie_1.md)
- [📁 Veille Technologique](docs/02_veille_technologique_P13_partie_1.md)
- [📁 Journal IA](docs/03_journal_ia_P13_partie_1.md)
- [📁 Synthèse Finale](docs/06_synthese_finale_P13_partie_1.md)
- [📊 Dataviz (13 graphiques)](output/dataviz/)
- [🖼️ Captures Portfolio](output/captures/)

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
git clone https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA.git
cd MON-PORTFOLIO-DATA

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
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Étape</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Résultat</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuve</strong></th></tr></thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Données chargées</td><td style="padding: 10px 12px; border: 1px solid #ddd;">825 (ERP) + 1 513 (Web) + 825 (Liaison)</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/data_merging.py">data_merging.py</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Contrôles qualité</td><td style="padding: 10px 12px; border: 1px solid #ddd;">18 points validés : 11 OK, 4 à vérifier, 2 à documenter, 1 corrigé.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/quality_checks.py">quality_checks.py</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Stocks corrigés</td><td style="padding: 10px 12px; border: 1px solid #ddd;">2 exceptions de stock négatif identifiées et tracées.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/stock_cleaning.py">stock_cleaning.py</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Rapprochement ERP/Web</td><td style="padding: 10px 12px; border: 1px solid #ddd;">714 / 1 513 matches (47.2%), anomalies à investiguer.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/data_merging.py">data_merging.py</a></td></tr>
	</tbody>
</table>
🔹 Phase II : KPI Business
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>KPI</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Valeur</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Interprétation</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuve</strong></th></tr></thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">CA total</td><td style="padding: 10px 12px; border: 1px solid #ddd;">143 680 EUR/mois (octobre 2026)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Revenue consolidée</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/kpi_analysis.py">kpi_analysis.py</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Produits avec CA</td><td style="padding: 10px 12px; border: 1px solid #ddd;">689</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Diversité du catalogue</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/eda_analysis.py">eda_analysis.py</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Pareto 80%</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Rang 435</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ Catalogue large, pas fortement concentré</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/dataviz/courbe_pareto_80_20.html">courbe_pareto_80_20.html</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Marge moyenne</td><td style="padding: 10px 12px; border: 1px solid #ddd;">47.32%</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Saine</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/dataviz/anomalies_prix_et_marges.html">anomalies_prix_et_marges.html</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Stock / Rotation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">2.98 mois (moyenne)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ À optimiser, 92 ruptures détectées</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/dataviz/distribution_stocks.html">distribution_stocks.html</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Anomalies détectées</td><td style="padding: 10px 12px; border: 1px solid #ddd;">10 (3 prix invalides, 7 marges négatives)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">🚨 À investiguer</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/dataviz/anomalies_prix_et_marges.html">anomalies_prix_et_marges.html</a></td></tr>
	</tbody>
</table>
🔹 Dataviz Générées (13 fichiers Plotly)
(Bloc RNCP37837BC03 : Visualiser des données et interpréter des résultats)
- [📊 Chiffre d’affaires par catégorie](output/dataviz/chiffre_affaires_par_categorie.html)
- [📈 Courbe Pareto 80/20](output/dataviz/courbe_pareto_80_20.html)
- [⚠️ Anomalies prix et marges](output/dataviz/anomalies_prix_et_marges.html)
- [📦 Distribution des stocks](output/dataviz/distribution_stocks.html)
- [🔄 Rotation mensuelle](output/dataviz/rotation_mensuelle.html)
- [🔗 Corrélations quantitatives](output/dataviz/correlations_quantitatives.html)
- *(+ 7 autres graphiques disponibles dans [output/dataviz/](output/dataviz/))*

🔧 Méthodologie et Choix Technologiques
(Blocs RNCP37837BC02, BC04)
📌 Contrôle Qualité : Pourquoi Pandas ?
(Bloc RNCP37837BC04 : Piloter un projet data)
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Critère</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Pandas</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Great Expectations</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Soda Core</strong></th></tr></thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Temps d’implémentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚡ Rapide (J+30 OK)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">🐢 Courbe d’apprentissage raide</td><td style="padding: 10px 12px; border: 1px solid #ddd;">🐢 Dépendance externe</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Reproductibilité</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Native</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ OK</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ Config YAML complexe</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Sobriété / Dépendances</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Minimal</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ Lourd</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ Lourd</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Audit Trail</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Logs Pandas</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ Full</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ Limité</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">RGPD / Chemins</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ OK</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅ OK</td><td style="padding: 10px 12px; border: 1px solid #ddd;">⚠️ À vérifier</td></tr>
	</tbody>
</table>
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
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Dimension</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>P6 Initial</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>P6 Amélioré</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Gain</strong></th></tr></thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Cellules notebook</td><td style="padding: 10px 12px; border: 1px solid #ddd;">148</td><td style="padding: 10px 12px; border: 1px solid #ddd;">49</td><td style="padding: 10px 12px; border: 1px solid #ddd;">-68%</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Temps d’exécution</td><td style="padding: 10px 12px; border: 1px solid #ddd;">~5 min</td><td style="padding: 10px 12px; border: 1px solid #ddd;">1:11 min</td><td style="padding: 10px 12px; border: 1px solid #ddd;">-76%</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Code cells</td><td style="padding: 10px 12px; border: 1px solid #ddd;">105</td><td style="padding: 10px 12px; border: 1px solid #ddd;">39</td><td style="padding: 10px 12px; border: 1px solid #ddd;">-63%</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Markdown cells</td><td style="padding: 10px 12px; border: 1px solid #ddd;">43</td><td style="padding: 10px 12px; border: 1px solid #ddd;">8</td><td style="padding: 10px 12px; border: 1px solid #ddd;">-81%</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Erreurs/warnings</td><td style="padding: 10px 12px; border: 1px solid #ddd;">1 major</td><td style="padding: 10px 12px; border: 1px solid #ddd;">0</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Contrôles qualité</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Implicites</td><td style="padding: 10px 12px; border: 1px solid #ddd;">18 explicites</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Data Contracts</td><td style="padding: 10px 12px; border: 1px solid #ddd;">0</td><td style="padding: 10px 12px; border: 1px solid #ddd;">7 formalisés</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Checkpoints</td><td style="padding: 10px 12px; border: 1px solid #ddd;">0</td><td style="padding: 10px 12px; border: 1px solid #ddd;">4 internes</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Documentation IA</td><td style="padding: 10px 12px; border: 1px solid #ddd;">0</td><td style="padding: 10px 12px; border: 1px solid #ddd;">26 prompts tracés</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Reproductibilité</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Chemins locaux</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Chemins relatifs</td><td style="padding: 10px 12px; border: 1px solid #ddd;">✅</td></tr>
	</tbody>
</table>

📚 Documentation Complète
(Bloc RNCP37837BC04 : Piloter un projet data)

Tous les 10 critères mission P13 Partie 1 sont documentés et tracés :
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Critère</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Document</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Lien</strong></th></tr></thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Améliorer le livrable</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Synthèse avant/après</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/06_synthese_finale_P13_partie_1.md">06_synthese_finale</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">IA critique & documentée</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Journal IA (26 prompts)</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/03_journal_ia_P13_partie_1.md">03_journal_ia</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Tester plusieurs options</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Benchmark outils (Pandas/GE/Soda)</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/02_veille_technologique_P13_partie_1.md">02_veille_technologique</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Critères explicites</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Tableau comparaison + méthodologie</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="notebooks/bottleneck_analyse_ameliore_final.ipynb">Notebook, Cellule 2</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Justifier les choix</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Chaque cellule commence par "Pourquoi ?"</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="notebooks/bottleneck_analyse_ameliore_final.ipynb">Notebook complet</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier les besoins métier</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Cahier des charges complet</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/01_cahier_des_charges_P13_partie_1.md">01_cahier_des_charges</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Cahier des charges</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Document complet (CDC)</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/01_cahier_des_charges_P13_partie_1.md">01_cahier_des_charges</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Organiser le projet</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Backlog, kanban, planning</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/04_plan_projet_P13_partie_1.md">04_plan_projet</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Outils de gestion</td><td style="padding: 10px 12px; border: 1px solid #ddd;">GitHub Projects Kanban</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/captures/">Captures disponibles</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Intégrer les contraintes</td><td style="padding: 10px 12px; border: 1px solid #ddd;">5 types documentés : délai, RGPD, budget, sobriété, conformité.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/04_plan_projet_P13_partie_1.md">04_plan_projet</a></td></tr>
	</tbody>
</table>

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
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Module</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Rôle</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Lien</strong></th></tr></thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">quality_checks.py</td><td style="padding: 10px 12px; border: 1px solid #ddd;">18 contrôles de données : structure, valeurs et doublons.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/quality_checks.py">Lien</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">stock_cleaning.py</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Corrections tracées des anomalies de stock.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/stock_cleaning.py">Lien</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">data_merging.py</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Rapprochement ERP/Web/Liaison avec logging.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/data_merging.py">Lien</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">eda_analysis.py</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses exploratoires : Pareto et corrélations.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/eda_analysis.py">Lien</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">kpi_analysis.py</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Calcul des KPI métier : CA, marges et rotation.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/kpi_analysis.py">Lien</a></td></tr>
	</tbody>
</table>

⚠️ Limites et Prudences
(Bloc RNCP37837BC05 : Spécialisation Statistiques)
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Limite</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Impact</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Recommandation</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuve</strong></th></tr></thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">1 mois de données (octobre 2026)</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Snapshot, pas de tendance</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Confirmer sur multi-mois</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/06_synthese_finale_P13_partie_1.md">06_synthese_finale</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Corrélations ≠ causalité</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Risque de faux signaux</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Utiliser comme aide à la décision, pas comme preuve</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="notebooks/bottleneck_analyse_ameliore_final.ipynb">Notebook, Cellule 7</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Outliers statistiques</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Modèle IQR</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Valider avec l’équipe métier les prix premium légitimes</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/dataviz/anomalies_prix_et_marges.html">anomalies_prix_et_marges.html</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Stock/Liaison manuels</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Risque de désynchronisation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Investiguer 799 références Web sans match ERP</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/data_merging.py">data_merging.py</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Pas d’historique</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Données point-in-time</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Intégrer l’historique pour analyser les tendances</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/06_synthese_finale_P13_partie_1.md">06_synthese_finale</a></td></tr>
	</tbody>
</table>

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
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead><tr style="background-color: #155799; color: white;"><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Bloc RNCP</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Compétence</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th><th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuves</strong></th></tr></thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">BC01</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Structurer et gérer la base de données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Rapprochement de 3 sources en une base unifiée.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/data_merging.py">data_merging.py</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">BC01</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer une base de données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">18 contrôles qualité et 7 Data Contracts formalisés.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/quality_checks.py">quality_checks.py</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">BC02</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier et collecter les données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Utilisation des 3 sources Bottleneck : ERP, Web, Liaison.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="notebooks/bottleneck_analyse_ameliore_final.ipynb">Notebook, Cellule 1</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">BC02</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Extraire et agréger</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Nettoyage des stocks/prix et rapprochement des données.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/stock_cleaning.py">stock_cleaning.py</a> + <a href="src/data_merging.py">data_merging.py</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">BC02</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Explorer et pré-traiter</td><td style="padding: 10px 12px; border: 1px solid #ddd;">EDA : Pareto, corrélations et anomalies.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/eda_analysis.py">eda_analysis.py</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">BC02</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse univariée/multivariée</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse Pareto : 80% du CA sur 435 produits.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/dataviz/courbe_pareto_80_20.html">courbe_pareto_80_20.html</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">BC03</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Solution de visualisation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">13 graphiques Plotly : CA, Pareto, anomalies, stocks.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/dataviz/">output/dataviz/</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">BC03</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Créer un tableau de bord</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard Streamlit en développement pour le CODIR.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">(À déployer)</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">BC03</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Reporting des tendances</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Exports HTML Plotly et synthèse écrite.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="output/dataviz/">output/dataviz/</a> + <a href="docs/06_synthese_finale_P13_partie_1.md">06_synthese_finale</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">BC04</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Veille métier/technologique</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Benchmark Pandas vs GE vs Soda et roadmap migration.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/02_veille_technologique_P13_partie_1.md">02_veille_technologique</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">BC04</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Formaliser le cahier des charges</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Cahier des charges complet avec objectifs, contraintes et livrables.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/01_cahier_des_charges_P13_partie_1.md">01_cahier_des_charges</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">BC04</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Organiser un projet data</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Backlog, kanban et planning GitHub Projects.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/04_plan_projet_P13_partie_1.md">04_plan_projet</a> + <a href="output/captures/">captures</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">BC04</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer la documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">8 docs, 26 prompts IA et 13 graphiques documentés.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/">docs/</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">BC04</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Adapter sa posture</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Journal IA : décisions humaines et limitations.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="docs/03_journal_ia_P13_partie_1.md">03_journal_ia</a></td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">BC05</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses multivariées</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse Pareto et corrélations prix/marges/stocks.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/eda_analysis.py">eda_analysis.py</a></td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">BC05</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Tests statistiques</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Validation des KPI : cohérence et outliers.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="src/kpi_analysis.py">kpi_analysis.py</a></td></tr>
	</tbody>
</table>


🎯 Mapping RNCP 37837

Blocs couverts par ce projet :

✅ BC01 : Structurer et gérer la base de données (rapprochement 3 sources, Data Contracts)
✅ BC02 : Identifier, collecter et analyser les données (nettoyage, EDA, KPI)
✅ BC03 : Visualiser des données et interpréter des résultats (13 graphiques Plotly, synthèse)
✅ BC04 : Piloter un projet data (documentation, CI, organisation, veille, posture consultante)
✅ BC05 : Spécialisation Statistiques (Pareto, corrélations, tests statistiques)


