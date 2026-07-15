# 📋 Proof Points Synthétiques — Portfolio Complet

**Format condensé** pour recruteurs/clients : 1 page par projet avec les 5 piliers essentiels.

> **Utilisation** : À imprimer/partager avant entretien ou pour rappel rapide de chaque réalisation.

---

## 🎯 P6 — Optimisation Boutique (Bottleneck)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | Boutique multi-source (ERP, Web, Liaison) désynchronisée. Besoin : single source of truth pour ventes/stocks/prix. |
| **2️⃣ Données** | 3 Excel sources (doublons/incohérences). ⚠️ Valeurs manquantes, décalages prix/stocks. Limites : snapshot unique, pas historique. |
| **3️⃣ Démarche** | **Python/Pandas** → Chargement → EDA → Fusion cross-source → Nettoyage (Z-score) → Analyses avancées (Pareto, corrélations) → Excel export. |
| **4️⃣ Résultats** | ✅ Doublons détectés/corrigés ; anomalies stocks identifiées ; outliers prix flagués. **Recommandations** : Synchroniser ERP/Web ; piloter marges. **Livrable** : `df_final.xlsx`. |
| **5️⃣ Limites** | Snapshot statique. Pas accès live sources. **Pistes** : Warehouse temps réel (dbt/Snowflake). |

