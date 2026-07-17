---
layout: default
title: "Veille metier et technologique - Partie 1"
---

# Veille metier et technologique - Partie 1

## Objectif

Montrer comment la veille a structure une logique de decision exploitable dans le dashboard: detecter, expliquer, prioriser, decider.

## Storytelling cible du dashboard

1. Detecter les cas a risque (regles qualite + anomalies multivariees).
2. Expliquer les cas prioritaires (SHAP + lecture metier).
3. Prioriser les actions (criticite business puis rarete statistique).
4. Decider au niveau CODIR (liste de produits a corriger, segmenter, suivre).

## Synthese de la veille technologique - Projet Bottleneck

Objectif de la veille: remplacer les controles manuels par des solutions automatisables, explicables et proportionnees au contexte P6 (volumes limites, lisibilite metier, delai court).

| Axe | Besoin | Solution cible | Niveau d'integration recommande |
|---|---|---|---|
| 1. Validation automatique | Bloquer les incoherences des l'import ERP/Web | Pandera + regles de controle Pandas | Priorite haute |
| 2. Detection intelligente | Remonter les cas critiques invisibles en univarie | Z-score/IQR + Isolation Forest | Priorite haute |
| 3. Explications claires | Justifier les alertes en langage metier | SHAP + regles metier explicites | Priorite haute |
| 4. Segmentation objective | Regrouper les profils produits pour actionner les leviers | K-Means (variables standardisees) | Priorite moyenne |
| 5. Priorisation locale | Classer les cas rares a traiter ensuite | kNN (score de rarete locale) | Priorite moyenne |
| 6. Aide a la decision | Recommandations de prix basees sur l'elasticite | Regression log-log | Priorite basse (lot suivant) |

## Choix retenu pour le lot courant

- Socle decision immediate: Pandera + Z-score/IQR + Isolation Forest + SHAP.
- Renfort de priorisation: K-Means et kNN, apres stabilisation des alertes critiques.
- Logique produit: ne pas remplacer le socle explicable, mais le completer.

## Conclusion transitoire

Le dashboard suit une chaine simple et defendable:

- qualite des donnees (Pandera),
- detection des risques (Isolation Forest),
- explicabilite (SHAP),
- priorisation avancee (K-Means/kNN).

Cette trajectoire maintient un compromis solide entre delai court, lisibilite CODIR et robustesse methodologique.

## Preuves associees

- [Cahier des charges fonctionnel](02_cahier_des_charges_fonctionnel.html)
- [Hypotheses de travail](04_hypotheses.html)
- [Tests et validations](05_tests.html)
- [Resultats](06_resultats.html)
- [Decisions](08_decisions.html)