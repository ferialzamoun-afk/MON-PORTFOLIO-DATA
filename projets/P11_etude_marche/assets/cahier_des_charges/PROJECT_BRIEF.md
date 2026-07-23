# PROJECT BRIEF - P11

## 1) Contexte

La poule qui chante est une entreprise francaise qui vend des poulets biologiques.
Le PDG souhaite evaluer des opportunites d expansion a l international.

Le projet data a pour but de proposer une premiere selection de pays cibles, puis de preparer une etude de marche plus detaillee.

## 2) Problematique

Quels groupes de pays presentent le meilleur potentiel pour exporter du poulet bio, selon des criteres d importation, de demande potentielle et de faisabilite macro-economique ?

## 3) Objectifs de la mission

- Construire une base d analyse multi-sources par pays.
- Integrer une logique PESTEL avec au moins 8 variables (16 retenues au total).
- Couvrir au minimum 100 pays et 60% de la population mondiale.
- Realiser une ACP pour reduire la dimension.
- Segmenter les pays via CAH puis K-means.
- Proposer un top 5 de pays a prioriser.

## 4) Donnees mobilisees

| Bloc de donnees | Sources principales | Apports principaux |
|---|---|---|
| Demande et disponibilite alimentaire | FAO Food Balances, FAO Population | consommation, pertes, population, variables par habitant, controle du seuil 60% population mondiale |
| Commerce et production volaille | FAOSTAT import/export, FAOSTAT production, OMC/ADB HS0207, Trade Map | importations, exportations, production, dependance import, intensite import volaille |
| Signal bio premium | FiBL, OMC/ADB, indicateurs croises bio/import | surface bio, part bio, producteurs bio, ventes retail bio, maturite bio/import |
| Risque sanitaire et reglementaire | FAO Latest Reported Events, FAOLEX Environment | evenements aviaires, H5N1, textes reglementaires, diversite textuelle Levenshtein |
| Contexte macro et institutionnel | Banque mondiale PIB, Ease of Business, stabilite politique | richesse, facilite d affaires, stabilite institutionnelle |
| Geographie et referentiels pays | dimension pays enrichie, CEPII geo/distances | ISO3, regions, harmonisation pays, distance et proxies logistiques |

## 5) Feature engineering realise

Transformations principales:

- Harmonisation pays: `country_key`, ISO3, libelles harmonises et exclusion des agregats geographiques.
- Indicateurs marche: import net, dependance import, ratios par habitant et transformations `log1p` pour limiter l effet taille.
- Indicateurs bio premium: variables FiBL, importations OMC/ADB HS0207 et signaux croises bio/import.
- Indicateurs risque: evenements aviaires, H5N1, volumes FAOLEX et score de diversite textuelle par Levenshtein.
- Scores de lecture: score coeur marche, score bio premium, indice de confiance donnees et segment d action, utilises pour interpreter la decision mais pas comme variables actives de l ACP.

## 6) Resultats et recommandation de soutenance

Synthese du notebook ACP/clustering:

- Base ACP finale: 139 pays; projection ACP/clusters exportee sur 138 pays.
- ACP: 11 variables actives, 3 composantes retenues pour le clustering, 89,90% de variance cumulee conservee.
- Lecture des axes: PC1 signal bio/import premium, PC2 risque sanitaire et intensite productive, PC3 lecture complementaire de structure marche.
- Clustering: KMeans retient `k=2`; le cluster prioritaire ACP regroupe 16 pays a instruire rapidement.
- Decision finale: candidats prioritaires fiables -> Top 5 -> shortlist 3 -> pays recommande.
- Top 5 candidats fiables: Suisse, Dominique, Emirats arabes unis, Belgique, Autriche. Shortlist 3: Suisse, Dominique, Emirats arabes unis. Pays recommande final: **Suisse**.

## 7) Methodologie

### Etape A - Preparation et nettoyage
- Standardiser les noms de pays (normalisation unicode + regex).
- Controler les types, valeurs manquantes et doublons.
- Fusionner les sources dans une table unique par pays.

