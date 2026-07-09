# P11 - Etude de marche internationale

## Contexte

Ce projet repond a une mission confiee par le PDG de La poule qui chante.

Objectif business:

- Identifier des groupements de pays a cibler pour exporter des poulets biologiques.
- Proposer une premiere priorisation des marchés (top 5 pays a approfondir).

## Structure du depot

```
notebooks/
    ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb
        # Preparation, nettoyage, EDA et constitution de la base d analyse
    ZAMOUN_Férial_2_clustering_visualisations _112025.ipynb
        # ACP, CAH, KMeans, profils de clusters et recommandation export
scripts/
    data_manager.py                  # Helper d inspection appele par le notebook 1
    enrich_market_features_model.py  # Fonctions testees et smoke-check CI (normalisation, Levenshtein, enrichissements)
tests/
    test_data_prep.py                # Tests normalize_text, add_country_key
    test_enrich_market_features_model.py  # Tests enrichissement, Levenshtein et diversite texte
.github/workflows/ci.yml            # CI: ruff, pytest, smoke checks, VERSION, controle notebooks
requirements.txt
pyproject.toml                      # Config ruff + pytest
VERSION                             # Version courante: 0.1.0
```

Les donnees brutes et fichiers intermediaires lourds sont partiellement ignores via `.gitignore` selon les besoins de versionnage.

La version GitHub montrable est volontairement allegee: elle conserve les deux notebooks finaux, les tests, la documentation, le brief et les scripts minimaux necessaires aux controles. Les donnees lourdes, exports graphiques temporaires, anciens notebooks et notebooks rapatries sont exclus du commit principal.

## Variables du modele (16 variables candidates, 6 dimensions PESTEL+)

| Dimension | Variables |
|---|---|
| Politique | political_stability |
| Economique | gdp_per_capita_usd, ease_business_score, poultry_import_qty_tonnes, poultry_import_value_kusd, poultry_production_2018_tonnes, import_dependency_ratio |
| Social | population, kcal_per_capita_day |
| Technologique | poultry_slaughtered_2018_1000_head |
| Environnemental | losses_ktons |
| Sanitaire | avian_events_recent_2y_count, avian_events_h5n1_count |
| Reglementaire | faolex_texts_recent_10y_count, faolex_texts_active_count, faolex_text_diversity_score |

`faolex_text_diversity_score` est une variable de feature engineering calculee par distance de Levenshtein normalisee sur les titres et resumes des textes FAOLEX.

## Etat technique (rerun complet)

Etat valide apres regeneration des donnees et reexecution des notebooks:

- `notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb` documente la preparation, l EDA, l analyse PESTEL, les controles de representativite et la constitution de la base ACP.
- `notebooks/ZAMOUN_Férial_2_clustering_visualisations _112025.ipynb` consomme la base ACP finale, documente l ACP, la segmentation CAH/KMeans, les profils de clusters et la recommandation finale.

Indicateurs observes dans le rerun courant:

- Base ACP finale: 139 pays dans `base_acp_finale_2017.csv`; projection ACP/clusters exportee sur 138 pays.
- ACP: 11 variables actives resumees en 3 composantes principales PC1 a PC3, conservant 89,90% de variance cumulee.
- Clustering: segmentation KMeans retenue a `k=2`, avec une silhouette autour de 0,60.
- Les solutions a partir de `k=4` fragmentent davantage les groupes et generent des micro-clusters moins exploitables metier.
- Cluster prioritaire ACP: 16 pays, correspondant a des marches a instruire rapidement.
- Entonnoir final du notebook 2: Top 5 candidats fiables = Suisse, Dominique, Emirats arabes unis, Belgique, Autriche; shortlist 3 = Suisse, Dominique, Emirats arabes unis; pays recommande final = Suisse.

Conclusion: la segmentation finale privilegie une lecture simple en 2 clusters; la decision export se fait ensuite au niveau pays en croisant score composite, confiance maximale, accord CAH/KMeans, dimensions ACP et variables metier. La Suisse est le marche prioritaire a instruire, avec Dominique et les Emirats arabes unis comme comparateurs immediats de shortlist.

## Demarrage rapide

```powershell
pip install -r requirements.txt
```

Ouvrir les notebooks dans l ordre :

1. `notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb`
2. `notebooks/ZAMOUN_Férial_2_clustering_visualisations _112025.ipynb`

## Qualite logicielle (CI)

Workflow GitHub Actions dans [.github/workflows/ci.yml](.github/workflows/ci.yml) :

- Lint via `ruff` (`scripts/enrich_market_features_model.py` + tests)
- 16 tests unitaires via `pytest`
- Smoke check des fonctions critiques
- Verification du fichier `VERSION`
- Validation structurelle des deux notebooks livres: JSON nbformat, volume minimal de cellules code/markdown, absence de sorties d'erreur enregistrees
- Execution complete du notebook 1 si les donnees sources `data/raw` sont disponibles dans l'environnement CI

Execution locale :

```powershell
pip install pytest ruff nbformat nbconvert ipykernel
ruff check scripts/enrich_market_features_model.py tests --ignore E501,W293
pytest -q
```

## Livrables

- Notebook 1 : preparation, nettoyage, feature engineering, tests pre-ACP.
- Notebook 2 : ACP + clustering (CAH + KMeans) + entonnoir de recommandation cluster prioritaire -> Top 5 -> shortlist -> pays recommande.
- Helpers Python conserves: inspection notebook et fonctions testees de normalisation/Levenshtein.
- Suite de tests unitaires integree au workflow CI.
- Documentation de soutenance: brief projet, documentation technique et note pipeline.

## Document complementaire

- Brief projet : [PROJECT_BRIEF.md](PROJECT_BRIEF.md)
- Documentation technique : [docs/documentation_technique.md](docs/documentation_technique.md)
- Note pipeline : [docs/note_pipeline_preparation_nettoyage.md](docs/note_pipeline_preparation_nettoyage.md)
