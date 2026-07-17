# 🏪 P14 — Stage : Analyse de Données Retail (Intermarché)

> **Type** : Stage · Retail analytics · Python · Power BI · Streamlit
> **Contexte** : Mission de stage en entreprise — données retail / assortiment
> **Date** : 2025–2026

---

## 🎯 1. Contexte et besoin métier

Mission de stage dans un contexte retail (périmètre Intermarché), centré sur le pilotage de la **disponibilité produit**, la **performance assortiment** et la **gouvernance des indicateurs**.

**Problème** : les données opérationnelles sont dispersées entre plusieurs sources, sans socle analytique consolidé permettant un pilotage métier fiable et reproductible.

**Enjeux** :
- Structurer les données depuis les sources brutes jusqu'aux jeux exploitables
- Produire des analyses reproductibles via notebooks et scripts
- Alimenter des restitutions métier via Power BI et une application Streamlit
- Conserver une documentation projet claire pour la maintenance et la transmission

**Thématiques métier couvertes** :
- Disponibilité produit et alertes assortiment
- Performance opérationnelle par rayon / segment
- Gouvernance des indicateurs et traçabilité des décisions

---

## 🧭 2. Démarche analytique

### **📊 Structure du Projet**
```text
P14/
├── data/
├── docs/
├── intermarche_notebook/
├── powerbi/
├── streamlit_app/
├── .gitignore
├── bilan_reflexif_stage_P14.md
├── feuille_de_route_stage_P5.md
├── modele_mail_note_livraison.md
└── README.md
```

**Architecture du pipeline** :

`data/raw/ -> préparation -> data/processed/ -> analyse -> Power BI / Streamlit`

**Couches du pipeline** :
- data/raw/ : données sources non modifiées (jamais transformées)
- data/processed/ : données nettoyées et standardisées prêtes pour l'analyse
- data/Fichiers transformés/DLP/ : jeux transformés liés au périmètre DLP

**Conventions qualité** :
- Journaliser les contrôles (doublons, clés, granularité, valeurs manquantes)
- Expliciter les prérequis d'exécution dans chaque sous-module
- Documenter toute transformation majeure dans docs/
- Séparer clairement les données brutes, transformées et publiées

**Flux de travail** :
1. **Ingestion et préparation** : nouvelles sources dans `data/raw/`, exécution notebooks/scripts, sorties dans `data/processed/`
2. **Analyse** : notebooks intermarche_notebook/ et powerbi/notebooks/, hypothèses tracées dans docs/
3. **Restitution** : mise à jour artefacts Power BI, cohérence avec l'application Streamlit

---

## 📊 3. Résultats et livrables

<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead>
		<tr style="background-color: #155799; color: white;">
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Livrable</strong></th>
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebooks d'analyse</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Exploration et analyse sur le périmètre Intermarché.</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Application Streamlit</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Vue applicative pour la restitution métier opérationnelle.</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Rapports Power BI</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Tableaux de bord décisionnels avec KPI de pilotage.</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Documentation projet</td><td style="padding: 10px 12px; border: 1px solid #ddd;">docs/, conventions et procédures.</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Bilan réflexif de stage</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Retour d'expérience et formalisation des apprentissages.</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Feuille de route</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Cadrage et contexte de la mission (feuille_de_route_stage_P5.md).</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Modèle de livraison</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Template de communication de livraison (modele_mail_note_livraison.md).</td></tr>
	</tbody>
</table>

---

## 🎓 4. Compétences RNCP 37837 mobilisées

<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead>
		<tr style="background-color: #155799; color: white;">
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Bloc</strong></th>
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Compétence</strong></th>
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Ce qui a été fait</strong></th>
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuve</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier et collecter</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Exploitation des données retail brutes Intermarché.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">data/raw/</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Extraire et agréger</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pipeline de transformation raw vers processed.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Scripts de préparation</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Vérifier la cohérence</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Contrôles qualité : doublons, clés, granularité, NaN.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Journaux de contrôle</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse univariée / multivariée</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse disponibilité, performance et KPI assortiment.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebooks</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Créer un tableau de bord</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Rapports Power BI et application Streamlit.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">powerbi/ + streamlit_app/</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Reporting des tendances</td><td style="padding: 10px 12px; border: 1px solid #ddd;">KPI pilotage, alertes assortiment et suivi temporel.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Rapports Power BI</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Organiser un projet data</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Architecture raw/processed, documentation et conventions.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">docs/</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer la documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">README, bilan réflexif, feuille de route et rapports.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Tous les livrables docs</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Adapter sa posture</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Positionnement professionnel en contexte réel.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Bilan réflexif de stage</td></tr>
	</tbody>
</table>

---

## 💡 5. Impact et apprentissages

**Ce que ça a apporté** : un socle analytique opérationnel permettant une meilleure priorisation des actions sur la disponibilité produit et la performance assortiment.

**Veille métier** : problématiques retail (disponibilité produit, performance assortiment, pilotage des alertes) → indicateurs priorisés, règles de gestion, critères d'arbitrage documentés.

**Veille technologique** : Python (pandas/notebooks), Streamlit, Power BI → structuration raw/processed, fiabilisation des transformations, documentation des hypothèses.

**Bilan de stage** : expérience en contexte professionnel réel — mise en pratique de l'ensemble du pipeline analytique de la collecte à la restitution décisionnelle. Voir ilan_reflexif_stage_P14.md.

---

## 🔗 Points d'entrée utiles

- [Résumé réflexif](resume_bilan_reflexif.md) : retour d'expérience de stage
- [Proof point stage](PROOF_POINT.md) : synthèse courte du stage
- [README du stage](README.md) : vue d'ensemble du contexte, de la démarche et des livrables

---

*Férial Zamoun · Stage Data Analyst · [GitHub](https://github.com/ferialzamoun-afk)*
