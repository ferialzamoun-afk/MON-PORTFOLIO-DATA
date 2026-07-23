# Note pipeline - Preparation et nettoyage des donnees

## Objectif du pipeline

Le notebook 1 simplifie a pour role de transformer des sources brutes heterogenes en une base analytique pays exploitable pour la decision export.

L objectif n est pas encore de recommander les pays finaux. L objectif est de produire un **jalon de donnees fiable**, documente et reproductible, qui servira ensuite a l ACP, au clustering et au scoring decisionnel.

Base figee en sortie:

- `data/processed/base_acp_finale_2017.csv`
- `data/processed/base_acp_finale_standardisee_2017.csv`

Ces bases deviennent la reference pour le notebook ACP decision export livre dans `notebooks/`.

## Fichiers utilises par les deux notebooks livres

Cette liste est issue des chemins effectivement references dans les deux notebooks presents dans le depot.

### Sources `data/raw` lues par le notebook 1

| Fichier | Role dans la preparation |
|---|---|
| `data/raw/1-Collecte des données/DAN-P9-data/DisponibiliteAlimentaire_2017.csv` | disponibilite alimentaire volaille |
| `data/raw/1-Collecte des données/DAN-P9-data/Population_2000_2018.csv` | population pays |
| `data/raw/1-Collecte des données/Données collectées/FAOSTAT_data_Imp_Exp_Poulets_Monde.csv` | imports/exports volaille |
| `data/raw/1-Collecte des données/Données collectées/country_mapping_fr_en_iso.csv` | mapping pays FR/EN/ISO |
| `data/raw/1-Collecte des données/Données collectées/ease doing of business Data.csv` | facilite d affaires |
| `data/raw/1-Collecte des données/Données collectées/PoliticalStability.csv` | stabilite politique |
| `data/raw/1-Collecte des données/Données collectées/pib.csv` | PIB principal |
| `data/raw/pib par habitant.csv` | fallback PIB |
| `data/raw/1-Collecte des données/Données collectées/geo_cepii.xls` | referentiel pays CEPII |
| `data/raw/1-Collecte des données/Données collectées/dist_cepii.xls` | distances et proxies logistiques CEPII |
| `data/raw/1-Collecte des données/Données collectées/FAOSTAT_data_Prod_Poulets_Monde.csv` | production/abattage poulets |
| `data/raw/1-Collecte des données/Données collectées/Latest Reported Events.csv` | evenements sanitaires aviaires |
| `data/raw/1-Collecte des données/Données collectées/FAOLEX_Environment.csv` | textes reglementaires FAOLEX |
| `data/raw/1-Collecte des données/Données collectées/dim_pays_enriched.csv` | dimension pays enrichie |

### Fichier `processed` lu en enrichissement par le notebook 1

| Fichier | Role |
|---|---|
| `data/processed/market_features_ready_omc_fibl_fe.csv` | signal OMC/ADB + FiBL + feature engineering bio/import si le fichier est disponible |

### Exports `processed` produits par le notebook 1 et utiles au suivi

| Fichier | Role |
|---|---|
| `controle_representativite_pays_population.csv` | controle couverture pays/population |
| `base_intermediaire_fusion_pays_2017.csv` | base fusionnee intermediaire |
| `base_intermediaire_fusion_pays_2017_sans_nan.csv` | base intermediaire nettoyee des NaN bloquants |
| `controle_variables_base_sans_nan.csv` | controle variables apres nettoyage |
| `controle_correlations_fortes_base_sans_nan.csv` | controle correlations fortes |
| `selection_variables_post_fusion.csv` | arbitrage initial des variables |
| `base_selectionnee_post_fusion_2017.csv` | base selectionnee avant enrichissement final |
| `base_feature_engineered_2017.csv` | base enrichie en variables derivees |
| `variables_creees_feature_engineering.csv` | inventaire des variables creees |
| `stats_descriptives_base_feature_engineered.csv` | statistiques descriptives |
| `controle_outliers_iqr_base_feature_engineered.csv` | controle outliers IQR |
| `detail_outliers_iqr_base_feature_engineered.csv` | detail outliers IQR |
| `base_pre_standardisation_acp_2017.csv` | base avant standardisation ACP |
| `controle_pre_standardisation_acp.csv` | controle pre-standardisation |
| `apercu_variables_standardisees_zscore.csv` | apercu z-score |
| `matrice_correlation_pearson_variables_candidates.csv` | matrice Pearson |
| `matrice_correlation_spearman_variables_candidates.csv` | matrice Spearman |
| `rapport_colinearite_variables_candidates.csv` | rapport colinearite |
| `paires_colinearite_pearson_forte_variables_candidates.csv` | paires Pearson fortes |
| `paires_colinearite_spearman_forte_variables_candidates.csv` | paires Spearman fortes |
| `arbitrage_selection_finale_variables_acp.csv` | arbitrage final des variables ACP |
| `base_acp_finale_2017.csv` | base finale non standardisee pour interpretation |
| `base_acp_finale_standardisee_2017.csv` | base finale standardisee pour ACP/CAH/KMeans |
| `controle_colinearite_base_acp_finale.csv` | controle colinearite final |
| `dictionnaire_variables_acp_finales.csv` | dictionnaire final des variables |
| `controle_completion_acp_finale.csv` | controle final de completion |

