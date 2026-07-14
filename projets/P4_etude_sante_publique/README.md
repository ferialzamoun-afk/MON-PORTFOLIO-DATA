# 🌍 P4 — Étude de Santé Publique : Sous-nutrition mondiale (FAO 2017)

> **Type** : Analyse exploratoire · Données FAO · Indicateurs nutritionnels
> **Date** : 2024 · Périmètre : mondial · Année de référence : 2017
> **Formation** : Data Analyst — GRETA Promo 2025

---

## 🎯 1. Contexte et besoin métier

Ce projet répond à une problématique de santé publique internationale : évaluer la situation de sous-nutrition et la disponibilité alimentaire mondiale à partir des données FAO 2017.

**Pour qui** : organisations de pilotage alimentaire international, acteurs de la sécurité alimentaire.

**Problème** : les données FAO sont hétérogènes, multi-sources, en unités non homogènes — impossible d'en tirer des constats comparables sans préparation structurée.

**Enjeux** :
- Estimer la proportion de population en sous-nutrition
- Calculer combien de personnes pourraient être nourries selon différents besoins caloriques
- Analyser la répartition de la disponibilité alimentaire intérieure (humain, animal, pertes, autres)

**Sources exploitées** :
- population.csv — Population par pays/continent
- dispo_alimentaire.csv — Disponibilité alimentaire intérieure
- ide_alimentaire.csv — Flux d'aide alimentaire
- sous_nutrition.csv — Données de sous-nutrition par pays

**Périmètre** : année 2017 · granularité pays/zone · regroupement complémentaire par continent · scénarios nutritionnels comparés : 1 500, 2 500 et 3 000 kcal/jour/personne

---

## 🧭 2. Démarche analytique

**Hypothèses méthodologiques** :
- Harmonisation des unités : conversions systématiques (milliers de tonnes → kg)
- Périmètre 2017 : année la plus complète dans les sources FAO
- Mapping pays-continent construit manuellement (industrialisable)

**Étapes** :
1. Chargement et contrôle des données (types, dimensions, valeurs manquantes)
2. Nettoyage et standardisation (renommage colonnes, conversions d'unités, gestion NaN)
3. Jointures entre jeux de données (population × sous-nutrition × disponibilité alimentaire)
4. Calcul des indicateurs métier :
   - Proportion de sous-nutrition par pays/région
   - Couverture théorique alimentaire selon 3 scénarios caloriques
   - Couverture théorique d'origine végétale
   - Répartition disponibilité intérieure (humain / animal / pertes / autres usages)
5. Restitution via tableaux de synthèse et visualisations (camemberts, tableaux scénarios)

**Limites identifiées** :
- Mapping pays-continent manuel → peut être industrialisé
- Hypothèses nutritionnelles simplificatrices → affinables par profil de population
- Une étape suivante serait un tableau de bord interactif pour comparer les régions dans le temps

---

## 📊 3. Résultats et livrables

| Livrable | Description |
|---------|-------------|
| Notebook d'analyse | Pipeline complet import → préparation → analyses → visualisations |
| Estimation sous-nutrition | Population en sous-nutrition estimée sur le périmètre 2017 |
| Simulations caloriques | Couverture alimentaire selon 3 hypothèses (1 500 / 2 500 / 3 000 kcal) |
| Analyse des usages | Répartition alimentation humaine, animale, pertes et autres usages |
| Support de présentation | Synthèse orale structurée |

---

## 🎓 4. Compétences RNCP 37837 mobilisées

| Bloc | Compétence | Ce qui a été fait | Preuve |
|------|-----------|------------------|--------|
| **BC02** | Identifier et collecter | Exploitation de 4 sources FAO hétérogènes | ssets/Template+Férial+V1.ipynb |
| **BC02** | Extraire et agréger | Conversions d'unités, jointures multi-sources | Étapes 1-3 du notebook |
| **BC02** | Traiter les données manquantes | Nettoyage, gestion NaN, standardisation | Étape 2 du notebook |
| **BC02** | Analyse temporelle | Focus 2017, lecture de la disponibilité annuelle | Étape 3 du notebook |
| **BC02** | Analyse univariée/multivariée | Stats descriptives, distributions, corrélations | Étape 4 du notebook |
| **BC03** | Solution de visualisation | Camemberts, tableaux scénarios, comparaisons | Étape 5 du notebook |
| **BC03** | Récit des résultats | Narration des constats pour un public non technique | Support de présentation |
| **BC04** | Identifier le besoin métier | Traduction des enjeux FAO en indicateurs actionnables | Contexte du notebook |

---

## 💡 5. Impact et apprentissages

**Ce que ça a apporté** : une meilleure lisibilité des leviers potentiels sur la sécurité alimentaire — disponibilité alimentaire, pertes, arbitrages d'usage.

**Veille métier** : enjeux de sécurité alimentaire (sous-nutrition, disponibilité, pertes) → traduction en indicateurs actionnables.

**Veille technologique** : bonnes pratiques d'analyse exploratoire Python (pandas, nettoyage, jointures) → pipeline reproductible par étapes avec conversion systématique des unités.

**Suite naturelle** : création d'un tableau de bord interactif pour comparer les régions dans le temps et anticiper les risques.

---

## 🔗 Ressources

- Notebook principal : ssets/Zamoun_Ferial_1_notebook_112025.ipynb
- Présentation : ssets/Zamoun_Férial_1_presentation_112025.pdf

---

*Férial Zamoun · Formation Data Analyst GRETA Promo 2025 · [GitHub](https://github.com/ferialzamoun-afk)*
