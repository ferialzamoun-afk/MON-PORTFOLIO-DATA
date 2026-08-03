# Recherche sur les standards EMV et les outils de detection de fraude

## 1) Objectif de la veille

Cette note de veille documente les references utilisees pour cadrer la detection de fraude dans le projet P12 (faux billets), avec un focus sur:

- les standards EMV (cartes et paiements),
- les pratiques de securite et de gestion du risque,
- les outils data et machine learning de detection de fraude.

## 2) Rappel sur EMV

EMV (Europay, Mastercard, Visa) est un ensemble de specifications techniques pour les paiements par carte a puce.

Points clefs:

- authentification forte de la carte,
- securisation des transactions,
- reduction de la fraude a la carte presente,
- standardisation des terminaux et protocoles.

Limite dans P12:

- EMV concerne prioritairement les paiements cartes;
- le projet P12 porte sur la classification de faux billets;
- la veille EMV sert ici de reference methodologique securite/risque, pas de protocole direct de modelisation des billets.

## 3) Outils et approches de detection de fraude

### 3.1 Outils Python / ML utilises

- scikit-learn: pipelines, modeles de classification, validation croisee;
- pandas / numpy: preparation et controle qualite des donnees;
- matplotlib / seaborn: visualisation des distributions, corrrelations, erreurs;
- joblib: serialisation du pipeline final;
- FastAPI: exposition du modele via API de prediction.

### 3.2 Methodes comparees dans le notebook

- Logistic Regression,
- K-Nearest Neighbors,
- Random Forest,
- GridSearchCV + StratifiedKFold pour la robustesse.

### 3.3 Metriques prioritaires

- recall de la classe faux billet (prioritaire metier),
- precision,
- F1-score,
- ROC-AUC,
- matrice de confusion.

## 4) Bonnes pratiques retenues

- separer strictement train/test (eviter fuite de donnees),
- imputer et standardiser dans un pipeline unique,
- comparer plusieurs modeles sur protocole homogene,
- selectionner le modele final sur metrique metier prioritaire,
- documenter les limites (generalisation, derive, volume).

## 5) Limites et vigilance

- la veille EMV ne couvre pas directement la physique des billets;
- les resultats restent dependants du jeu de donnees disponible;
- un monitoring de derive est recommande en production.

## 6) Sources de reference (a consolider)

- EMVCo: specifications EMV (niveau standard).
- Documentation scikit-learn: model selection, metrics, pipelines.
- Documentation FastAPI: exposition d API ML.

Note: cette veille est un support de contexte pour le bloc RNCP BC04 et complete la preuve de pilotage de projet data.