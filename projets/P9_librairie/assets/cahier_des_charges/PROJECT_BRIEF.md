# PROJECT BRIEF - P9

## 1) Contexte

Lapage est une librairie souhaitant mieux comprendre ses donnees de vente pour optimiser sa strategie commerciale et marketing.
La mission consiste a realiser une analyse data-driven des ventes, des comportements clients et des tendances temporelles.

## 2) Problematique

Quels segments clients, quelles categories de produits et quelles tendances temporelles permettent d'expliquer la performance commerciale de Lapage et d'orienter les decisions strategiques du CODIR ?

## 3) Objectifs de la mission

- Analyser la performance commerciale (CA, panier moyen, concentration des ventes, saisonnalite).
- Segmenter les clients selon leur comportement d'achat (frequence, categories, profils).
- Identifier les leviers marketing et les opportunites de croissance.
- Produire des livrables exploitables : notebooks, dashboard interactif, exports KPI.

## 4) Donnees mobilisees

| Source | Description |
|---|---|
| `data/raw/customers.csv` | Profils clients (age, sexe, localisation) |
| `data/raw/products.csv` | Catalogue produits (categorie, prix) |
| `data/raw/transactions.csv` | Historique des transactions |

- **Volume** : environ 8 600 clients, CA annuel ~480 000 €.
- **Concentration** : indice de Gini ~0.40 (concentration modéree).

## 5) Feature engineering realise

- Fusion des trois tables sur `client_id` et `product_id`.
- Creation de variables derivees : panier moyen, frequence d'achat, RFM simplifie.
- Calcul des parts de CA par categorie et par tranche d'age.
- Agregations temporelles (mensuel, trimestriel) pour l'analyse des tendances.
- Tests statistiques : correlation de Pearson, Spearman, test du chi-2, test de Mann-Whitney.

## 6) Resultats

- **CA annuel** : ~480 000 € sur 8 600 clients.
- **Concentration** : Gini ~0.40 — pas de surconcentration critique.
- **Segments identifies** : profils B2C distincts par frequence et categorie de produit.
- **Dashboard Streamlit** multi-pages deployé pour le CODIR.
- **Exports KPI** : tableaux Excel et figures de reporting.

## 7) Methodologie

### Etape A - Exploration et nettoyage (Notebook 01)
- Controle qualite des trois fichiers sources, gestion des doublons et valeurs manquantes.
- EDA : distributions, valeurs aberrantes, coherence temporelle.

### Etape B - Analyses marketing et BI (Notebook 02)
- Analyse des tendances de CA (mensuel, saisonnier).
- Segmentation clients par comportement d'achat.
- Top produits et categories, analyse du panier moyen.

### Etape C - Analyses statistiques (Notebook 03)
- Tests de correlation entre variables numeriques (Pearson, Spearman).
- Tests d'independance (chi-2) entre variables categoriques.
- Comparaison de groupes (Mann-Whitney).

### Etape D - Dashboard et livrables
- Application Streamlit multi-pages pour la visualisation interactive des KPI.
- Exports Excel des indicateurs cles pour le reporting.

## 8) Livrables

- `lapage_project/notebooks/analyses/01_Exploration_et_nettoyage.ipynb` : EDA, nettoyage, base de donnees consolidee.
- `lapage_project/notebooks/analyses/02_Analyses_Marketing.ipynb` : performance commerciale, segmentation client.
- `lapage_project/notebooks/analyses/03_Analyses_Statistiques.ipynb` : tests statistiques, correlations, comparaisons.
- `lapage_project/dashboard/` ou `Streamlit/` : application Streamlit multi-pages.
- `lapage_project/outputs/` : exports KPI Excel et figures de reporting.

## 9) Criteres de qualite

- Analyses reproductibles : notebooks documentes, fonctions mutualisees dans `src/`.
- Tests statistiques justifies (choix du test selon la nature des variables).
- Dashboard exploitable par des non-techniciens (CODIR).
- Exports KPI structures et prets a l'emploi.

## 10) Limites et risques

- Donnees simulees/pedagogiques : les conclusions sont illustratives, pas operationnelles.
- Segmentation simplifiee (pas de clustering ML) : approche analytique directe.
- Dashboard non deploye en production : execution locale ou Streamlit Cloud.
