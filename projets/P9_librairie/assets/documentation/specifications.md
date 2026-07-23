# Specifications fonctionnelles – P9 Lapage

## 1) Perimetre

Analyse des ventes de la librairie Lapage a partir de trois tables sources : clients, produits, transactions.

## 2) Sources de donnees

| Fichier | Contenu | Cle |
|---|---|---|
| `data/raw/customers.csv` | Profils clients (age, sexe, localisation) | `client_id` |
| `data/raw/products.csv` | Catalogue produits (categorie, prix) | `product_id` |
| `data/raw/transactions.csv` | Historique des achats | `client_id`, `product_id`, `date` |

## 3) Indicateurs cles (KPI)

| Indicateur | Definition | Granularite |
|---|---|---|
| CA total | Somme des montants transactions | Global, mensuel, par categorie |
| Panier moyen | CA / nombre de transactions | Global, par segment client |
| Indice de Gini | Concentration du CA entre clients | Global |
| Part de CA par categorie | CA categorie / CA total | Par categorie produit |
| Frequence d'achat | Nombre de transactions par client | Par client |

## 4) Regles de gestion

- Une transaction est valide si `montant > 0` et `date` non nulle.
- Les doublons sur (`client_id`, `product_id`, `date`) sont supprimes (conservation du premier enregistrement).
- Les clients sans transaction sont exclus des analyses de segmentation.
- Les aggregations temporelles utilisent le mois calendaire (YYYY-MM).

## 5) Tests statistiques appliques

| Test | Variables | Condition d'application |
|---|---|---|
| Pearson | Deux variables numeriques continues | Distribution approximativement normale |
| Spearman | Deux variables numeriques (dont ordinales) | Distribution non normale ou presence de rangs |
| Chi-2 | Deux variables categoriques | Effectifs theoriques >= 5 par case |
| Mann-Whitney | Comparaison de deux groupes numeriques | Distribution non normale |

## 6) Livrables attendus

- Notebooks documentes (01, 02, 03) avec conclusions interpretees.
- Dashboard Streamlit multi-pages avec filtres interactifs.
- Exports Excel des KPI dans `lapage_project/outputs/`.
- Figures de reporting dans `lapage_project/outputs/figures/`.
