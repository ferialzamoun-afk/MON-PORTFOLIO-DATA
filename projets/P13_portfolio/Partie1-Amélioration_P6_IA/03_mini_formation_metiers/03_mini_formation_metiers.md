---
layout: default
title: "Mini formation metiers - Partie 1"
---

# Mini formation metiers - Partie 1

## Objectif

Permettre a un lecteur non technique de lire le dashboard dans le bon ordre: detecter, expliquer, prioriser, decider.

## Modules proposes

| Module | Objectif |
|---|---|
| 1 | Lire le statut qualite des donnees (ce qui est fiable, ce qui est a verifier). |
| 2 | Identifier les risques business immediats (marge negative, incoherence prix). |
| 3 | Comprendre les anomalies multivariees (Isolation Forest) et leur explication (SHAP). |
| 4 | Utiliser la priorisation avancee (K-Means/kNN) pour planifier les actions de second niveau, sans confondre rarete statistique et urgence critique. |
| 5 | Traduire les alertes en decisions metier et en suivi CODIR. |

## Script de lecture en 90 secondes

| Etape | Action |
|---|---|
| 1 | Verifier le bloc Qualite. |
| 2 | Lire le Top prioritaire des produits a corriger. |
| 3 | Consulter le scatter anomalies et la justification SHAP. |
| 4 | Utiliser la segmentation/rarete pour ordonner le backlog d investigation. |
| 5 | Exporter la liste d actions pour la reunion CODIR. |

## Message metier type

Notre outil detecte automatiquement les produits vendus a perte ou incoherents, explique pourquoi ils sont signales, puis les classe par priorite d action.

## Lecture des priorites IA

| Priorite | Lecture metier |
|---|---|
| Critique | Short-list stricte : IF + SHAP + impact business, action sous 24-48h. |
| A surveiller | Produits rares, eloignes de leur cluster ou statistiquement atypiques a suivre au cycle hebdomadaire. |
| Normal | Suivi standard. |

## Usage portfolio

Cette fiche sert de passerelle entre le notebook technique, le dashboard et la decision operationnelle.
