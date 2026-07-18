---
layout: default
title: "Resultats - Partie 1"
---

# Resultats - Partie 1

## Objectif

Synthetiser les gains visibles du projet P6 ameliore et leur traduction en decisions operationnelles via le dashboard.

## Resultats cles

| Resultat | Detail |
|---|---|
| Workflow | Qualite -> Detection -> Explication -> Priorisation -> Decision. |
| Qualite | 18 controles visibles et exploitables metier. |
| Detection | Detection multivariee operationnelle avec Isolation Forest. |
| Explicabilite | Alertes expliquees via SHAP pour les cas prioritaires. |
| Priorisation | Renfort via K-Means/kNN pour `A surveiller`, sans remplacer le score critique explicable. |

## Restitution Pandera (lecture metier)

| Aspect | Regle de restitution |
|---|---|
| Visibilite | Le code Pandera est masque dans la restitution principale pour conserver une lecture orientee decision. |
| Resume | Le resultat affiche un statut de validation (OK/Alerte/Indisponible) et volume de violations. |
| Details techniques | Ils restent disponibles dans les artefacts de test et la version complete du notebook. |

## Journal IA - traces de resultats

### Entree 1 - Lecture des gains avant/apres

| Champ | Contenu |
|---|---|
| Contexte | Transformer des ameliorations techniques en preuves evaluables. |
| Hypothese IA | Le trio cellules/temps/controles est le plus convaincant pour la soutenance. |
| Options considerees | 1. Presenter une liste exhaustive de metriques techniques. 2. Prioriser des indicateurs peu nombreux mais directement lisibles. |
| Decision humaine | Option 2 retenue. |
| Justification | Lisibilite forte pour recruteur, jury et lecture portfolio. |
| Impact | Argumentaire plus clair sur la valeur du P6 ameliore. |

### Entree 2 - Resultats BC05 valorises

| Champ | Contenu |
|---|---|
| Contexte | Le BC05 devait passer de "indirect" a "direct" dans la narration. |
| Hypothese IA | Le trio IF + SHAP + impact business porte la criticite ; K-Means/kNN renforcent la surveillance. |
| Options considerees | 1. Rester sur une mention generale des "analyses statistiques". 2. Relier chaque resultat BC05 a une methode identifiable. |
| Decision humaine | Option 2 retenue. |
| Justification | Preuves mieux alignees avec le besoin CODIR de priorisation concrete. |
| Impact | BC05 defendable sur le plan statistique et operationnel. |

### Entree 3 - Focus prompts BC05

| Champ | Contenu |
|---|---|
| Contexte | Prouver l'effort IA reel sur l'objectif dashboard anomalies. |
| Decision humaine | Isoler un comptage cible des prompts utiles a BC05. |
| Resultat | 13 prompts directement lies au flux Detecter -> Expliquer -> Prioriser -> Decider. |
| Impact | Meilleure tracabilite entre assistance IA et valeur metier livree. |

## Conclusion transitoire pour le dashboard

| Horizon | Orientation |
|---|---|
| Court terme | Corriger en priorite les marges negatives et incoherences prix achat/vente. |
| Court terme | Appuyer ces corrections par l explication SHAP des cas signales. |
| Moyen terme | Utiliser K-Means/kNN pour structurer le backlog d optimisation (segmentation, rarete locale, politique stock/prix), sans declenchement critique automatique. |
| Gouvernance | Maintenir Pandera comme garde-fou d entree pour limiter la propagation des erreurs. |

## Resultats BC05 actualises

| Indicateur | Resultat |
|---|---|
| Alertes immediates | 36 alertes statistiques (4,36%) |
| Isolation Forest | 25 alertes multivariees |
| K-Means | 4 clusters produits |
| kNN | 42 produits rares au seuil 95e percentile |
| Matrice complete | 825 produits : 1 critique, 172 a surveiller, 652 normaux |
| Dashboard filtre courant | 713 lignes : 1 critique, 152 a surveiller, 560 normaux |

## Preuves associees

| Preuve | Lien |
|---|---|
| Dashboard KPI | [Ouvrir](output/captures/05_kpi_dashboard_phase2.png) |
| Notebook BC05 - section globale | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05) |
| Notebook BC05 - 9.1 Immediate | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IMMEDIATE) |
| Notebook BC05 - 9.2 Isolation Forest | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IFOREST) |
| Notebook BC05 - 9.3 K-Means et kNN | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-KMEANS-KNN) |
| Mode d'emploi dashboard | [Ouvrir](09_mode_emploi_dashboard.html) |
| GitHub Project - Kanban | [Ouvrir](https://github.com/users/ferialzamoun-afk/projects/2/views/1) |
| GitHub Project - Vue portfolio | [Ouvrir](https://github.com/users/ferialzamoun-afk/projects/2/views/3) |
| README du portfolio | [Ouvrir](README.md) |