**🔗 Liens** : [GitHub P13 - P6 amélioré](https://github.com/ferialzamoun-afk/P13/tree/main/Partie_1/P6_ameliore_IA) | [Notebook](https://github.com/ferialzamoun-afk/P13/blob/main/Partie_1/P6_ameliore_IA/bottleneck_analyse_ameliore_final.ipynb)

---

## 📊 P7 — Dashboard Gouvernance Projets (SANITORAL)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | SANITORAL : 3 personas (DG, DR, DP) besoin reporting consolidé coût/délai/avancement projets. Enjeu : arbitrage rapide comité pilotage. |
| **2️⃣ Données** | Données internes SANITORAL (portefeuille IT/Marketing). ✅ Complètes. Limites : pas données externes. |
| **3️⃣ Démarche** | **Power BI Desktop** → Star schema (Fact/Dim) → 3 dashboards persona-spécifiques → KPI cards (seuil alerte 15%) → Support soutenance. |
| **4️⃣ Résultats** | Dashboard DG/DR/DP differentiated ; alertes immédiates (>15% écart) ; narration décision-first. **Impact** : Temps décision comité réduit. |
| **5️⃣ Limites** | Référentiel phases à valider (A-F vs 1-4). Processus mise à jour à industrialiser. **Pistes** : Monitoring alertes temporel. |

**🔗 Liens** : [Assets P7](https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA/tree/main/projets/P7_dashboard_powerbi/assets)

---

## 📚 P8 — OC vs INSEE (Data Engineering & dbt)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | OpenClassrooms : comprendre couverture géographique vs INSEE. Enjeu RH/marketing : recruter régions sous-représentées, cibler groupes d'âge oubliés. |
| **2️⃣ Données** | OC (2022-2025) + INSEE (pop. région/genre/âge). ✅ Harmonisées. ⚠️ Lag estimations post-2024 ; pas dissimulation genre. |
| **3️⃣ Démarche** | **dbt 1.11.3 + Snowflake** → Staging (harmonisation) → Intermediate (FULL JOIN) → Marts (export) → CSV export CI/CD GitHub Actions. |
| **4️⃣ Résultats** | KPIs : Taux pénétration OC 2.3% ; gap régional Île-de-France 5.1% vs Auvergne 1.9% ; +4% femmes. **Recommandations** : Recruitement Sud. **Livrable** : CSV (633 lignes) Power BI. |
| **5️⃣ Limites** | OC data anonyme ; analyse descriptive. **Pistes** : Prédictions régionales ; tableau temps réel Streamlit. |

**🔗 Liens** : [GitHub P8--DBT](https://github.com/ferialzamoun-afk/P8--DBT) | [Workflow CI/CD](https://github.com/ferialzamoun-afk/P8--DBT/actions)

---

## 📖 P9 — Analyse Ventes Lapage (BI & Analytics)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | Lapage (librairie) : insights ventes pour piloter CA, détecter best-sellers, segmenter clientèle. De statique → dashboard interactif. |
| **2️⃣ Données** | 3 CSV (customers 1.2k, products 500, transactions 15k). ✅ Complètes/propres. Limites : snapshot annuel, pas données externes. |
| **3️⃣ Démarche** | **Python/Pandas + Streamlit** → EDA → Segmentation (Pareto, RFM) → Tests stats (corrélations Quanti) → Streamlit (filtres interactifs) + Excel KPI. |
| **4️⃣ Résultats** | CA mensuel ; concentration clients (top 20% = 80% CA) ; catégories top/flop ; segmentation B2B/B2C. **Recommandations** : Fidéliser top 20% ; pousser faibles. **Livrables** : Dashboard Streamlit + KPI Excel. |
| **5️⃣ Limites** | Données fournies (pas live). Descriptive only. **Pistes** : Churn ML ; LTV ; recommandation produits. |

**🔗 Liens** : [GitHub Analyses](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies) | [Dashboard Streamlit](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/)

---

## 🌍 P10 — Dashboard Eau Potable (Power BI & Langage M)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | ODD ONU : 2.2B sans accès eau potable. Enjeu décideur/ONG : identifier régions prioritaires, évaluer stabilité politique vs accès WASH. |
| **2️⃣ Données** | 5 sources (Banque Mondiale, UN régions, stabilité politique, mortalité WASH, services eau) × 150+ pays × 20 ans. ✅ Harmonisées. ⚠️ Lag estimations. |
| **3️⃣ Démarche** | **Python + Langage M (Power Query) + Power BI** → Schéma canonique → Fact/Dim tables (star) → Visualisations (choroplethe, heatmap, top N ranking). |
| **4️⃣ Résultats** | 200 pays classés accès eau vs stabilité ; 5 clusters zones critiques ; trajectoires 2000-2024. **Recommandations** : Top 20 prioritaires (<50% accès). **Livrable** : Dashboard Power BI 5 pages + CSV étoile (180k lignes). |
| **5️⃣ Limites** | Pas données ICP ; modèle descriptif. **Pistes** : Données satellite ; ML clustering validé ; tableau temps réel API. |

**🔗 Liens** : [GitHub P10](https://github.com/ferialzamoun-afk/P10)

---

## 🌐 P11 — Étude Marché Export Poulets Bio (Clustering & ACP)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | "La Poule qui Chante" : identifier marchés cibles export poulets bio. Enjeu : grouper 195 pays par profil pour concentrer efforts (top 5 first). |
| **2️⃣ Données** | 7 datasets FAO/Banque Mondiale (16 variables PESTEL: GDP, import dependency, avian flu events, FAOLEX régulations). ⚠️ Couverture 139 pays, valeurs manquantes régionales. |
| **3️⃣ Démarche** | **Python (scikit-learn)** → Prep + feature engineering (Levenshtein) → ACP (11 actives → 3 PC, 89.9% variance) → CAH/KMeans (clustering) → Profils recommandation. |
| **4️⃣ Résultats** | 5 clusters profils marché (Import-dépendant stable / Croissance volailles forte / Régulation restrictive). Top 5 : Pays X (margin haute) → Pays Y (faible régulation). **Recommandations** : Débuter Pays X-Y ; éviter Pays Z. |
| **5️⃣ Limites** | Pas données commerciales actuelles. Clustering non labélisé. **Pistes** : Tarifs réels import/export ; validation terrain ; seasonalité. |

**🔗 Liens** : [GitHub P11](https://github.com/ferialzamoun-afk/P11) | [Notebooks](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/)

---

## 🏦 P12 — Détection Faux Billets (ML & FastAPI)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | BCE : Détecter faux billets € rapidement (accuracy >97%) pour tri automatisé sans manuel (coûts énormes fraude). |
| **2️⃣ Données** | Dataset bancaire (1400 billets : 900 vrais + 500 faux, 6 mesures géométriques). ✅ Sans manquantes, bien distribuées. Limites : euros seulement, pas données temporelles. |
| **3️⃣ Démarche** | **scikit-learn** → EDA → Split stratifié (70/30) → Pipeline (imputation + standardisation) → Éval 3 modèles → Export joblib → **FastAPI** (routes /predict, /predict/batch). |
| **4️⃣ Résultats** | RandomForest : accuracy 99%, precision 98.5%, recall 97%. <15 faux négatifs (risque maîtrisé). **Recommandations** : Deploy RandomForest ; monitorer drift ; retrain 6m. **Livrable** : API REST + modèle joblib. |
| **5️⃣ Limites** | Euros seulement (pas généralisation). Pas monitoring production (drift detection). **Pistes** : Augmenter devises ; logs production ; active learning. |

**🔗 Liens** : [GitHub P12](https://github.com/ferialzamoun-afk/P12) | [API / dépôt](https://github.com/ferialzamoun-afk/P12)

---

## 🎓 P13 — Portfolio Final (RNCP Validation)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | Validation compétences Data Analyst (RNCP-37837) via portfolio + soutenance. Enjeu : formaliser progression P1-P12 (cleaning → analytics → ML → deployment). |
| **2️⃣ Données** | 12 projets (P1-P12) + synthèse avec livrables hétérogènes (notebooks, APIs, dashboards, CSV/Power BI exports). ✅ Complets documentés. |
| **3️⃣ Démarche** | **GitHub Pages** (hub portfolio) + markdown docs (veille) + templates proof points → Sélection 6 phares → Structuration 5 piliers → Narration recruteur → Deployment. |
| **4️⃣ Résultats** | Portfolio 6 phares + 9 secondaires ; 5 blocs RNCP couverts (100%) ; veille techno 10 sections + veille métier 5 domaines. **Livrables** : README synthétique + 6 proof points + veille + soutenance. |
| **5️⃣ Limites** | Portfolio statique (snapshot). **Pistes** : Metrics temps réel (GitHub workflows) ; testimonials ; dashboard interactif. |

**🔗 Liens** : [Portfolio Hub](https://ferialzamoun-afk.github.io/MON-PORTFOLIO-DATA/) | [GitHub](https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA)

---

## 🏪 P14 — Stage Intermarché (Retail Analytics)

| Pilier | Résumé |
|--------|--------|
| **1️⃣ Besoin** | Intermarché : piloter assortiment, disponibilité et performance opérationnelle. Enjeu : single source of truth transactionnel → tableaux décisionnels. |
| **2️⃣ Données** | Données Intermarché (transactionnel, assortiment, stocks, DLP = stock disponible jour J). ✅ Grain granulaire. ⚠️ Nettoyage requis ; confidential-client. |
| **3️⃣ Démarche** | **Python/Pandas + Power Query (Langage M) + Power BI** → ETL → Star schema (Fact/Dim) → 2 restitutions (Power BI statique + Streamlit interactif). |
| **4️⃣ Résultats** | KPIs : Coverage assortiment, disponibilité produits (% stock jour J), perf opérationnelle (ventes/m² magasin). **Impact** : Reporting manuel 5h → 15min auto. **Livrables** : Power BI multi-page + Streamlit app + notebooks. |
| **5️⃣ Limites** | Données stage (temporaire) ; analyses rétrospectives. **Pistes** : ETL production temps réel (Airflow/dbt) ; KPIs RH ; demand planning ML. |

**🔗 Liens** : [GitHub P14](https://github.com/ferialzamoun-afk/P14)

---

## 📌 À Imprimer / Partager

- 📄 **Une page par projet** : synthèse exécutive complète
- 🎯 **Angle recruteur** : contexte métier → données → démarche → résultats → limites & pistes  
- ⏱️ **Temps lecture** : 3-5 minutes par projet
- 🔗 **Tous liens cliquables** vers GitHub, notebooks, dashboards

---

## 🔄 Comment Utiliser Ce Fichier

1. **Avant entretien** : Parcourir synthèses pour rappel rapide de chaque projet
2. **Pour recruteur** : Imprimer + remises lors de présentation
3. **Pour portfolio** : Ajouter ce fichier aux assets en PDF
4. **Pour documentation** : Référencer template PROOF_POINTS_TEMPLATE.md pour structure complète

