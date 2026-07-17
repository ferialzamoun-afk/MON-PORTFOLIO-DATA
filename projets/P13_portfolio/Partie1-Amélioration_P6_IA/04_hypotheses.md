---
layout: default
title: "Hypotheses de travail - Partie 1"
---

# Hypotheses de travail - Partie 1

## Objectif

Rendre explicites les hypotheses qui guident la chaine de decision du dashboard.

## Hypotheses retenues

- Les controles qualite en amont reduisent fortement les faux signaux d anomalies.
- Les anomalies les plus critiques combinent prix et marge, pas une seule variable.
- Une alerte sans explication est peu actionnable; SHAP est donc necessaire pour la lecture metier.
- K-Means/kNN apportent de la priorisation, mais ne remplacent pas Isolation Forest pour la correction immediate.
- Le dashboard doit privilegier les decisions de court terme avant l optimisation de moyen terme.

## Journal IA - traces d'hypotheses

### Entree 1 - Fiabiliser sans reconstruire

- **Contexte** : Le notebook P6 initial etait exploitable mais trop dense pour une restitution claire.
- **Hypothese IA** : Une refonte progressive (et non une reconstruction totale) permet de gagner en qualite et en lisibilite.
- **Options considerees** :
	1. Repartir d'une page blanche.
	2. Ameliorer l'existant en documentant chaque arbitrage.
- **Decision humaine** : Option 2 retenue.
- **Justification** : Meilleure maitrise du risque, conservation de la logique metier deja validee.
- **Impact** : Trajectoire d'amelioration measurable (avant/apres) et plus defendable en soutenance.

### Entree 2 - Priorite aux hypotheses BC05 utiles au metier

- **Contexte** : Besoin de renforcer BC05 sans alourdir excessivement le lot courant.
- **Hypothese IA** : Les gains les plus rapides viennent d'un noyau progressif: controle qualite -> Isolation Forest -> SHAP.
- **Options considerees** :
	1. Introduire tout de suite plusieurs methodes avancees.
	2. Prioriser les hypotheses a forte valeur immediate pour notebook + Streamlit.
- **Decision humaine** : Option 2 retenue.
- **Justification** : Delai court, lisibilite metier, decisions actionnables des la premiere version dashboard.
- **Impact** : Differenciation claire entre priorite immediate (IF + SHAP) et priorisation avancee (K-Means/kNN).

### Entree 3 - Arbitrage methodes pour la decision

- **Contexte** : Plusieurs modeles disponibles dans BC05 (IF, K-Means, kNN).
- **Hypothese IA** : Le socle le plus defendable pour decider vite est Isolation Forest + SHAP, puis K-Means/kNN en renfort.
- **Options considerees** :
	1. Basculer la priorite sur K-Means/kNN.
	2. Garder IF + SHAP comme socle et utiliser K-Means/kNN pour le backlog.
- **Decision humaine** : Option 2 retenue.
- **Justification** : meilleure explicabilite immediate pour le CODIR.
- **Impact** : storytelling dashboard plus clair et decisions plus robustes.

## Preuves associees

- [README.md](README.md)
- [Dashboard KPI](output/captures/05_kpi_dashboard_phase2.png)
- [README du portfolio](README.md)