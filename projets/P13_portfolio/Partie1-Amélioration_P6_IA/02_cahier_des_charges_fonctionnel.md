---
layout: default
title: "Cahier des charges fonctionnel - Partie 1"
---

# Cahier des charges fonctionnel - Partie 1

## Objectif

Formaliser le besoin metier et traduire le projet P6 en un dashboard de decision court terme pour le CODIR.

## Besoin formule

- Reconciler ERP, Web et liaison sans perte de tracabilite.
- Transformer les controles data en decisions operationnelles priorisees.
- Garantir une explicabilite lisible des alertes IA.

## Storytelling fonctionnel impose

1. Detecter: controles qualite + anomalies critiques.
2. Expliquer: raisons des alertes (lecture SHAP et variables metier).
3. Prioriser: top produits a corriger maintenant.
4. Decider: actions CODIR et plan de suivi.

## Exigences fonctionnelles dashboard

- Bloc Qualite: statut global des controles Pandera et nombre d anomalies bloquantes.
- Bloc Risque immediate: produits a marge negative ou incoherence prix achat/vente.
- Bloc Anomalies multivariees: score Isolation Forest + explication SHAP.
- Bloc Priorisation: segmentation K-Means et score kNN pour file d investigation.
- Bloc Decision: export des top produits a traiter et trace des regles appliquees.

## Criteres de reussite

- Le lecteur metier comprend en moins de 2 minutes quoi corriger en priorite.
- Chaque alerte majeure est reliee a une justification interpretable.
- La priorisation est reproductible entre deux executions.
- Les regles qualite sont explicites et auditables.

## Livrables attendus

- Notebook ameliore et reproductible.
- Documentation de cadrage, tests, resultats et limites.
- Synthese claire exploitable dans le portfolio.
- Dashboard KPI lisible pour la lecture CODIR.
- Exports operationnels (top anomalies, justifications, priorites).

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
| T17 | Executer 9.3 renfort BC05 (K-Means + kNN) | [~] |
| T18 | Synchroniser les taches dans GitHub Projects | [~] |
| T19 | Fixer les seuils metier BC05 | [~] |
| T20 | Integrer la synthese BC05 dans le dashboard | [~] |
| T21 | Mettre a jour la tracabilite IA (decisions + impacts) | [ ] |

Points de cloture avant push final:

- Finaliser les cartes encore en A faire (T12, T21) dans GitHub Project.
- Verifier les liens publics et la coherence des statuts dans les pages du portfolio.