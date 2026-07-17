---
layout: default
title: "Resultats - Partie 1"
---

# Resultats - Partie 1

## Objectif

Synthetiser les gains visibles du projet P6 ameliore et leur traduction en decisions operationnelles via le dashboard.

## Resultats cles

- Workflow clarifie: Qualite -> Detection -> Explication -> Priorisation -> Decision.
- 18 controles qualite visibles et exploitables metier.
- Detection multivariee operationnelle avec Isolation Forest.
- Explicabilite des alertes via SHAP pour les cas prioritaires.
- Renfort de priorisation via K-Means/kNN sans remplacer le socle explicable.

## Restitution Pandera (lecture metier)

- Le code Pandera est masque dans la restitution principale pour conserver une lecture orientee decision.
- Le resultat affiche est un resume: statut de validation (OK/Alerte/Indisponible) et volume de violations.
- Les details techniques Pandera restent disponibles dans les artefacts de test et la version complete du notebook.

## Journal IA - traces de resultats

### Entree 1 - Lecture des gains avant/apres

- **Contexte** : Transformer des ameliorations techniques en preuves evaluables.
- **Hypothese IA** : Le trio cellules/temps/controles est le plus convaincant pour la soutenance.
- **Options considerees** :
	1. Presenter une liste exhaustive de metriques techniques.
	2. Prioriser des indicateurs peu nombreux mais directement lisibles.
- **Decision humaine** : Option 2 retenue.
- **Justification** : Lisibilite forte pour recruteur, jury et lecture portfolio.
- **Impact** : Argumentaire plus clair sur la valeur du P6 ameliore.

### Entree 2 - Resultats BC05 valorises

- **Contexte** : Le BC05 devait passer de "indirect" a "direct" dans la narration.
- **Hypothese IA** : Le trio IF + SHAP + priorisation K-Means/kNN renforce la credibilite et l actionnabilite.
- **Options considerees** :
	1. Rester sur une mention generale des "analyses statistiques".
	2. Relier chaque resultat BC05 a une methode identifiable.
- **Decision humaine** : Option 2 retenue.
- **Justification** : preuves mieux alignees avec le besoin CODIR de priorisation concrete.
- **Impact** : BC05 defendable sur le plan statistique et operationnel.

### Entree 3 - Focus prompts BC05

- **Contexte** : Prouver l'effort IA reel sur l'objectif dashboard anomalies.
- **Decision humaine** : Isoler un comptage cible des prompts utiles a BC05.
- **Resultat** : 13 prompts directement lies au flux Detecter -> Expliquer -> Prioriser -> Decider.
- **Impact** : meilleure tracabilite entre assistance IA et valeur metier livree.

## Conclusion transitoire pour le dashboard

- Court terme: corriger en priorite les marges negatives et incoherences prix achat/vente.
- Court terme: appuyer ces corrections par l explication SHAP des cas signales.
- Moyen terme: utiliser K-Means/kNN pour structurer le backlog d optimisation (segmentation, rarete locale, politique stock/prix).
- Gouvernance: maintenir Pandera comme garde-fou d entree pour limiter la propagation des erreurs.

## Preuves associees

- [Dashboard KPI](output/captures/05_kpi_dashboard_phase2.png)
- [Notebook BC05 - section globale](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05)
- [Notebook BC05 - 9.1 Immediate](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IMMEDIATE)
- [Notebook BC05 - 9.2 Isolation Forest](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IFOREST)
- [Notebook BC05 - 9.3 K-Means et kNN](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-KMEANS-KNN)
- [Mode d'emploi dashboard](09_mode_emploi_dashboard.html)
- [GitHub Project - Kanban](https://github.com/users/ferialzamoun-afk/projects/2/views/1)
- [GitHub Project - Vue portfolio](https://github.com/users/ferialzamoun-afk/projects/2/views/3)
- [README du portfolio](README.md)