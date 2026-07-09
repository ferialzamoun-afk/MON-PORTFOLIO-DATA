# US5 - Base immobiliere SQL

Projet d'analyse immobiliere realise en SQL pour structurer une base relationnelle, produire des indicateurs de marche et soutenir la prise de decision.

## Contexte

Dans ce cas d'usage, l'objectif est de manipuler une base immobiliere avec une approche orientee metier:

- fiabiliser la structure des donnees,
- interroger les transactions de facon pertinente,
- restituer des constats lisibles sur les prix et les volumes.

## Objectif metier

Construire une vision analytique exploitable du marche immobilier afin d'aider a:

- suivre les dynamiques de prix,
- comparer des zones geographiques,
- identifier des tendances de volume et d'activite.

## Perimetre des donnees et sources

- Donnees structurees dans une base relationnelle orientee immobilier.
- Appui documentaire fourni par un dictionnaire de donnees projet.
- Restitution de synthese formalisee dans le support de presentation.

## Methode

1. Cadrage des entites et des attributs via le dictionnaire de donnees.
2. Verification de la coherence des champs utilises pour les analyses.
3. Construction de requetes SQL d'analyse (selection, agregation, filtres, comparaisons).
4. Production d'indicateurs metiers sur les prix et les volumes.
5. Interpretation des resultats dans une logique aide a la decision.

## Resultats et livrables

- Dictionnaire de donnees pour decrire la structure exploitee.
- Support de presentation des analyses et conclusions metiers.
- Jeu de requetage SQL mobilise durant le projet pour produire les indicateurs.

## Limites et suites

- Les performances de requetes peuvent etre ameliorees via indexation selon les usages.
- La qualite des analyses depend de la granularite et de la completude des donnees sources.
- Une suite naturelle est la mise en place d'un tableau de bord automatisant les KPI immobiliers.

## Preuve de competences

### Resultats de veille metier

- Veille sur les usages d'analyse du marche immobilier: evolution des prix, dynamique des ventes, comparaisons territoriales.
- Traduction des attentes metier en questions SQL orientees pilotage.
- Apport metier: priorisation des indicateurs les plus utiles a l'arbitrage.

### Resultats de veille technologique

- Veille sur les bonnes pratiques SQL (structuration relationnelle, jointures, agregations, lisibilite des requetes).
- Choix retenus: approche progressive du simple vers l'agrege pour fiabiliser les resultats.
- Apport technique: meilleure robustesse des analyses et restitution plus reproductible.

### Tracabilite des preuves

- Competence: comprendre un modele de donnees metier | Action: formalisation des champs/definitions | Preuve: assets/Zamoun_Férial_1_dictionnaire_de_donnees_24112025.xlsx.
- Competence: produire une analyse SQL exploitable | Action: creation de requetes d'analyse prix/volume | Preuve: resultats presentes dans le support de restitution.
- Competence: communiquer les conclusions | Action: synthese des analyses pour un public metier | Preuve: assets/Zamoun_Férial_1_presentation_112025.pdf.

## Ressources du projet

- Dictionnaire de donnees: assets/Zamoun_Férial_1_dictionnaire_de_donnees_24112025.xlsx
- Presentation: assets/Zamoun_Férial_1_presentation_112025.pdf

## Auteur

Ferial Zamoun
Formation Data Analyst - GRETA Promo 2025
Objectif: alternance en data
