# PROJECT BRIEF - P12

## 1) Contexte

L'ONCFM (Office National de Lutte contre le Faux Monnayage) souhaite automatiser la detection des faux billets.
La mission consiste a construire un modele de classification capable de distinguer les vrais billets des faux a partir de mesures geometriques.

## 2) Problematique

Peut-on predire de facon fiable si un billet est authentique ou contrefait, uniquement a partir de ses dimensions physiques ?

## 3) Objectifs de la mission

- Analyser et preparer les donnees de mesures geometriques.
- Selectionner et entrainer le meilleur modele de classification.
- Optimiser le recall sur la classe "faux billet" (priorite metier : limiter les faux negatifs).
- Exporter le pipeline final et l'exposer via une API FastAPI.

## 4) Donnees mobilisees

| Source | Description | Variables |
|---|---|---|
| `data/raw/billets.csv` | Donnees source labellisees | 6 variables geometriques + cible `is_genuine` |
| `data/prod/billets_production.csv` | Donnees de production sans label | 6 variables geometriques |

Variables predictives : `diagonal`, `height_left`, `height_right`, `margin_low`, `margin_up`, `length`.

Convention cible : `0` = vrai billet, `1` = faux billet.

## 5) Feature engineering realise

- Creation de la variable cible `faux_billet` depuis `is_genuine`.
- Imputation des valeurs manquantes integree dans le pipeline scikit-learn.
- Standardisation conditionnelle selon le modele.
- Split train/test stratifie pour conserver la distribution des classes.

## 6) Resultats

- **Recall (faux billets)** : **100%** — aucun faux billet classe comme vrai.
- **F1-Score** : **0.91**.
- **Modele retenu** : pipeline scikit-learn exporte dans `src/model_oncfm.joblib`.
- **API** : 4 endpoints (GET /, GET /health, POST /predict, POST /predict/batch).

## 7) Methodologie

### Etape A - Exploration et preparation
- Controle qualite des 6 variables, valeurs manquantes, distribution des classes.
- EDA : visualisations par classe, correlations.

### Etape B - Modelisation
- GridSearchCV avec StratifiedKFold sur 3 modeles : Logistic Regression, KNN, Random Forest.
- Critere de selection : recall de la classe faux billet.
- Evaluation finale sur jeu de test hold-out.

### Etape C - Export et API
- Pipeline complet (preprocessing + modele) exporte avec joblib.
- API FastAPI avec validation Pydantic, endpoints unitaire et batch.
- Tests unitaires pytest sur les routes et la logique de prediction.

## 8) Livrables

- `notebooks/p12_da_maj+(1).ipynb` : exploration, modelisation, selection du modele, evaluation finale.
- `src/model_oncfm.joblib` : pipeline scikit-learn serialise.
- `api/` : application FastAPI (main.py, router.py, services/prediction.py, validation.py).
- `tests/` : tests unitaires et tests API (pytest).
- `Dockerfile` et `Procfile` : deploiement sur Render ou conteneur Docker.

## 9) Criteres de qualite

- Recall 100% sur la classe faux billet (objectif metier prioritaire).
- Pipeline reproductible : preprocessing integre, pas de fuite train/test.
- API documentee via Swagger automatique (FastAPI).
- Tests couvrant les routes critiques et la logique de prediction.

## 10) Limites et risques

- Dataset de taille limitee (environ 1500 billets) : resultats a confirmer sur des volumes plus larges.
- Modele base uniquement sur des variables geometriques : toute alteration physique non representee dans les donnees d entrainement peut degrader les performances.
- API non deployee en production : necessite une plateforme externe (Render, Docker) pour une URL publique.
