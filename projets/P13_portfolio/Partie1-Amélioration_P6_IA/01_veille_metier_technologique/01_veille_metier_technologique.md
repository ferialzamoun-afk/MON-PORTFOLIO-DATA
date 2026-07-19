---
layout: default
title: "Veille metier et technologique - Partie 1"
---

# Veille metier et technologique - Partie 1

## Objectif

Montrer comment la veille a structure une logique de decision exploitable dans le dashboard: detecter, expliquer, prioriser, decider.

## Storytelling cible du dashboard

| Etape | Role dans la lecture metier |
|---|---|
| Detecter | Repérer les cas a risque via les regles qualite et les anomalies multivariees. |
| Expliquer | Rendre les cas prioritaires compréhensibles avec SHAP et une lecture metier. |
| Prioriser | Classer les actions selon la criticite business puis la rarete statistique. |
| Decider | Produire une liste de produits a corriger, segmenter et suivre au niveau CODIR. |

## Synthese de la veille technologique - Projet Bottleneck

Objectif de la veille: remplacer les controles manuels par des solutions automatisables, explicables et proportionnees au contexte P6 (volumes limites, lisibilite metier, delai court).

| Axe | Besoin | Solution cible | Niveau d'integration recommande |
|---|---|---|---|
| 1. Validation automatique | Bloquer les incoherences des l'import ERP/Web | Pandera + regles de controle Pandas | Priorite haute |
| 2. Detection intelligente | Remonter les cas critiques invisibles en univarie | Z-score/IQR + Isolation Forest | Priorite haute |
| 3. Explications claires | Justifier les alertes en langage metier | SHAP + regles metier explicites | Priorite haute |
| 4. Segmentation objective | Regrouper les profils produits pour actionner les leviers | K-Means (variables standardisees) | Priorite moyenne |
| 5. Priorisation locale | Classer les cas rares a traiter ensuite | kNN non supervise (score de rarete locale) | A surveiller |
| 6. Aide a la decision | Recommandations de prix basees sur l'elasticite | Regression log-log | Priorite basse (lot suivant) |

## Choix retenu pour le lot courant

| Axe | Choix retenu |
|---|---|
| Socle decision immediate | Pandera + Z-score/IQR + Isolation Forest + SHAP |
| Renfort de priorisation | K-Means et kNN, apres stabilisation des alertes critiques, sans declenchement critique automatique |
| Logique produit | Ne pas remplacer le socle explicable, mais le completer |

## Conclusion transitoire

| Brique | Contribution |
|---|---|
| Qualite des donnees | Pandera |
| Detection des risques | Isolation Forest |
| Explicabilite | SHAP |
| Priorisation avancee | K-Means/kNN |

Cette trajectoire maintient un compromis solide entre delai court, lisibilite CODIR et robustesse methodologique.

## Regle BC05 retenue

| Niveau | Score | Usage |
|---|---|---|
| Critique | `critical_score >= 0.65` | IF + SHAP + impact business pour une short-list actionnable. |
| A surveiller | `surveillance_score >= 0.45` | IF + kNN + K-Means + SHAP + impact business pour le backlog. |

kNN et K-Means ordonnent les investigations, mais ne suffisent plus a declencher une urgence critique.

## Preuves associees

| Document | Lien |
|---|---|
| Cahier des charges fonctionnel | [Ouvrir](02_cahier_des_charges_fonctionnel.html) |
| Hypotheses de travail | [Ouvrir](04_hypotheses.html) |
| Tests et validations | [Ouvrir](05_tests.html) |
| Resultats | [Ouvrir](06_resultats.html) |
| Decisions | [Ouvrir](08_decisions.html) |