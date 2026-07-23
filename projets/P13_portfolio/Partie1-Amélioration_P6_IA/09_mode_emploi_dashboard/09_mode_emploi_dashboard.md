---
layout: default
title: "Mode d'emploi dashboard - Partie 1"
---

# Mode d'emploi dashboard - Partie 1

## Objectif

Fournir une lecture utilisateur simple du dashboard pour passer rapidement de la qualite des donnees a la decision metier.

## Parcours recommande

| Etape | Action |
|---|---|
| 1 | Ouvrir la page **Reporting qualite**. |
| 2 | Verifier le statut global des controles (OK / Alerte / Indisponible). |
| 3 | Ouvrir le **Tableau de bord decisionnel**. |
| 4 | Lire les priorites `Critique`, `A surveiller`, `Normal`. |
| 5 | Exporter la liste d'action. |

## Lecture des priorites

| Priorite | Interpretation |
|---|---|
| `Critique` | Traitement immediat (24-48h), base sur `critical_score` : IF + SHAP + impact business. |
| `A surveiller` | Suivi hebdomadaire et prevention d'escalade, base sur `surveillance_score` : IF + kNN + K-Means + SHAP + impact. |
| `Normal` | Surveillance standard. |

## Logique metier resumee

| Brique | Role |
|---|---|
| Qualite amont | Controles data + Pandera. |
| Detection | Isolation Forest. |
| Explication | SHAP. |
| Criticite stricte | IF + SHAP + impact business. |
| Priorisation avancee | K-Means/kNN en renfort pour le backlog de surveillance. |

Le principe est de garder une decision explicable et actionnable, sans noyer l'utilisateur dans les details techniques.

## Point de vigilance kNN

kNN est non supervise : il mesure une rarete locale, pas une erreur certaine. Il aide a ordonner les investigations dans `A surveiller`, mais ne declenche pas seul une priorite `Critique`.

## Bonnes pratiques d'usage

| Bonne pratique | Pourquoi |
|---|---|
| Verifier la qualite | Eviter d'interpreter des alertes sur des donnees non fiables. |
| Appliquer les filtres metier | Restreindre la lecture au bon perimetre. |
| Prioriser l'impact business | Traiter d'abord les produits a plus fort enjeu. |

## Lien vers le dashboard

| Element | Lien |
|---|---|
| Dashboard Streamlit | [Ouvrir le dashboard](https://p6-dashboard-wdcn5o8grt39nqtim6mgym.streamlit.app/) |

## Preuves associees

| Preuve | Lien |
|---|---|
| Tests et validations | [Ouvrir](05_tests.html) |
| Resultats | [Ouvrir](06_resultats.html) |
| Decisions | [Ouvrir](08_decisions.html) |
