# 📊 P7 — Dashboard Décisionnel Power BI — SANITORAL

> **Type** : Dashboard Power BI · Reporting décisionnel · Multi-persona
> **Date** : 2025
> **Outil** : Power BI Desktop

---

## 🎯 1. Contexte et besoin métier

**Mission** : produire un reporting décisionnel pour SANITORAL afin de faciliter les arbitrages de pilotage projets à trois niveaux de gouvernance.

**Pour qui** :

<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead>
		<tr style="background-color: #155799; color: white;">
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Profil</strong></th>
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Besoin</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Directeur Général</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Vision portefeuille et arbitrage stratégique : poursuite, priorisation, arrêt.</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Directeur Régional</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Isolation des projets en risque et alertes sur les dépassements coût/délai/livrables.</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Directeur Pays</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Suivi opérationnel détaillé et comparaison prévisionnel/réalisé.</td></tr>
	</tbody>
</table>

**Problème** : les informations de coût, délai et avancement sont éparpillées — aucune vue consolidée ne permet des arbitrages rapides en comité de pilotage.

**Enjeux** :
- Prioriser les projets en alerte (seuil : écart > 15%)
- Segmenter l'analyse par département (IT vs Marketing), régions et phases
- Réduire le temps de décision en comité de pilotage

**Périmètre** :
- Axes de comparaison : IT vs Marketing · régions · pays · phases projet
- Granularité : portefeuille → projet → phase
- Phases suivies : A à F selon le modèle de données retenu

---

## 🧭 2. Démarche analytique

**Étapes de conception** :
1. Cadrage des besoins par persona (DG, DR, DP) via Product Strategy Canvas
2. Modélisation des données (relations, ajustements, référentiel de phases)
3. Construction des dashboards différenciés par profil utilisateur
4. Définition des indicateurs d'alerte et des KPI par niveau
5. Intégration d'un onglet de documentation (canvas, procédure de mise à jour, modèle de données)
6. Validation de la narration métier pour la soutenance

**Choix de conception** :
- Dashboards différenciés par persona → réduction du bruit informationnel
- Seuil d'alerte 15% explicite → priorisation immédiate des actions
- Vues structurées pour l'action et non pour la contemplation

**Limites et points d'attention** :
- Valider définitivement le référentiel de phases (A-F ou 1-4) pour stabiliser les comparaisons
- Industrialiser le processus de mise à jour des données
- Ajouter un suivi temporel des alertes pour mesurer l'efficacité des actions correctives

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
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard DG</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Vision portefeuille, alertes stratégiques et comparaison IT/Marketing.</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard DR</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Projets en risque par région, alertes phases et dépassements.</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard DP</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Détail opérationnel par projet, prévisionnel vs réalisé.</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Onglet documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Product Strategy Canvas, procédure de mise à jour et modèle de données.</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Support de soutenance</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Storytelling avec prise de parole orientée décision.</td></tr>
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
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier et collecter</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Collecte des données coût, délai et avancement SANITORAL.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Sources projet</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Vérifier la cohérence</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Validation du référentiel de phases et des relations.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Modèle de données</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Solution de visualisation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">3 dashboards Power BI différenciés par profil.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboards DG / DR / DP</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Créer un tableau de bord</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard multi-pages opérationnel sous Power BI.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Fichier PBIX</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Reporting des tendances</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Seuil d'alerte 15%, KPI cards et comparaisons IT/Marketing.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pages KPI</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Présenter les résultats</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Support storytelling pour la soutenance.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Présentation</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier le besoin métier</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Product Strategy Canvas avec 3 personas définis.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Onglet documentation</td></tr>
		<tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Formaliser le cahier des charges</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Procédure de mise à jour et modèle de données documentés.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Onglet documentation</td></tr>
		<tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Adapter sa posture</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Posture consultant pour challenger les besoins.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Canvas + dashboard</td></tr>
	</tbody>
</table>

---

## 💡 5. Impact et apprentissages

**Ce que ça a apporté** : un dispositif de pilotage consolidé permettant des arbitrages plus rapides en comité de direction, avec une lisibilité immédiate des priorités et des alertes.

**Veille métier** : pratiques de pilotage de portefeuille projets et gouvernance multi-niveaux (global, régional, local) → traduction en besoins analytiques concrets par profil décisionnaire.

**Veille technologique** : bonnes pratiques de visualisation décisionnelle Power BI (hiérarchie des indicateurs, infobulles, lisibilité des alertes) → vues différenciées pour l'action.

---

## 🔗 Ressources

- Dashboards Power BI : ssets/
- Support de soutenance : ssets/

---

*Férial Zamoun · Formation Data Analyst GRETA Promo 2025 · [GitHub](https://github.com/ferialzamoun-afk)*
