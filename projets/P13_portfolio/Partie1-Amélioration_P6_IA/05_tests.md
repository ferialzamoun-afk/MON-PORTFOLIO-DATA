---
layout: default
title: "Tests et validations - Partie 1"
---

# Tests et validations - Partie 1

## Objectif

Montrer comment les hypotheses ont ete validees dans une logique dashboard: qualite, detection, explicabilite, priorisation.

## Tests menes

- Audit du notebook initial et verification de reproductibilite.
- Validation Pandera des regles critiques (prix, marge, stock, coherence achat/vente).
- Verification des alertes statistiques (Z-score/IQR, Isolation Forest).
- Verification de l explicabilite (SHAP) pour les produits prioritaires.
- Verification de la priorisation avancee (K-Means/kNN) en appui du backlog.
- Validation de la restitution metier dans le dashboard.

## Mode de restitution Pandera

- Execution: Pandera est execute dans le notebook en arriere-plan pour valider les regles de qualite.
- Affichage: le dashboard n'affiche pas le code technique ni les tables brutes de failure cases.
- Restitution visible: un resume metier est affiche (statut OK/Alerte/Indisponible + nombre de violations).
- Traçabilite: les details techniques restent documentes dans la documentation projet et rejouables dans le notebook.

## Articulation Pandera et Great Expectations

- Pandera est utilise en controle amont: il securise les donnees avant calcul des scores et priorites.
- Great Expectations est utilise en controle aval: il securise la publication et la traçabilite des lots.
- Decision de blocage:
	- Echec Pandera => on corrige la donnee avant de continuer l'analyse.
	- Echec GE => on bloque la diffusion externe tant que les expectations ne sont pas conformes.
- Benefice metier: les equipes traitent des alertes fiables, et la publication reste gouvernee par des regles qualite explicites.

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

- **Contexte** : Besoin de valider vite sans casser le flux notebook existant.
- **Hypothese IA** : Une sequence en 3 etapes (schema, anomalies, restitution) couvre l'essentiel pour le lot en cours.
- **Options considerees** :
	1. Tests complets type framework lourd des la premiere iteration.
	2. Sequence progressive Pandas/Pandera + controles statistiques de base.
- **Decision humaine** : Option 2 retenue.
- **Justification** : Delai court, meilleure lisibilite pour la soutenance, integration immediate dans le notebook.
- **Impact** : Tests rejouables, etat des controles plus clair pour le lecteur metier.

### Entree 2 - Validation BC05 en conditions reelles

- **Contexte** : Prouver la valeur statistique sans sur-complexifier l'implementation.
- **Hypothese IA** : IF + SHAP couvre la decision immediate; K-Means/kNN complete la priorisation.
- **Options considerees** :
	1. Introduire directement plusieurs modeles en parallele.
	2. Stabiliser d'abord les alertes statistiques de base.
- **Decision humaine** : Option 2 retenue.
- **Justification** : separation nette entre alerte critique immediate et priorisation de second niveau.
- **Impact** : traçabilite claire de la chaine Qualite -> Detection -> Explication -> Decision.

## Preuves associees

- [README.md](README.md)
- [Dashboard KPI](output/captures/05_kpi_dashboard_phase2.png)
- [Notebook BC05 - section globale](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05)
- [Notebook BC05 - 9.1 Immediate](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IMMEDIATE)
- [Notebook BC05 - 9.2 Isolation Forest](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IFOREST)
- [Notebook BC05 - 9.3 K-Means et kNN](https://nbviewer.org/github/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P13_portfolio/Partie1-Am%C3%A9lioration_P6_IA/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-KMEANS-KNN)
- [Mode d'emploi dashboard](09_mode_emploi_dashboard.html)
- [README du portfolio](README.md)