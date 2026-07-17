---
layout: default
title: "Mode d'emploi dashboard - Partie 1"
---

# Mode d'emploi dashboard - Partie 1

## Objectif

Fournir une lecture utilisateur simple du dashboard pour passer rapidement de la qualite des donnees a la decision metier.

## Parcours recommande

1. Ouvrir la page **Reporting qualite**.
2. Verifier le statut global des controles (OK / Alerte / Indisponible).
3. Ouvrir le **Tableau de bord decisionnel**.
4. Lire les priorites `Critique`, `A surveiller`, `Normal`.
5. Exporter la liste d'action.

## Lecture des priorites

- `Critique` : traitement immediat (24-48h).
- `A surveiller` : suivi hebdomadaire et prevention d'escalade.
- `Normal` : surveillance standard.

## Logique metier resumee

- Qualite amont : controles data + Pandera.
- Detection : Isolation Forest.
- Explication : SHAP.
- Priorisation avancee : K-Means/kNN en renfort.

Le principe est de garder une decision explicable et actionnable, sans noyer l'utilisateur dans les details techniques.

## Bonnes pratiques d'usage

- Toujours verifier la qualite avant d'interpreter les alertes.
- Appliquer les filtres metier avant export.
- Prioriser les actions sur les produits a plus fort impact business.

## Lien vers le dashboard

- Dashboard Streamlit : [Ouvrir le dashboard](https://p6-dashboard-wdcn5o8grt39nqtim6mgym.streamlit.app/)

## Preuves associees

- [Tests et validations](05_tests.html)
- [Resultats](06_resultats.html)
- [Decisions](08_decisions.html)
