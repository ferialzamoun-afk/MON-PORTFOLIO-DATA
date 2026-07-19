---
layout: default
title: "Cahier des charges fonctionnel - Partie 1"
---

# Cahier des charges fonctionnel - Partie 1

## Objectif

Formaliser le besoin metier et traduire le projet P6 en un dashboard de decision court terme pour le CODIR.

## Besoin formule

| Besoin | Formulation |
|---|---|
| Traçabilité | Reconciler ERP, Web et liaison sans perte de tracabilite. |
| Decision | Transformer les controles data en decisions operationnelles priorisees. |
| Explicabilite | Garantir une explicabilite lisible des alertes IA. |

## Storytelling fonctionnel impose

| Etape | Objectif |
|---|---|
| Detecter | Controles qualite + anomalies critiques |
| Expliquer | Raisons des alertes (lecture SHAP et variables metier) |
| Prioriser | Top produits a corriger maintenant |
| Decider | Actions CODIR et plan de suivi |

## Exigences fonctionnelles dashboard

| Bloc | Contenu attendu |
|---|---|
| Qualite | Statut global des controles Pandera et nombre d anomalies bloquantes |
| Risque immediate | Produits a marge negative ou incoherence prix achat/vente |
| Anomalies multivariees | Score Isolation Forest + explication SHAP |
| Priorisation | Segmentation K-Means et score kNN pour file d investigation, sans passage critique automatique |
| Decision | Export des top produits a traiter et trace des regles appliquees |

## Regle de priorisation retenue

| Priorite | Regle |
|---|---|
| Critique | `critical_score >= 0.65` : IF + SHAP + impact business. |
| A surveiller | `surveillance_score >= 0.45` : IF + kNN + K-Means + SHAP + impact business. |
| Normal | Sous les seuils, suivi standard. |

Le kNN est interprete comme une rarete locale non supervisee : il priorise les investigations mais ne remplace pas la validation metier.

## Criteres de reussite

| Critere | Cible |
|---|---|
| Compréhension rapide | Le lecteur metier comprend en moins de 2 minutes quoi corriger en priorite. |
| Justification | Chaque alerte majeure est reliee a une justification interpretable. |
| Reproductibilite | La priorisation est reproductible entre deux executions. |
| Auditabilite | Les regles qualite sont explicites et auditables. |

## Livrables attendus

| Livrable | Attendu |
|---|---|
| Notebook | Ameliore et reproductible |
| Documentation | Cadrage, tests, resultats et limites |
| Synthese | Claire et exploitable dans le portfolio |
| Dashboard | Lisible pour la lecture CODIR |
| Exports | Top anomalies, justifications, priorites |

## Preuves associees

- [README.md](README.md)
- [Dashboard KPI](output/captures/05_kpi_dashboard_phase2.png)
- [README du portfolio](README.md)

## Suivi des taches (passe pre-commit/push)

Etat aligne avec la documentation projet P13 (controle du 2026-07-18):

| Tache | Description | Statut |
|---|---|---|
| T09 | Preparer les preuves pour le portfolio | [x] |
| T11 | Nettoyer le depot GitHub avant publication | [~] |
| T12 | Nettoyer le depot GitHub + setup security scanning | [~] |
| T15 | Valider metier les alertes actionnables (top 20) | [~] |
| T17 | Executer 9.3 renfort BC05 (K-Means + kNN) | [x] |
| T18 | Synchroniser les taches dans GitHub Projects | [~] |
| T19 | Fixer les seuils metier BC05 | [x] |
| T20 | Integrer la synthese BC05 dans le dashboard | [x] |
| T21 | Mettre a jour la tracabilite IA (decisions + impacts) | [ ] |

Points de cloture avant push final:

| Point | Action |
|---|---|
| Taches restantes | Finaliser les cartes encore en A faire (T12, T21) dans GitHub Project. |
| Verification finale | Verifier les liens publics et la coherence des statuts dans les pages du portfolio. |