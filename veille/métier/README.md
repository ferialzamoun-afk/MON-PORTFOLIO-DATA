# 📊 Veille Métier — Ferial Zamoun
**Data Analyst — RNCP 37837 — 2024-2026**

> *Objectif : rester à jour sur les enjeux métier des secteurs dans lesquels les projets de formation s'inscrivent, et identifier les besoins analytiques récurrents en entreprise.*

---

## 1. Domaines Métier Couverts par les Projets

| Domaine | Projet(s) | Problématique métier |
|---------|-----------|---------------------|
| **Commerce & Distribution** | P6, P9, P13, P14 | Optimisation des ventes, analyse de la valeur client, ruptures de stock |
| **Éducation & RH** | P8 | Représentativité étudiants, égalité F/H, recrutement ciblé |
| **Santé publique** | P4, P12 | Détection de fraude (billets), indicateurs épidémiologiques |
| **Eau & Développement** | P10 | Accès à l'eau potable, indicateurs ODD, pilotage international |
| **Immobilier** | P5 | Analyse de marché, prix, dynamiques territoriales |
| **Alimentation** | P11 | Étude de marché, segmentation pays, recommandations export |
| **IT / Services numériques** | P7 | Reporting décisionnel, suivi commercial multi-persona |

---

## 2. Enjeux Métier Identifiés par Secteur

### 🛒 Commerce & Retail (P6, P9, P13, P14)

**Contexte observé :**
- Les équipes métier manquent de KPIs actionnables en temps réel.
- Les données ERP et web sont souvent **désynchronisées** (111 produits non-appariés dans P6).
- Les ruptures de stock représentent un **coût invisible** mal mesuré.

