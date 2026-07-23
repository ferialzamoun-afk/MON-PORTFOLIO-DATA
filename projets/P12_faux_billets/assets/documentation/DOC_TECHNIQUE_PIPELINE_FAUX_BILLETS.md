# Documentation technique - Detection de faux billets (mise a jour)

## 1) Objectif

Ce projet met en place une chaine complete de classification binaire pour predire si un billet est authentique ou faux.

Convention cible utilisee dans le notebook:

- `faux_billet = 0` : billet authentique
- `faux_billet = 1` : faux billet

Le projet couvre:

- l'analyse exploratoire et la qualite des donnees,
- la comparaison de plusieurs algorithmes,
- la selection d'un modele final,
- l'integration du modele dans une API FastAPI.

## 2) Fichiers livrables principaux

| Fichier | Role |
|---|---|
| `notebooks/p12_da_maj+(1).ipynb` | Notebook de reference (EDA, modelisation, comparaison, export). |
| `data/raw/billets.csv` | Jeu de donnees source (1500 billets). |
| `data/processed/billets_cleaned.csv` | Donnees preprocesses exportees depuis notebook. |
| `src/model_oncfm.joblib` | Modele final exporte avec preprocessing integre. |
| `api/main.py` | Point d'entree FastAPI. |
| `api/router.py` | Endpoints `/`, `/health`, `/predict`, `/predict/batch`. |
| `api/services/prediction.py` | Chargement modele + logique de prediction. |

## 3) Traitements et analyses en amont

### 3.1 Analyse exploratoire

Le notebook verifie:

- dimensions du dataset,
- types de colonnes,
- statistiques descriptives,
- valeurs manquantes,
- doublons,
- repartition de la cible.

Constat important:

- `margin_low` contient des valeurs manquantes.

### 3.2 Construction de la cible

La variable `is_genuine` est convertie en `faux_billet`:

- `True` -> `0`
- `False` -> `1`

La variable cible sert uniquement pendant l'entrainement. En prediction API, on ne fournit que les mesures du billet.

### 3.3 Outliers

Deux approches sont documentees:

- IQR global descriptif,
- verification Z-score.

Une approche IsolationForest est egalement testee pour quantifier les observations atypiques.

### 3.4 Preparation des donnees

Principes appliques:

- split train/test stratifie (`test_size=0.20`, `random_state=42`),
- imputation mediane,
- standardisation,
- prevention de fuite de donnees (fit sur train, transform sur test).

## 4) Algorithmes testes et resultats

### 4.1 KMeans (non supervise, comparaison pedagogique)

Usage:

- test exploratoire de separabilite,
- comparaison indirecte aux vraies classes.

Conclusion:

- utile pour discussion methodologique,
- non retenu pour la prediction metier car non supervise.

### 4.2 Regression logistique (baseline supervisee)

Configuration:

- pipeline `SimpleImputer(median) -> StandardScaler -> LogisticRegression(max_iter=1000)`
- split 80/20 stratifie.

Ordre de grandeur observe dans le notebook:

- Accuracy proche de `0.99`
- ROC-AUC proche de `0.999`
- matrice de confusion stable, avec peu d'erreurs.

Interet:

- interpretable,
- rapide,
- tres bonne baseline,
- facile a encapsuler dans API.

### 4.3 KNN

Configuration:

- KNN (`n_neighbors=5`) sur donnees standardisees.

Resultat:

- performance elevee,
- mais plus sensible a l'echelle et potentiellement moins robuste au bruit.

### 4.4 RandomForest

Configuration:

- RandomForest avec ponderation de classes,
- evaluation sans et avec ACP.

Resultat:

- performance tres elevee,
- tres bon compromis robustesse/performance,
- retenu pour le modele final exporte dans `src/model_oncfm.joblib`.

## 5) Choix du modele final et justification

Le projet conserve deux niveaux:

1. **Baseline de reference:** regression logistique (simple, explicable, bonne performance).
2. **Modele final de livraison:** RandomForest pipeline exporte (`src/model_oncfm.joblib`) pour l'API.

Raisons du choix final livraison:

- robustesse globale,
- excellents scores sur le jeu de test,
- pipeline complet exportable (preprocessing + modele).

## 6) Application fonctionnelle (API)

L'API expose:

- `GET /` : message de bienvenue,
- `GET /health` : etat de service et chargement du modele,
- `POST /predict` : prediction unitaire,
- `POST /predict/batch` : lecture d'un CSV (version de base).

Schema d'entree unitaire attendu par `POST /predict`:

- `diagonal`
- `height_left`
- `height_right`
- `margin_low`
- `margin_up`
- `length`

Schema de sortie:

- `prediction` : `"VRAI"` ou `"FAUX"`
- `is_genuine` : booleen
- `proba_vrai` : probabilite classe 0
- `proba_faux` : probabilite classe 1

## 7) Chargement et prediction du modele

Le service de prediction:

- cherche d'abord `src/model_oncfm.joblib`,
- conserve une compatibilite avec d'anciens emplacements de `model_oncfm.joblib`,
- controle que l'entree contient bien 6 features,
- retourne prediction et probabilite associee.

Exemple minimal:

```python
import joblib
import pandas as pd

model = joblib.load("src/model_oncfm.joblib")

sample = pd.DataFrame([
    {
        "diagonal": 171.81,
        "height_left": 104.86,
        "height_right": 104.95,
        "margin_low": 4.52,
        "margin_up": 2.89,
        "length": 112.83,
    }
])

pred = model.predict(sample)[0]
proba_faux = model.predict_proba(sample)[0, 1]
print(pred, round(proba_faux, 3))
```

## 8) Limites et points de vigilance

- vigilance drift en production (distribution des nouvelles donnees),
- surveillance continue des metriques,
- recalibrage/reentrainement uniquement sur donnees etiquetees valides,
- gestion des erreurs d'input API (types, colonnes manquantes, valeurs hors bornes).

## 9) Conclusion

Le projet est coherent de bout en bout:

- notebook pedagogique et reproductible,
- baseline claire (regression logistique),
- modele final performant exporte,
- API fonctionnelle basee sur le meme schema de features.

La livraison est donc exploitable pour une demonstration et pour une premiere integration metier.
