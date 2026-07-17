---
layout: default
title: "Mini formation metiers - Partie 1"
---

# Mini formation metiers - Partie 1

## Objectif

Permettre a un lecteur non technique de lire le dashboard dans le bon ordre: detecter, expliquer, prioriser, decider.

## Modules proposes

1. Lire le statut qualite des donnees (ce qui est fiable, ce qui est a verifier).
2. Identifier les risques business immediats (marge negative, incoherence prix).
3. Comprendre les anomalies multivariees (Isolation Forest) et leur explication (SHAP).
4. Utiliser la priorisation avancee (K-Means/kNN) pour planifier les actions de second niveau.
5. Traduire les alertes en decisions metier et en suivi CODIR.

## Script de lecture en 90 secondes

- Etape 1: verifier le bloc Qualite.
- Etape 2: lire le Top prioritaire des produits a corriger.
- Etape 3: consulter le scatter anomalies et la justification SHAP.
- Etape 4: utiliser la segmentation/rarete pour ordonner le backlog d investigation.
- Etape 5: exporter la liste d actions pour la reunion CODIR.

## Message metier type

Notre outil detecte automatiquement les produits vendus a perte ou incoherents, explique pourquoi ils sont signales, puis les classe par priorite d action.

## Usage portfolio

Cette fiche sert de passerelle entre le notebook technique, le dashboard et la decision operationnelle.

## Preuves associees

- [README.md](README.md)
- [Dashboard KPI](output/captures/05_kpi_dashboard_phase2.png)
- [README du portfolio](README.md)