**Besoins analytiques identifiés :**
- Taux de pénétration produit par région / canal
- Analyse des marges négatives
- Segmentation client (RFM, comportement d'achat)
- Détection d'anomalies dans les flux de commandes

**Sources :**
- 📰 INSEE — données consommation des ménages
- 📰 Fevad (e-commerce) — rapports annuels
- 📄 Cours OC P6, P9, P14

---

### 🎓 Éducation & Égalité professionnelle (P8)

**Contexte observé :**
- Obligation légale de publication de l'Index Égalité F/H depuis 2019 (loi "Pour la liberté de choisir son avenir professionnel").
- Sous-représentation des femmes dans les filières tech (≈ 25-30% en France selon INSEE 2023).
- Besoin de segmentation fine par région, âge, genre pour cibler les actions RH.

**Besoins analytiques identifiés :**
- Calcul de l'écart de représentation OC vs population française (INSEE)
- Taux de pénétration par région
- Identification des groupes d'âge sous-représentés
- Indicateurs de tendance annuelle (2022-2025)

**Sources :**
- 📄 [INSEE — Estimations de population par département, sexe, âge (2025)](https://www.insee.fr)
- 📰 [Rapport Index Égalité F/H — Ministère du Travail 2024](https://travail-emploi.gouv.fr)
- 📰 Eurostat — Women in digital sector

---

### 🌊 Eau potable & Développement (P10)

**Contexte observé :**
- 2,2 milliards de personnes n'ont pas accès à l'eau potable (OMS 2022).
- Les ODD (Objectifs de Développement Durable) fixent des cibles mesurables à 2030.
- Les ONG et agences internationales ont besoin de dashboards **comparatifs multi-pays**.

**Besoins analytiques identifiés :**
- Clustering pays par niveau d'accès à l'eau
- Corrélation instabilité politique / accès eau
- Taux de mortalité attribuable à l'eau non-traitée
- Priorisation des pays pour interventions

**Sources :**
- 📄 [WHO/UNICEF Joint Monitoring Programme (JMP)](https://washdata.org)
- 📄 [Banque Mondiale — Open Data](https://data.worldbank.org)
- 📰 Rapport ODD 2023 (Nations Unies)

---

### 🏦 Sécurité financière & Fraude (P12)

**Contexte observé :**
- La fraude aux billets représente plusieurs centaines de millions d'euros/an en Europe (Rapport BCE 2023).
- Les modèles de ML permettent une détection quasi-temps réel avec >97% de précision.

**Besoins analytiques identifiés :**
- Classification binaire (vrai/faux billet)
- Feature engineering sur les dimensions physiques
- Déploiement API pour intégration aux systèmes de caisse

**Sources :**
- 📄 [Rapport annuel BCE — contrefaçons 2023](https://www.ecb.europa.eu)
- 📰 Europol — Economic Crime Report

---

### 🍽️ Agroalimentaire & Export (P11)

**Contexte observé :**
- La France est le 2e exportateur mondial de produits agroalimentaires (FranceAgriMer 2023).
- L'étude de marché internationale nécessite une segmentation pays multi-critères.

**Besoins analytiques identifiés :**
- ACP + Clustering pour regrouper les pays selon leur profil nutritionnel / économique
- Recommandations de marchés cibles
- Indicateurs : PIB/habitant, taux malnutrition, disponibilité alimentaire

**Sources :**
- 📄 [FAO — Food and Agriculture Data (FAOSTAT)](https://www.fao.org/faostat)
- 📰 FranceAgriMer — panorama des exportations

---

## 3. Méthodes d'Analyse Identifiées et Justifiées

| Méthode | Projets | Justification métier |
|---------|---------|---------------------|
| **Analyse exploratoire (EDA)** | Tous | Toujours première étape : comprendre les distributions, valeurs manquantes, outliers avant toute modélisation |
| **Tests statistiques** (Shapiro-Wilk, Chi2, Mann-Whitney) | P9 | Valider scientifiquement les hypothèses avant conclusions métier (ex : différence de comportement H/F) |
| **ACP (Analyse en Composantes Principales)** | P10, P11 | Réduction de dimensions pour des datasets multi-variables → lisibilité des clusters |
| **Clustering K-Means** | P10, P11 | Segmentation non supervisée — identifier des groupes homogènes sans label a priori |
| **Régression logistique** | P12 | Modèle interprétable, adapté à la classification binaire avec contraintes réglementaires |
| **Modèle en étoile (Star Schema)** | P7, P10, P14 | Standard DWH pour Power BI — performance optimale sur grandes tables de faits |
| **Pipeline ELT (dbt)** | P8 | Transformation in-warehouse — plus scalable qu'ETL classique sur Snowflake |
| **Analyse Pareto (80/20)** | P6, P13 | Identification des 20% de produits/problèmes générant 80% des impacts |

---

## 4. Tendances Métier Suivies (2024-2026)

| Tendance | Impact sur mon profil | Source |
|----------|----------------------|--------|
| **IA Générative en Data** | Gouvernance des prompts, traçabilité (P13), augmentation de la productivité analytique | IA Act EU, OpenAI Dev Days 2024 |
| **Data Mesh** | Architecture décentralisée — chaque domaine métier propriétaire de ses données | Zhamak Dehghani — *Data Mesh* (O'Reilly) |
| **Real-time Analytics** | Demande croissante de dashboards temps réel vs batch quotidien | Snowflake Summit 2024, Confluent (Kafka) |
| **MLOps** | Industrialisation des modèles ML — monitoring drift, CI/CD modèles | ML Engineering (Chip Huyen), Evidently AI |
| **RGPD & Privacy by Design** | Anonymisation des données, gestion consentement — appliqué P8 (données étudiants) | CNIL guides 2024 |

---

## 5. Ressources Métier Consultées

| Source | Domaine | Format |
|--------|---------|--------|
| [INSEE](https://www.insee.fr) | Démographie, économie France | Open Data, rapports |
| [FAO FAOSTAT](https://www.fao.org/faostat) | Alimentation mondiale | Open Data |
| [Banque Mondiale Open Data](https://data.worldbank.org) | Développement international | Open Data |
| [Kaggle Datasets](https://www.kaggle.com/datasets) | Benchmarks ML, datasets variés | Datasets, notebooks |
| [Data.gouv.fr](https://www.data.gouv.fr) | Données publiques françaises | Open Data |
| [Ministère du Travail — Index Égalité](https://travail-emploi.gouv.fr) | Égalité F/H | Rapports annuels |
| [BCE — Contrefaçons](https://www.ecb.europa.eu) | Fraude financière | Rapports annuels |
| OpenClassrooms (cours métier) | Formation | Vidéos, PDF |

---

*Dernière mise à jour : Juillet 2026*
