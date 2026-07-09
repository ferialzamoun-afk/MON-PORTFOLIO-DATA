# Projet P14 - Analyse de donnees retail

Ce depot centralise les travaux d'analyse, de preparation de donnees et de restitution autour du perimetre P14, avec deux axes principaux:

- une couche analytique et documentaire (notebooks, livrables, rapports),
- une couche applicative (Streamlit) et decisionnelle (Power BI).

L'objectif est de fournir un socle exploitable pour le pilotage metier (assortiment, disponibilite, performance operationnelle, gouvernance des indicateurs).

## Objectifs du depot

- Structurer les donnees depuis des sources brutes jusqu'a des jeux exploitables.
- Produire des analyses reproductibles via notebooks et scripts.
- Alimenter des restitutions metier via Power BI et application Streamlit.
- Conserver une documentation projet claire pour la maintenance et la transmission.

## Arborescence principale

- data/: donnees brutes et jeux transformes.
- docs/: documentation transverse, archives, exports, figures, notebooks et supports.
- intermarche_notebook/: notebooks d'exploration et d'analyse sur le perimetre Intermarche.
- powerbi/: ecosysteme Power BI (documentation, exports, scripts, rapports).
- streamlit_app/: application Streamlit (modules, scripts, assets, notebooks associes).
- bilan_reflexif_stage_P14.md: retour d'experience et formalisation de stage.
- feuille_de_route_stage_P5.md: feuille de route et contexte de cadrage.
- modele_mail_note_livraison.md: modele de communication de livraison.

## Organisation des donnees

Le dossier data/ suit une logique classique de pipeline:

- data/raw/: donnees sources non modifiees.
- data/processed/: donnees nettoyees/standardisees pretes pour l'analyse.
- data/Fichiers transformes/DLP/: jeux transformes lies au perimetre DLP.

Bonnes pratiques:

- conserver les fichiers sources intacts dans raw/;
- documenter toute transformation majeure dans docs/ ou dans les rapports concernes;
- eviter de versionner des donnees sensibles ou inutilement volumineuses.

## Demarrage rapide (Windows)

1. Activer l'environnement virtuel Python du projet:

```powershell
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned)
& .\venv\Scripts\Activate.ps1
```

2. Installer/mettre a jour les dependances de l'application Streamlit:

```powershell
python -m pip install -r streamlit_app\requirements.txt
```

3. Lancer l'application Streamlit (si le point d'entree est present dans streamlit_app/):

```powershell
streamlit run streamlit_app\streamlit_app.py
```

## Flux de travail recommande

1. Ingestion et preparation:

- deposer les nouvelles sources dans data/raw/;
- executer les notebooks/scripts de preparation;
- produire des sorties homogenes dans data/processed/ ou powerbi/outputs/ selon le besoin.

2. Analyse:

- utiliser les notebooks dans intermarche_notebook/ et les notebooks du dossier powerbi/notebooks/;
- tracer les hypotheses, regles et limites dans docs/ ou powerbi/rapports/.

3. Restitution:

- mettre a jour les artefacts Power BI dans powerbi/;
- aligner les KPI et la narration metier avec les rapports de reference;
- verifier la coherence entre les sorties Streamlit et Power BI.

## Conventions projet

- Documentation: privilegier des notes courtes, actionnables et datees.
- Reproductibilite: expliciter les prerequis d'execution dans chaque sous-module.
- Qualite des donnees: journaliser les controles (doublons, cles, granularite, valeurs manquantes).
- Gouvernance: separer clairement les donnees brutes, transformees et publiees.
- Portfolio: inclure une section "Preuve de competences" dans chaque README projet.

## Preuve de competences

Cette section formalise les preuves mobilisables dans le cadre du portfolio, avec un accent explicite sur la veille metier et technologique.

### Resultats de veille metier

- Problematiques metier suivies: disponibilite produit, performance assortiment, pilotage des alertes.
- Traduction analytique: indicateurs priorises, regles de gestion, criteres d'arbitrage.
- Impacts attendus: meilleure priorisation des actions et reduction des angles morts operationnels.

### Resultats de veille technologique

- Outils mobilises: Python (pandas/notebooks), Streamlit, Power BI.
- Pratiques retenues: structuration raw/processed, fiabilisation des transformations, documentation des hypotheses.
- Valeur produite: acceleration des analyses, restitution plus lisible, cadre de maintenance renforce.

### Tracabilite des livrables

- Sources de preuve: notebooks d'analyse, scripts de transformation, rapports Power BI, documentation projet.
- Principe de preuve: chaque livrable doit expliciter le besoin metier adresse, la methode appliquee et le resultat obtenu.

### Convention portfolio (a appliquer ensuite)

Pour les prochains README du portfolio, appliquer la trame de reference disponible dans docs/config/convention_readme_portfolio.md.

## Points d'entree utiles

- README global: ce fichier.
- streamlit_app/README.md: cadre applicatif Streamlit.
- powerbi/README.md: cadre de la partie BI.
- docs/README.md: socle documentaire transverse.

## Maintenance

Pour garder le depot lisible dans la duree:

- supprimer ou archiver regulierement les livrables obsoletes;
- conserver les versions finales dans des emplacements explicites (rapports, exports, outputs);
- mettre a jour ce README a chaque evolution structurelle majeure.
