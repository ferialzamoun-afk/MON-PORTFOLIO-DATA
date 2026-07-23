# Documentation technique - P11

## 1. Objet

Ce document decrit l etat technique des livrables P11 apres menage du depot.

Les livrables analytiques de reference sont les deux notebooks presents dans `notebooks/`:

- `ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb`
- `ZAMOUN_Férial_2_clustering_visualisations _112025.ipynb`

La documentation ci-dessous liste uniquement les fichiers `data/raw` et `data/processed` explicitement utilises ou produits par ces notebooks livres.

## 2. Composants Python conserves

### Scripts utilises par les livrables ou les controles

| Fichier | Statut | Usage actuel |
|---|---|---|
| `scripts/data_manager.py` | utilise | importe par le notebook 1 pour `inspecter_dataframe` |
| `scripts/enrich_market_features_model.py` | utilise | fonctions `normalize_text`, `levenshtein_distance`, `text_diversity_score` et chargement CEPII couverts par les tests et le smoke check CI |

Le dossier `src/` ne contient plus de pipeline Python actif dans l etat actuel du workspace. Les references historiques a `src/run_market_study.py`, `src/p11_market/data_prep.py` ou `src/p11_market/modeling.py` ont donc ete retirees.

### Scripts presents mais non utilises par les deux notebooks livres

| Fichier | Observation |
|---|---|
| `scripts/preprocess_dw_csvs.py` | utilitaire historique Data Wrangler, non appele par les notebooks livres |
| `scripts/rebuild_geography_exports.py` | utilitaire historique de reconstruction geographique, non appele par les notebooks livres |
| `scripts/enrich_dataset_template.py` | template d enrichissement, non appele par les notebooks livres |
| `scripts/schema_fr.py` | dictionnaires/schema FR disponibles, non importes par les notebooks livres actuels |

Ces fichiers peuvent etre gardes comme outils annexes, mais ils ne doivent plus etre presentes comme scripts necessaires au rerun des livrables.

## 3. Flux notebook actuel

### 3.1 Notebook 1 - Preparation, nettoyage et EDA

Role: constituer la base ACP finale a partir de sources brutes et d un enrichissement `processed` deja disponible.

Import local:

- `from scripts.data_manager import inspecter_dataframe`

Entrees `data/raw` referencees dans le notebook:

| Fichier | Role |
|---|---|
| `data/raw/1-Collecte des données/DAN-P9-data/DisponibiliteAlimentaire_2017.csv` | disponibilite alimentaire volaille |
| `data/raw/1-Collecte des données/DAN-P9-data/Population_2000_2018.csv` | population pays |
| `data/raw/1-Collecte des données/Données collectées/FAOSTAT_data_Imp_Exp_Poulets_Monde.csv` | imports/exports volaille |
| `data/raw/1-Collecte des données/Données collectées/country_mapping_fr_en_iso.csv` | correspondances pays FR/EN/ISO |
| `data/raw/1-Collecte des données/Données collectées/ease doing of business Data.csv` | facilite d affaires |
| `data/raw/1-Collecte des données/Données collectées/PoliticalStability.csv` | stabilite politique |
| `data/raw/1-Collecte des données/Données collectées/pib.csv` | PIB source principale |
| `data/raw/pib par habitant.csv` | fallback PIB si `pib.csv` est absent |
| `data/raw/1-Collecte des données/Données collectées/geo_cepii.xls` | referentiel geographique CEPII |
| `data/raw/1-Collecte des données/Données collectées/dist_cepii.xls` | distances/proxies logistiques CEPII |
| `data/raw/1-Collecte des données/Données collectées/FAOSTAT_data_Prod_Poulets_Monde.csv` | production/abattage poulets |
| `data/raw/1-Collecte des données/Données collectées/Latest Reported Events.csv` | evenements sanitaires aviaires |
| `data/raw/1-Collecte des données/Données collectées/FAOLEX_Environment.csv` | textes reglementaires FAOLEX |
| `data/raw/1-Collecte des données/Données collectées/dim_pays_enriched.csv` | dictionnaire pays enrichi |

Entree `data/processed` referencee par le notebook 1:

| Fichier | Role |
|---|---|
| `data/processed/market_features_ready_omc_fibl_fe.csv` | base enrichie OMC/ADB + FiBL + feature engineering bio/import, utilisee si disponible |

Sorties `data/processed` produites par le notebook 1:

| Fichier | Role |
|---|---|
| `controle_representativite_pays_population.csv` | controle couverture pays/population |
| `base_intermediaire_fusion_pays_2017.csv` | base fusionnee avant nettoyage final |
| `base_intermediaire_fusion_pays_2017_sans_nan.csv` | base intermediaire apres traitement des NaN bloquants |
| `controle_variables_base_sans_nan.csv` | audit variables post-nettoyage |
| `controle_correlations_fortes_base_sans_nan.csv` | controle correlations fortes |
| `selection_variables_post_fusion.csv` | selection de variables apres fusion |
| `base_selectionnee_post_fusion_2017.csv` | base selectionnee avant feature engineering final |
| `base_feature_engineered_2017.csv` | base avec variables derivees |
| `variables_creees_feature_engineering.csv` | inventaire des variables creees |
| `stats_descriptives_base_feature_engineered.csv` | statistiques descriptives |
| `controle_outliers_iqr_base_feature_engineered.csv` | synthese outliers IQR |
| `detail_outliers_iqr_base_feature_engineered.csv` | detail outliers IQR |
| `base_pre_standardisation_acp_2017.csv` | base prete avant standardisation ACP |
| `controle_pre_standardisation_acp.csv` | controle pre-standardisation |
| `apercu_variables_standardisees_zscore.csv` | apercu variables standardisees |
| `matrice_correlation_pearson_variables_candidates.csv` | matrice Pearson candidates |
| `matrice_correlation_spearman_variables_candidates.csv` | matrice Spearman candidates |
| `rapport_colinearite_variables_candidates.csv` | rapport colinearite |
| `paires_colinearite_pearson_forte_variables_candidates.csv` | paires Pearson fortement correlees |
| `paires_colinearite_spearman_forte_variables_candidates.csv` | paires Spearman fortement correlees |
| `arbitrage_selection_finale_variables_acp.csv` | arbitrage final variables ACP |
| `base_acp_finale_2017.csv` | base finale non standardisee transmise au notebook 2 |
| `base_acp_finale_standardisee_2017.csv` | base standardisee utilisee par ACP/CAH/KMeans |
| `controle_colinearite_base_acp_finale.csv` | controle colinearite final |
| `dictionnaire_variables_acp_finales.csv` | dictionnaire final variables actives et traces qualite |
| `controle_completion_acp_finale.csv` | controle de completion des bases finales |

