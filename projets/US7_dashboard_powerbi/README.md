# Dashboard SANITORAL - P7

Produire un reporting decisionnel pour faciliter les arbitrages de pilotage projets.

## Contexte

Mission de data analyst pour SANITORAL.
Le dispositif de pilotage est realise dans Power BI avec trois vues ciblees selon le profil utilisateur:

- Directeur General (vision portefeuille et arbitrage strategique)
- Directeur Regional (vision regionale et alertes de pilotage)
- Directeur Pays (vision operationnelle detaillee)

## Objectif metier

Permettre une prise de decision plus rapide et mieux argumentee sur les projets en cours en consolidant les informations de cout, delai et avancement dans un meme environnement de restitution.

## Perimetre des donnees et hypotheses

- Seuil d'alerte principal: ecart superieur a 15%.
- Axes de comparaison: IT versus Marketing, regions, pays, phases projet.
- Granularite d'analyse: portefeuille, projet, phase.
- Phases suivies: A a F ou 1 a 4 selon le modele de donnees retenu.

## Utilisateurs et besoins

### Directeur General

- Evaluer la performance globale du portefeuille pour arbitrer (poursuite, priorisation, arret).
- Suivre le volume de projets en alerte.
- Identifier les ecarts de performance entre departements.

### Directeur Regional

- Isoler les projets en risque dans son perimetre.
- Recevoir des signaux rapides sur les depassements de couts/delais/livrables.
- Analyser les phases qui concentrent les retards.

### Directeur Pays

- Suivre les indicateurs detailles par projet.
- Comparer previsionnel et realise.
- Definir les actions correctives court terme.

### Cheffe de projet (Sophie)

- Identifier les problemes recurrents observes sur les derniers exercices.
- Structurer la narration metier pour la soutenance.

## Methode et conception

- Construction de dashboards Power BI par persona (DG, DR, DP).
- Priorisation d'indicateurs lisibles et actionnables.
- Integration d'elements d'explication dans un onglet de presentation:
  1. Product Strategy Canvas
  2. Etapes de preparation de la procedure de mise a jour des donnees
  3. Modele de donnees (relations et ajustements)

## Resultats et livrables

- 3 dashboards metier (DG, DR, DP).
- 1 onglet de cadrage et documentation integree.
- 1 support de soutenance axe storytelling (incluant prise de parole).

## Limites et suites

- Valider definitivement le referentiel de phases (A-F ou 1-4) pour stabiliser les comparaisons.
- Industrialiser le processus de mise a jour des donnees.
- Ajouter un suivi temporel des alertes pour mesurer l'efficacite des actions correctives.

## Preuve de competences

### Resultats de veille metier

- Veille sur les pratiques de pilotage de portefeuille projets et la gouvernance multi-niveaux (global, regional, local).
- Traduction en besoins analytiques concrets: priorisation des alertes, segmentation par profil decisionnaire, suivi des derives cout/delai/livrables.
- Impact metier vise: arbitrages plus rapides et meilleure lisibilite des priorites.

### Resultats de veille technologique

- Veille sur les bonnes pratiques de visualisation decisionnelle sous Power BI (hierarchie des indicateurs, usage des infobulles, lisibilite des alertes).
- Choix retenus: dashboards differencies par persona, seuil d'alerte explicite, structuration des vues pour l'action.
- Apports: reduction du bruit informationnel et meilleure exploitabilite des analyses en comite de pilotage.

### Tracabilite des preuves

- Competence: cadrer un besoin metier decisionnel | Action: definition de 3 vues cibles par profil | Preuve: dashboards DG, DR, DP.
- Competence: modeliser des indicateurs de performance | Action: mise en place du seuil d'alerte > 15% et comparaisons IT/Marketing | Preuve: pages KPI et visualisations comparatives.
- Competence: documenter une solution data | Action: creation d'un onglet de presentation (canvas, procedure, modele) | Preuve: onglet d'introduction et support de soutenance.