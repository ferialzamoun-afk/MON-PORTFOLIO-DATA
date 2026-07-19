---
layout: default
title: "Tests et validations - Partie 1"
---

# Tests et validations - Partie 1

## Objectif

Montrer comment les hypotheses ont ete validees dans une logique dashboard: qualite, detection, explicabilite, priorisation.

## Tests menes

| Test | Objet |
|---|---|
| Audit notebook | Verification de reproductibilite du notebook initial. |
| Pandera | Validation des regles critiques (prix, marge, stock, coherence achat/vente). |
| Alertes statistiques | Verification des alertes (Z-score/IQR, Isolation Forest). |
| Explicabilite | Verification de SHAP pour les produits prioritaires. |
| Priorisation | Verification de K-Means/kNN en appui du backlog, sans passage critique automatique. |
| Restitution dashboard | Validation de la lecture metier dans le dashboard. |

## Mode de restitution Pandera

| Aspect | Regle de restitution |
|---|---|
| Execution | Pandera est execute dans le notebook en arriere-plan pour valider les regles de qualite. |
| Affichage | Le dashboard n'affiche pas le code technique ni les tables brutes de failure cases. |
| Restitution visible | Un resume metier est affiche (statut OK/Alerte/Indisponible + nombre de violations). |
| Traçabilite | Les details techniques restent documentes dans la documentation projet et rejouables dans le notebook. |

## Articulation Pandera et Great Expectations

| Niveau | Role |
|---|---|
| Pandera | Controle amont: securise les donnees avant calcul des scores et priorites. |
| Great Expectations | Controle aval: securise la publication et la traçabilite des lots. |

| Situation | Action |
|---|---|
| Echec Pandera | Corriger la donnee avant de continuer l'analyse. |
| Echec GE | Bloquer la diffusion externe tant que les expectations ne sont pas conformes. |

| Benefice metier | Effet attendu |
|---|---|
| Publication gouvernee | Les equipes traitent des alertes fiables, avec des regles qualite explicites. |

## Grille de validation dashboard

| Etape | Question de validation | Statut attendu |
|---|---|---|
| Qualite | Les donnees critiques sont-elles conformes ? | OK ou Alerte explicite |
| Detection | Les produits a risque sont-ils identifies ? | Oui, avec score |
| Explication | Les alertes sont-elles compréhensibles ? | Oui, via SHAP |
| Priorisation | L ordre de traitement est-il explicite ? | Oui, top produits |
| Decision | Une action concrete est-elle derivable ? | Oui, liste exportable |

## Journal IA - traces de validation

### Entree 1 - Sequence de tests rapide et fiable

| Champ | Contenu |
|---|---|
| Contexte | Besoin de valider vite sans casser le flux notebook existant. |
| Hypothese IA | Une sequence en 3 etapes (schema, anomalies, restitution) couvre l'essentiel pour le lot en cours. |
| Options considerees | 1. Tests complets type framework lourd des la premiere iteration. 2. Sequence progressive Pandas/Pandera + controles statistiques de base. |
| Decision humaine | Option 2 retenue. |
| Justification | Delai court, meilleure lisibilite pour la soutenance, integration immediate dans le notebook. |
| Impact | Tests rejouables, etat des controles plus clair pour le lecteur metier. |

### Entree 2 - Validation BC05 en conditions reelles

| Champ | Contenu |
|---|---|
| Contexte | Prouver la valeur statistique sans sur-complexifier l'implementation. |
| Hypothese IA | IF + SHAP couvre la decision immediate; K-Means/kNN complete la priorisation. |
| Options considerees | 1. Introduire directement plusieurs modeles en parallele. 2. Stabiliser d'abord les alertes statistiques de base. |
| Decision humaine | Option 2 retenue. |
| Justification | Separation nette entre alerte critique immediate et priorisation de second niveau. |
| Impact | Traçabilite claire de la chaine Qualite -> Detection -> Explication -> Decision. |

### Entree 3 - Validation de la matrice decisionnelle stricte

| Champ | Contenu |
|---|---|
| Contexte | Les premiers compteurs donnaient trop de critiques lorsque kNN/K-Means entraient dans le score critique. |
| Hypothese IA | Separer `critical_score` et `surveillance_score` rend la priorisation plus robuste. |
| Decision humaine | `Critique` = IF + SHAP + impact ; kNN/K-Means = surveillance. |
| Resultat | Matrice complete : 1 critique, 172 a surveiller, 652 normaux. Dashboard filtre courant : 1 critique, 152 a surveiller, 560 normaux. |
| Impact | La short-list critique redevient actionnable sans perdre les signaux rares dans le backlog. |

## Preuves associees

| Preuve | Lien |
|---|---|
| README | [Ouvrir](https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/README.md) |
| Dashboard KPI | [Ouvrir](output/captures/05_kpi_dashboard_phase2.png) |
| Notebook BC05 - section globale | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05) |
| Notebook BC05 - 9.1 Immediate | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IMMEDIATE) |
| Notebook BC05 - 9.2 Isolation Forest | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IFOREST) |
| Notebook BC05 - 9.3 K-Means et kNN | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-KMEANS-KNN) |
| Mode d'emploi dashboard | [Ouvrir](https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/assets/Guide-Utilisateur-Dashboard-Ventes-and-Stocks.pdf) |
| README du portfolio | [Ouvrir](https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/README.md) |