### 3.2 Notebook 2 - ACP, clustering et decision export

Role: consommer les sorties finales du notebook 1, realiser ACP + clustering, puis exporter les tableaux de decision.

Entrees `data/processed` obligatoires:

| Fichier | Role |
|---|---|
| `data/processed/base_acp_finale_2017.csv` | base pays non standardisee pour controle et interpretation |
| `data/processed/base_acp_finale_standardisee_2017.csv` | matrice standardisee pour ACP, CAH et KMeans |
| `data/processed/dictionnaire_variables_acp_finales.csv` | dictionnaire des variables transmises |
| `data/processed/controle_completion_acp_finale.csv` | controle de completion lu si disponible |

Sorties `data/processed/decision_export` produites par le notebook 2:

| Fichier | Role |
|---|---|
| `decision_export_scores.csv` | scores export complets et segment de decision |
| `top5_decision_export_synthese.csv` | top 5 final de decision export |
| `top10_decision_export.csv` | top 10 de decision export |
| `top20_recommandations_decision_export.csv` | top 20 avec recommandations finales |
| `segments_decision_export_synthese.csv` | synthese des segments de priorite export |
| `tests_robustesse_segments_decision_export.csv` | tests de robustesse des segments de decision |
| `zamoun_acp_projection_clusters.csv` | projection des pays et labels de clusters |
| `zamoun_acp_cluster_profiles.csv` | profils de clusters |
| `zamoun_acp_cluster_summary.csv` | synthese interpretable des clusters |
| `zamoun_acp_variable_loadings.csv` | contributions/loadings des variables ACP |

## 4. Resultats analytiques documentes

Etat courant de la chaine livree:

- Base ACP finale: 139 pays dans `base_acp_finale_2017.csv`; projection ACP/clusters exportee sur 138 pays.
- ACP: 11 variables actives; les 3 premieres composantes sont retenues pour le clustering et conservent 89,90% de variance cumulee.
- Clustering: KMeans retenu a `k=2`, avec une silhouette autour de 0,60.
- Cluster prioritaire ACP: 16 pays, avec notamment CHE, BEL, AUT, LVA, EST, SWE, SVN et ESP dans les premiers pays du cluster.
- Entonnoir final du notebook 2: Top 5 candidats fiables = Suisse, Dominique, Emirats arabes unis, Belgique, Autriche; shortlist 3 = Suisse, Dominique, Emirats arabes unis; pays recommande final = Suisse.
- Point de vigilance documentaire: les fichiers `top5_decision_export_synthese.csv` et `top10_decision_export.csv` correspondent a un scoring export intermediaire. La recommandation finale est calculee ensuite dans la synthese du notebook 2, apres filtrage des candidats prioritaires fiables et construction de la shortlist 3.

## 5. Tests et qualite logicielle

La suite de tests actuelle contient 16 tests unitaires:

| Fichier | Couverture principale |
|---|---|
| `tests/test_data_prep.py` | normalisation texte et creation locale de `country_key` |
| `tests/test_enrich_market_features_model.py` | Levenshtein, score de diversite textuelle, proxy logistique CEPII |

Execution locale:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## 6. GitHub Actions

Workflow: `.github/workflows/ci.yml`

Controles executes sur push et pull request:

1. Installation des dependances projet et outils de controle (`pytest`, `ruff`, `nbformat`, `nbconvert`, `ipykernel`).
2. Verification de presence du fichier `VERSION`.
3. Lint cible sur `scripts/enrich_market_features_model.py` et `tests/`.
4. Suite unitaire `pytest -q`.
5. Validation structurelle des deux notebooks livres: JSON nbformat, seuil minimal de cellules code/markdown, absence de sorties d erreur enregistrees.
6. Execution complete du notebook 1 uniquement si `data/raw` est disponible dans l environnement CI.
7. Smoke check des fonctions critiques importees depuis `scripts/enrich_market_features_model.py`.

## 7. Reproductibilite attendue

Ordre de lecture/rejeu:

1. Notebook 1: preparation/nettoyage/EDA, generation des bases ACP finales.
2. Notebook 2: ACP, CAH, KMeans, profils et exports de decision.
3. Tests: `pytest -q` via GitHub Actions et localement via le `.venv`.

Les fichiers `data/raw` lourds peuvent rester hors versionnement. Dans ce cas, le CI garde les controles de structure et les tests unitaires, mais saute l execution complete du notebook 1.
