---
layout: default
title: "Decisions - Partie 1"
---

# Decisions - Partie 1

## Objectif

Tracer les arbitrages qui structurent la version portfolio de la Partie 1.

## Decisions majeures

| Decision | Choix |
|---|---|
| Architecture | Ameliorer l'existant plutot que refaire tout le projet. |
| Lisibilite | Prioriser la lisibilite metier et la traçabilite pour la soutenance. |
| Court terme | Garder Pandas a court terme, documenter la trajectoire future. |
| Documentation | Faire de la documentation un livrable principal. |
| Restitution | Appuyer la restitution par un dashboard KPI deja realise. |

## Journal IA - mises a jour (Lot editorial BC05)

### Entree 1 - Positionnement BC05

| Champ | Contenu |
|---|---|
| Contexte | Le mapping global P13 affichait encore BC05 en couverture indirecte. |
| Hypothese IA | Defendre BC05 en couverture directe via un noyau statistique progressif est plus coherent avec la Partie 1. |
| Options considerees | 1. Garder BC05 indirect pour eviter une promesse trop ambitieuse. 2. Passer BC05 direct avec methodes explicites et limites documentees. |
| Decision humaine | Option 2 retenue. |
| Justification | La veille et les artefacts couvrent deja Z-score/IQR, Isolation Forest, SHAP, K-Means et kNN. |
| Impact | Message soutenance clarifie, alignement entre veille, decisions et mapping RNCP. |

### Entree 2 - Priorisation des solutions (vitesse d'integration)

| Champ | Contenu |
|---|---|
| Contexte | Besoin de solution rapide pour notebook P6 et portail Streamlit actuel. |
| Hypothese IA | L'ordre le plus efficace est Pandera + Z-score/IQR, puis Isolation Forest. |
| Options considerees | 1. Commencer par SHAP (forte explicabilite, plus lourd a stabiliser). 2. Commencer par Pandera + Z-score/IQR (quick win), puis renfort BC05. |
| Decision humaine | Option 2 retenue. |
| Justification | Delai court, forte lisibilite metier, sortie immediate exploitable dans Streamlit. |
| Impact | Plan de mise en oeuvre progressif sans rupture de l'existant. |

### Entree 3 - Homogeneisation des pages Partie 1

| Champ | Contenu |
|---|---|
| Contexte | Les liens vers `.md` etaient heterogenes dans le parcours public. |
| Hypothese IA | Rendre les fiches Partie 1 en pages Jekyll `.html` stabilise l'experience lecteur. |
| Options considerees | 1. Garder les liens `.md`. 2. Creer des wrappers `index.md` par dossier. 3. Ajouter un front matter aux fiches et pointer vers `.html`. |
| Decision humaine | Option 3 retenue. |
| Justification | Solution simple, compatible Jekyll 3.10, sans include relatif fragile. |
| Impact | Affichage homogène des livrables Partie 1 dans le theme Cayman. |

### Entree 4 - Acces public aux preuves notebook

| Champ | Contenu |
|---|---|
| Contexte | Les URLs locales `.ipynb` pouvaient afficher `Not Found` en preview. |
| Hypothese IA | Les liens `nbviewer` offrent une lecture publique stable et immediate. |
| Options considerees | 1. Forcer la publication locale des `.ipynb`. 2. Pointer vers GitHub blob. 3. Pointer vers nbviewer. |
| Decision humaine | Option 3 retenue. |
| Justification | Lecture directe pour recruteur/evaluateur, sans telechargement obligatoire. |
| Impact | Preuves notebook consultables de facon plus fluide dans le parcours portfolio. |

### Entree 5 - Separation critique / surveillance BC05

| Champ | Contenu |
|---|---|
| Contexte | La matrice incluant kNN/K-Means dans le score global affichait trop de produits critiques. |
| Hypothese IA | Une rarete statistique doit prioriser l'investigation, pas declencher seule une urgence metier. |
| Options considerees | 1. Garder le score global unique. 2. Creer `critical_score` et `surveillance_score`. |
| Decision humaine | Option 2 retenue. |
| Justification | IF + SHAP + impact business est plus defendable pour une short-list CODIR. |
| Impact | Matrice stricte : 1 critique, 172 a surveiller, 652 normaux. |

## Preuves associees

| Preuve | Lien |
|---|---|
| README | [Ouvrir](README.md) |
| Veille metier et technologique | [Ouvrir](01_veille_metier_technologique.html) |
| Tests et validations | [Ouvrir](05_tests.html) |
| Resultats | [Ouvrir](06_resultats.html) |
| Notebook BC05 - section globale | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05) |
| Notebook BC05 - 9.1 Immediate | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IMMEDIATE) |
| Notebook BC05 - 9.2 Isolation Forest | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-IFOREST) |
| Notebook BC05 - 9.3 K-Means et kNN | [Ouvrir](https://nbviewer.org/github/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/notebooks/bottleneck_analyse_ameliore_final.ipynb#RNCP37837BC05-KMEANS-KNN) |
| Mode d'emploi dashboard | [Ouvrir](09_mode_emploi_dashboard.html) |
| Dashboard KPI | [Ouvrir](https://p6-dashboard-wdcn5o8grt39nqtim6mgym.streamlit.app/) |
| README du portfolio | [Ouvrir](README.md) |
