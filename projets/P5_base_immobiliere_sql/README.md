# 🏠 P5 — Base Immobilière SQL : Indicateurs de Marché

> **Type** : SQL · Base de données relationnelle · Analyse marché immobilier
> **Date** : 2024
> **Formation** : Data Analyst — GRETA Promo 2025

---

## 🎯 1. Contexte et besoin métier

Analyser le marché immobilier via une base de données relationnelle pour construire une vision analytique des prix et volumes de transactions.

**Pour qui** : acteurs du secteur immobilier souhaitant piloter la dynamique des ventes et comparer les performances géographiques.

**Problème** : les données immobilières sont stockées en base relationnelle mais pas encore interrogées de façon structurée pour produire des indicateurs de marché fiables.

**Enjeux** :
- Suivre les dynamiques de prix par zone géographique
- Comparer les volumes d'activité entre secteurs
- Identifier les tendances et signaux d'alerte sur le marché

**Périmètre** : base relationnelle immobilière, structurée via un dictionnaire de données projet pour cadrer les entités et attributs.

---

## 🧭 2. Démarche analytique

**Étapes** :
1. Cadrage des entités et attributs via le dictionnaire de données
2. Vérification de la cohérence des champs utilisés pour les analyses
3. Construction de requêtes SQL d'analyse (sélection, agrégation, filtres, comparaisons)
4. Production d'indicateurs métier sur les prix et les volumes
5. Interprétation des résultats dans une logique d'aide à la décision

**Limites** :
- Les performances de requêtes peuvent être améliorées via indexation selon les usages
- La qualité des analyses dépend de la granularité et de la complétude des données sources

---

## 📊 3. Résultats et livrables

| Livrable | Description |
|---------|-------------|
| Dictionnaire de données | Description des entités, attributs et définitions métier |
| Scripts SQL | Requêtes d'analyse prix/volume documentées |
| Support de présentation | Synthèse des analyses et conclusions métier |

---

## 🎓 4. Compétences RNCP 37837 mobilisées

| Bloc | Compétence | Ce qui a été fait | Preuve |
|------|-----------|------------------|--------|
| **BC01** | Créer une base de données | Structuration du modèle relationnel immobilier | Dictionnaire de données |
| **BC01** | Stratégie de requêtes SQL | Requêtes d'analyse prix, volumes, comparaisons géo | Scripts SQL |
| **BC01** | Gérer une base de données | Vérification cohérence des champs, clés, relations | Étape 2 de la démarche |
| **BC02** | Extraire et agréger | KPI immobiliers via agrégations SQL | Scripts SQL |
| **BC02** | Vérifier la cohérence | Contrôle des jointures et cohérence des résultats | Rapport de vérification |
| **BC03** | Présenter les résultats | Synthèse pour un public métier non technique | Support de présentation |
| **BC04** | Identifier le besoin métier | Enjeux immobiliers → questions SQL orientées pilotage | Dictionnaire de données |
| **BC04** | Gérer la documentation | Dictionnaire de données + scripts commentés | Livrables documentés |

---

## 💡 5. Impact et apprentissages

**Ce que ça a apporté** : capacité à transformer une base immobilière en vision analytique exploitable pour le pilotage stratégique et opérationnel.

**Veille métier** : enjeux d'analyse du marché immobilier (évolution des prix, dynamique des ventes, comparaisons territoriales) → traduction en questions SQL orientées pilotage.

**Veille technologique** : bonnes pratiques SQL (structuration relationnelle, jointures, agrégations, lisibilité) → approche progressive du simple vers l'agrégé pour fiabiliser les résultats.

**Suite naturelle** : mise en place d'un tableau de bord automatisant les KPI immobiliers avec mise à jour périodique.

---

## 🔗 Ressources

- Dictionnaire de données : ssets/Zamoun_Férial_1_dictionnaire_de_donnees_24112025.xlsx
- Présentation : ssets/Zamoun_Férial_1_presentation_112025.pdf

---

*Férial Zamoun · Formation Data Analyst GRETA Promo 2025 · [GitHub](https://github.com/ferialzamoun-afk)*
