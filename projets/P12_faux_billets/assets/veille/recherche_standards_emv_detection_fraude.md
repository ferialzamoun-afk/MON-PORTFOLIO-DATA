# Recherche sur les standards EMV et les outils de detection de fraude

## 1) Objectif de la veille

Cette note de veille documente les references utilisees pour cadrer la detection de fraude dans le projet P12 (faux billets), avec un focus sur:

- les standards EMV (cartes et paiements),
- les pratiques de securite et de gestion du risque,
- les outils data et machine learning de detection de fraude.

## 2) Avancees majeures 2026 avec impact strict sur les paiements cartes

| Avancee 2026 | Impact strict paiements cartes | Priorite operationnelle 2026-2027 |
|---|---|---|
| Mise a jour EMV Payment Tokenisation v2.4 (juillet 2026) | Renforce la securisation des paiements carte a distance (CNP), la gestion du cycle de vie des tokens et la resilience des transactions tokenisees. | Elevee pour e-commerce, wallet, card-on-file. |
| Publication Contactless Kernel Book C-3 a C-7 v2.12 (juillet 2026) | Ameliore l interoperabilite carte-terminal en paiement sans contact et reduit les ecarts d implementation. | Elevee pour acceptance de proximite. |
| Bulletins techniques EMV Level 3 (juillet 2026) | Met a jour les exigences de validation de bout en bout pour l acceptance carte, avec impact direct sur certification et maintenance terminale. | Elevee pour acquerreurs, integrateurs et fabricants terminaux. |
| Bulletin annuel EMVCo sur la longueur des cles publiques (juillet 2026) | Ajuste les exigences cryptographiques applicables aux transactions EMV carte (contact/contactless). | Moyenne a elevee selon parc et cycle de certification. |
| Consultation EMVCo sur les Verifiable Digital Credentials pour authentification card-based (avril 2026) | Ouvre une trajectoire de renforcement de l authentification des paiements carte a distance, en complement de 3DS. | Moyenne en 2026, forte a moyen terme selon adoption scheme/issuer. |

## 3) Rappel sur EMV

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

## 4) Outils et approches de detection de fraude

### 4.1 Outils Python / ML utilises

- scikit-learn: pipelines, modeles de classification, validation croisee;
- pandas / numpy: preparation et controle qualite des donnees;
- matplotlib / seaborn: visualisation des distributions, corrrelations, erreurs;
- joblib: serialisation du pipeline final;
- FastAPI: exposition du modele via API de prediction.

### 4.2 Methodes comparees dans le notebook

- Logistic Regression,
- K-Nearest Neighbors,
- Random Forest,
- GridSearchCV + StratifiedKFold pour la robustesse.

### 4.3 Metriques prioritaires

- recall de la classe faux billet (prioritaire metier),
- precision,
- F1-score,
- ROC-AUC,
- matrice de confusion.

### 4.4 Impact 2026 sur les outils et approches de detection de fraude

- Tokenisation EMV v2.4: deplace une partie du risque vers la gestion du cycle de vie des tokens. Les pipelines de fraude doivent integrer des signaux token-centriques (age du token, frequence de remplacement, coherence device-token-merchant) en plus des signaux PAN historiques.
- Contactless kernels v2.12 et bulletins L3: imposent des mises a jour de conformite terminale. Cote data science fraude, cela force une segmentation pre/post mise en conformite pour eviter de melanger des comportements transactionnels issus de regles terminal differentes.
- Renforcement cryptographique (cles publiques): augmente le besoin de tracer les erreurs techniques vs fraude reelle. Les tableaux de bord doivent separer declins techniques, authentification echouee et suspicion fraude pour ne pas biaiser les modeles.
- Credentials verifiables pour authentification card-based: pousse les approches vers une fraude plus contextuelle (identite, preuve cryptographique, parcours client) et moins uniquement comportementale. En pratique, cela favorise des modeles hybrides: regles temps reel + score ML.
- Consequence operative: la detection devient plus "risk orchestration" que simple classification. Il faut combiner scoring, politiques d'authentification adaptative (step-up), et monitoring continu de drift par canal (presentiel, CNP, wallet).

## 5) Bonnes pratiques retenues

- separer strictement train/test (eviter fuite de donnees),
- imputer et standardiser dans un pipeline unique,
- comparer plusieurs modeles sur protocole homogene,
- selectionner le modele final sur metrique metier prioritaire,
- documenter les limites (generalisation, derive, volume).

## 6) Limites et vigilance

- la veille EMV ne couvre pas directement la physique des billets;
- les resultats restent dependants du jeu de donnees disponible;
- un monitoring de derive est recommande en production.

## 7) Sources de reference (a consolider)

- EMVCo: specifications EMV (niveau standard).
- Documentation scikit-learn: model selection, metrics, pipelines.
- Documentation FastAPI: exposition d API ML.

Note: cette veille est un support de contexte pour le bloc RNCP BC04 et complete la preuve de pilotage de projet data.