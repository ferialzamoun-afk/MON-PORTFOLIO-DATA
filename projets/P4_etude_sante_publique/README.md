# US4 - Etude de sante publique

Analyse exploratoire des donnees FAO pour evaluer la situation de sous-nutrition et la disponibilite alimentaire mondiale, avec un focus sur l'annee 2017.

## Contexte

Ce projet s'inscrit dans un cas d'usage data analyst orientee sante publique.
L'objectif est de transformer des jeux de donnees heterogenes en constats quantifies utiles a la decision.

Sources exploitees dans l'etude:

- population.csv
- dispo_alimentaire.csv
- aide_alimentaire.csv
- sous_nutrition.csv

## Objectif metier

Repondre a des questions de pilotage alimentaire a l'echelle internationale:

- quelle est la proportion de population en sous-nutrition,
- combien de personnes pourraient etre nourries selon differents besoins caloriques,
- quelle est la part de la disponibilite interieure orientee vers l'alimentation humaine, animale, les pertes et les autres usages.

## Perimetre des donnees et hypotheses

- Perimetre temporel principal: annee 2017.
- Granularite: pays/zone, avec regroupement complementaire par continent.
- Harmonisation des unites: conversions realisees pour rendre les comparaisons coherentes (ex. milliers de tonnes vers kg).
- Scenarios nutritionnels compares: 1500, 2500 et 3000 kcal/jour/personne.

## Methode

1. Chargement et controle des donnees (types, dimensions, valeurs manquantes).
2. Nettoyage/standardisation (renommage de colonnes, conversions d'unites, gestion des NaN).
3. Jointures entre jeux de donnees (population, sous-nutrition, disponibilite alimentaire).
4. Calcul d'indicateurs metiers:
	- proportion de sous-nutrition,
	- couverture theorique alimentaire,
	- couverture theorique d'origine vegetale,
	- repartition de la disponibilite interieure.
5. Restitution via tableaux de synthese et visualisations (camemberts, tableaux scenarios).

## Resultats et livrables

- Notebook d'analyse complet (import, preparation, analyses, visualisations).
- Estimation de la population en sous-nutrition sur le perimetre 2017.
- Simulations de couverture alimentaire sur trois hypotheses caloriques.
- Analyse de la part vegetale et des usages de la disponibilite interieure.
- Support de presentation du projet pour synthese orale.

## Limites et suites

- Le mapping pays-continent est construit manuellement dans le notebook et peut etre industrialise.
- Certaines hypotheses nutritionnelles restent simplificatrices et peuvent etre affinees par profil de population.
- Une etape suivante pertinente serait la creation d'un tableau de bord interactif pour comparer les regions dans le temps.

## Preuve de competences

### Resultats de veille metier

- Veille sur les enjeux de securite alimentaire: sous-nutrition, disponibilite, pertes et arbitrages d'usage.
- Traduction des enjeux en indicateurs actionnables: proportion sous-nutrie, couverture theorique, repartition des usages.
- Apport metier: meilleure lisibilite des leviers potentiels (alimentation humaine, pertes, autres usages).

### Resultats de veille technologique

- Veille sur les bonnes pratiques d'analyse exploratoire sous Python (pandas, nettoyage, jointures, controle qualite).
- Choix retenus: pipeline reproductible par etapes, conversion systematique des unites, visualisations de synthese.
- Apport technique: fiabilisation des comparaisons et restitution plus claire pour un public non technique.

### Tracabilite des preuves

- Competence: preparer des donnees heterogenes | Action: nettoyage, renommage, conversions | Preuve: notebook assets/Template+Férial+V1.ipynb.
- Competence: produire des indicateurs metiers | Action: calcul sous-nutrition et scenarios de couverture | Preuve: sections Etape 3 du notebook.
- Competence: communiquer une analyse data | Action: formalisation d'un support de restitution | Preuve: assets/Zamoun_Férial_1_presentation_112025.pdf.

## Ressources du projet

- Notebook principal: assets/Template+Férial+V1.ipynb
- Presentation: assets/Zamoun_Férial_1_presentation_112025.pdf

## Auteur

Ferial Zamoun
Formation Data Analyst - GRETA Promo 2025
Objectif: alternance en data