### Etape B - Feature engineering
- Creer les variables derivees listees ci-dessus dans le notebook de preparation.
- Conserver `scripts/enrich_market_features_model.py` comme module de fonctions testees et reutilisables pour la normalisation pays, Levenshtein et certains enrichissements.

### Etape C - Tests pre-ACP
- Tests d adequation pre-ACP et controles de qualite des variables actives.

### Etape D - ACP
- Standardiser les variables actives et retenir PC1 a PC3 pour combiner variance conservee, lisibilite metier et stabilite du clustering.
- Analyser cercle des correlations et projection des individus.

### Etape E - Clustering
- CAH (Ward) comme controle de coherence et KMeans comme segmentation operationnelle.
- Choisir `k=2` selon silhouette, taille minimale des groupes et lisibilite metier.

### Etape F - Recommandation business
- Profiler les segments, identifier le cluster prioritaire, selectionner le Top 5 puis la shortlist.

## 8) Livrables

- `notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb` : preparation, feature engineering, controles qualite et base ACP.
- `notebooks/ZAMOUN_Férial_2_clustering_visualisations _112025.ipynb` : ACP, CAH, KMeans, robustesse, profils de clusters, entonnoir de recommandation.
- `scripts/data_manager.py` : helper d inspection appele par le notebook 1.
- `scripts/enrich_market_features_model.py` : fonctions testees de normalisation, Levenshtein et enrichissements reutilisables.
- `tests/` : 16 tests unitaires (pytest) couvrant les fonctions critiques.
- Workflow CI GitHub Actions (lint, tests et controles structurels notebooks a chaque push/pull request).
- Support de presentation `.ppt` : maximum 25 slides, structure contexte -> demarche -> resultats.

## 9) Criteres de qualite

- Tracabilite: sources, transformations, exports ACP et exports de decision documentes.
- Qualite donnees: harmonisation pays/ISO3, exclusion des agregats, controle de couverture et des doublons.
- Pertinence metier: variables reliees aux dimensions marche, bio premium, sanitaire, reglementaire, institutionnelle et logistique.
- Justification methodologique: ACP sur variables actives, scores gardes en lecture, PC1 a PC3 retenues, `k=2` choisi pour lisibilite et silhouette.
- Robustesse: comparaison CAH/KMeans, tests de segments decision export, limites explicites.
- Reproductibilite: notebooks documentes, helpers Python conserves, tests unitaires, lint et CI GitHub Actions.
- Lisibilite: separation claire entre resultats statistiques, interpretation metier et recommandation business.

## 10) Limites et risques

- Qualite heterogene des sources et annees disponibles.
- Variables production/slaughter avec ~42% de couverture seulement.
- ACP exploratoire: les axes synthetiques aident a structurer la decision, mais ne remplacent pas la lecture des indicateurs sources.
- Sensibilite des clusters aux choix de variables, de normalisation et de perimetre pays; les segments export doivent etre relus avec la confiance source et les profils atypiques.

## 11) Facteurs de priorisation

La recommandation finale combine trois lectures complementaires:

- Attractivite marche: potentiel import, richesse, facilite d affaires, dependance aux importations.
- Compatibilite bio premium: maturite bio, signaux FiBL/OMC-ADB, environnement reglementaire et sanitaire.
- Fiabilite decisionnelle: qualite de couverture, indice de confiance, accord CAH/KMeans et lecture des variables brutes.

## 12) Charge et planning indicatif

Estimation centrale: 18 a 20 JH, avec une fourchette realiste de 14 a 25 JH selon la qualite des donnees et les iterations de soutenance.

| Semaine | Focales | Charge |
|---|---|---|
| S1 | Cadrage, inventaire sources, nettoyage initial | 4-5 JH |
| S2 | Fusion multi-sources, feature engineering, controles qualite | 4-5 JH |
| S3 | ACP, CAH/KMeans, interpretation des profils | 4-5 JH |
| S4 | Robustesse, recommandation, finalisation notebooks et support | 4-5 JH |

Livrable final: deux notebooks finalises, exports de decision, tests/CI, documentation et support de presentation.