### Fichiers consommes et produits par le notebook 2

Le notebook 2 lit uniquement les quatre fichiers finals suivants dans `data/processed`:

- `base_acp_finale_2017.csv`
- `base_acp_finale_standardisee_2017.csv`
- `dictionnaire_variables_acp_finales.csv`
- `controle_completion_acp_finale.csv`

Il produit les exports suivants dans `data/processed/decision_export`:

- `decision_export_scores.csv`
- `top5_decision_export_synthese.csv`
- `top10_decision_export.csv`
- `top20_recommandations_decision_export.csv`
- `segments_decision_export_synthese.csv`
- `tests_robustesse_segments_decision_export.csv`
- `zamoun_acp_projection_clusters.csv`
- `zamoun_acp_cluster_profiles.csv`
- `zamoun_acp_cluster_summary.csv`
- `zamoun_acp_variable_loadings.csv`

Le notebook 2 calcule ensuite l entonnoir final suivant: Top 5 candidats fiables = Suisse, Dominique, Emirats arabes unis, Belgique, Autriche; shortlist 3 = Suisse, Dominique, Emirats arabes unis; pays recommande final = Suisse.

Attention: les exports `top5_decision_export_synthese.csv` et `top10_decision_export.csv` ne suffisent pas a decrire la recommandation finale. Ils correspondent a un scoring export intermediaire; la decision finale est produite plus loin dans le notebook, apres filtrage des candidats prioritaires fiables et construction de la shortlist 3.

## Question metier portee par la preparation

La question fil rouge est:

> Quelles donnees transforment une source brute en information utile pour prioriser des pays d export poulet bio ?

Le pipeline construit donc une base pays qui permet de lire:

- la taille du marche,
- l intensite d importation de volaille,
- la dependance aux importations,
- la concurrence ou capacite de production locale,
- la facilite d entree commerciale,
- la stabilite politico-institutionnelle,
- le risque sanitaire,
- le cadre reglementaire,
- le signal bio/premium lorsque les extensions FiBL et OMC/ADB sont mobilisees.

## Logique generale du traitement

Le pipeline suit une logique en entonnoir.

### 1. Inventorier les sources

Les sources ne sont pas directement comparables. Elles peuvent differer par:

- pays libelles en francais ou en anglais,
- code pays manquant ou non normalise,
- annee disponible,
- unite de mesure,
- granularite pays ou pays-annee,
- couverture partielle.

Le premier travail consiste donc a identifier les fichiers utiles, leurs colonnes, leur role metier et leur potentiel d integration.

### 2. Normaliser les cles pays

Le point critique est l harmonisation pays.

Le pipeline cherche a stabiliser:

- `country_key`: cle textuelle normalisee,
- `code_iso3`: code pays ISO3 quand il est disponible,
- `country`: libelle lisible pour restitution.

Cette etape evite de comparer plusieurs lignes qui representeraient le meme pays sous des noms differents.

### 3. Filtrer les entites non exploitables

Certaines lignes peuvent correspondre a:

- anciennes entites geopolitiques,
- territoires sans ISO3 robuste,
- aggregats regionaux,
- lignes de metadata,
- pays avec donnees insuffisantes.

Ces lignes ne sont pas masquees silencieusement. Elles doivent etre tracees dans les audits ou exports d exclusion.

### 4. Construire les variables analytiques

Le pipeline ne se limite pas a reprendre des colonnes sources. Il cree des variables utiles a la decision:

- importations par habitant,
- ratio de dependance aux importations,
- signaux sanitaires recents,
- indicateurs reglementaires FAOLEX,
- indicateurs de contexte business,
- variables de production locale.

Ces variables donnent une lecture plus proche du probleme commercial que les donnees brutes.

### 5. Auditer la couverture

Avant l ACP, le pipeline mesure la disponibilite des variables.

L audit distingue:

- valeurs observees,
- valeurs manquantes,
- variables trop incompletes,
- variables disponibles mais a interpreter avec prudence,
- colonnes de tracabilite qui ne doivent pas entrer dans les calculs.

Cette etape est essentielle car une ACP peut devenir trompeuse si elle repose sur trop d imputation.

### 6. Imputer de facon transparente

L imputation permet d obtenir une matrice exploitable par l ACP.

Principe retenu:

- documenter les NaN avant imputation,
- imputer uniquement les variables analytiques,
- conserver les colonnes d identification hors imputation analytique,
- produire un resume d imputation.

Le but n est pas de faire disparaitre le probleme des donnees manquantes. Le but est de le rendre visible et maitrisable.

## Pourquoi figer un jalon de donnees ?

Une fois le notebook 1 termine, on fige un jalon pour eviter que les resultats ACP changent sans controle.

Figer un jalon signifie documenter:

- le fichier source final,
- le nombre de lignes,
- le nombre de colonnes,
- les variables disponibles,
- les regles de filtrage,
- les traitements de valeurs manquantes,
- les exports associes.

Les fichiers figes actuels sont:

- `data/processed/base_acp_finale_2017.csv`
- `data/processed/base_acp_finale_standardisee_2017.csv`

Ces fichiers sont les bases stables pour rejouer le notebook 2.

## Place de OMC/ADB et FiBL

Les donnees OMC/ADB et FiBL existent dans le projet et apportent un signal important.

Elles ne sont pas ignorees. Elles sont separees du coeur marche pour une raison methodologique.

### Pourquoi ne pas tout mettre dans le core ?

Le **core marche** doit rester robuste et lisible. Il mesure l attractivite export generale:

- taille de marche,
- importations,
- dependance aux importations,
- production locale,
- stabilite,
- facilite des affaires.

Si l on ajoute directement toutes les variables FiBL et bio dans cette ACP principale, on risque de melanger deux signaux:

- le signal marche massif,
- le signal bio premium.

Le risque est d obtenir une ACP difficile a interpreter: les grands importateurs, les pays tres bio et les pays avec donnees incompletes peuvent tirer les axes dans des directions differentes.

### Role correct de FiBL / OMC-ADB

Les variables FiBL et OMC/ADB doivent plutot alimenter le bloc **bio premium**:

- surface bio,
- part de surface bio,
- producteurs bio,
- ventes retail bio,
- importations OMC/ADB HS0207,
- indicateurs croises bio/import.

Elles servent a affiner la priorisation apres le classement coeur marche.

Lecture recommandee:

1. Le core marche repond: le pays est-il un marche export credible ?
2. Le bloc bio premium repond: le pays est-il interessant pour une offre differenciee bio ?
3. Le score final combine les deux reponses.

## Exports attendus du notebook 1 livre

Exports principaux:

- `data/processed/base_acp_finale_2017.csv`
- `data/processed/base_acp_finale_standardisee_2017.csv`
- `data/processed/dictionnaire_variables_acp_finales.csv`
- `data/processed/controle_completion_acp_finale.csv`
- `data/processed/arbitrage_selection_finale_variables_acp.csv`

Role des fichiers:

- `base_acp_finale_2017.csv`: base analytique non standardisee pour controle et interpretation.
- `base_acp_finale_standardisee_2017.csv`: matrice standardisee pour ACP, CAH et KMeans.
- `dictionnaire_variables_acp_finales.csv`: description, role et justification PESTEL des variables.
- `controle_completion_acp_finale.csv`: controle final avant passage au notebook ACP.
- `arbitrage_selection_finale_variables_acp.csv`: justification des variables retenues/ecartees.

## Message oral court

Le notebook 1 est le socle de confiance du projet. Il ne cherche pas a donner directement le top pays, mais a construire une base propre, auditee et reproductible. Les variables sont selectionnees pour repondre a la question export: demande, accessibilite, dependance, risque et signal premium. Les donnees FiBL et OMC/ADB ne sont pas exclues; elles sont separees du coeur marche pour eviter de melanger le potentiel import general et le signal bio. Elles servent ensuite a affiner la priorisation dans l ACP bio premium.

## Points de vigilance

- Une variable complete techniquement n est pas toujours une variable observee de meme qualite partout.
- Les zeros peuvent representer une absence reelle ou un manque de declaration selon la source.
- Les pays sans ISO3 fiable doivent rester traces.
- Les resultats du notebook 2 dependent directement du jalon fige par le notebook 1.
- Le top pays final doit toujours etre accompagne d un niveau de confiance donnees.
