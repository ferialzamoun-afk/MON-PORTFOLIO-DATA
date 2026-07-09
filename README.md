# 📊 **Portfolio Data Analyst – Ferial Zamoun**
**Transformation de données dispersées en **décisions fiables**, indicateurs actionnables et restitutions partageables.**

> **🎯 Fil Rouge** :
> *Cadrer un besoin métier → Fiabiliser les données → Produire des KPI → Visualiser pour la décision → Documenter les preuves.*

> **🔹 Objectif** : **Alternance ou poste en Data / IA** (25 ans d’expérience IT + reconversion Data Science).

---
---
## **👤 À Propos**
**👩‍💻 Qui suis-je ?**
- **Data Analyst en reconversion vers l’IA** (Certification **RNCP 37837** en cours – GRETA OpenClassrooms).
- **25 ans d’expérience en IT** (ESN, Banque, Assurance) : Développement, MOA, Pilotage.
- **Expertise** : **Analyse exploratoire**, **Machine Learning**, **Visualisation**, **Pilotage de projets data**.

**🎯 Ma Mission** :
*Rendre les données **compréhensibles, exploitables et actionnables** pour les décideurs, avec une approche **pédagogique** et **orientée business*.*

**📩 Contact** :
- **Email** : [ton.email@exemple.com](mailto:ton.email@exemple.com)
- **LinkedIn** : [lien-vers-ton-linkedin](https://linkedin.com/in/tonprofil)
- **GitHub** : [ferialzamoun-afk](https://github.com/ferialzamoun-afk)

---
---
## **🌟 Projets Phares**
*(Sélection de projets documentés, consultables et orientés recruteur)*

### **🔹 1. Fiabilisation de Données E-Commerce – Bottleneck**
**📌 Projet de référence** pour démontrer le **nettoyage, rapprochement de sources et qualité des données**.
- **Contexte** : Boutique de vins en ligne avec **3 sources incohérentes** (ERP, Web, Liaison).
- **Objectifs** :
  - Réconcilier les données pour une **vue unifiée**.
  - Identifier les **anomalies** (prix invalides, marges négatives, ruptures de stock).
  - Fournir des **KPI au CODIR** pour la décision.

**📊 Résultats** :
- **CA mensuel** : **143 680 €** (octobre 2026).
- **Catalogue** : **689 produits** (80% du CA porté par 435 produits – loi de Pareto).
- **Anomalies détectées** : **10** (3 prix, 7 marges, 92 ruptures de stock).
- **Optimisation** : **Notebook refactoré** (-68% de cellules, -76% de temps d’exécution).

**🔗 Liens** :
- [📄 Fiche Projet Bottleneck](https://github.com/ferialzamoun-afk/P6_ameliore_IA/blob/main/docs/06_synthese_finale_P13_partie_1.md)
- [🌐 Dashboard Public](https://p6-dashboard-wdcn5o8grt39nqtim6mgym.streamlit.app/)
- [🔗 Dépôt Source Initial](https://github.com/ferialzamoun-afk/OC_P6_Optimisation_des_donnees_dune_boutique_en_Python)
- [🔗 Version Portfolio (P13 Partie 1)](https://github.com/ferialzamoun-afk/P6_ameliore_IA)

**🎯 Compétences Demonstrées** :
- Nettoyage et rapprochement de données (**BC01, BC02**).
- Contrôles qualité (**18 points validés**, 7 Data Contracts).
- KPI business (CA, Pareto, marges).
- **Reproductibilité** et **traçabilité IA** (26 prompts documentés).

---

### **🔹 2. Étude Marché – Priorisation des Pays pour l’Export (P11)**
**📌 Projet d’analyse multivariée et clustering** pour identifier des marchés porteurs à l’export.
- **Contexte** : Mission confiée par **La Poule Qui Chante** (entreprise de poulets biologiques) pour **optimiser sa stratégie d’export**.
- **Objectifs** :
  - Identifier des **groupements de pays** à cibler via une **analyse PESTEL+** (Politique, Économique, Social, Technologique, Environnemental, Sanitaire, Réglementaire).
  - Proposer une **priorisation des marchés** (Top 5 pays à approfondir).
  - **Automatiser** la détection des opportunités via des **scores composites**.

**📊 Résultats** :
- **Base d’analyse** : **139 pays** × **16 variables** → `base_acp_finale_2017.csv`.
- **ACP (Analyse en Composantes Principales)** : **11 variables actives** → **3 composantes principales** (89.90% de variance conservée).
- **Clustering** : **KMeans (k=2)** avec un **Silhouette Score de ~0.60** (qualité bonne).
- **Recommandations** :
  - **Top 5 pays** : Suisse 🇨🇭, Dominique 🇩🇲, Émirats Arabes Unis 🇦🇪, Belgique 🇧🇪, Autriche 🇦🇹.
  - **Shortlist 3** : Suisse, Dominique, Émirats Arabes Unis.
  - **Pays prioritaire** : **Suisse** (score composite optimal, accord CAH/KMeans).

**🔗 Liens** :
- [📄 Fiche Projet P11](https://github.com/ferialzamoun-afk/P11)
- [📓 Notebook 1 : Préparation & EDA (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Ferial_1_preparation_nettoyage_EDA_analyse_exploratoire_112025.ipynb)
- [📓 Notebook 2 : Clustering & Recommandations (nbviewer)](https://nbviewer.org/github/ferialzamoun-afk/P11/blob/main/notebooks/ZAMOUN_Férial_2_clustering_visualisations_112025.ipynb)
- [📊 Dashboard Power BI (Template)](https://github.com/ferialzamoun-afk/P11/raw/main/data/processed/pbi_star/Dashboard_eau_v6.pbit) *(à ouvrir avec Power BI Desktop)*

**🎯 Compétences Demonstrées** :
- **Structurer une base de données** (**BC01**) : Création de `base_acp_finale_2017.csv` et tables étoile Power BI.
- **Identifier, collecter et analyser les données** (**BC02**) : Nettoyage, EDA, **Feature Engineering** (distance de Levenshtein pour `faolex_text_diversity_score`).
- **Visualiser des données** (**BC03**) : ACP, clustering (CAH/KMeans), profils de clusters.
- **Piloter un projet data** (**BC04**) : Pipeline en 3 notebooks, documentation complète (8 docs), CI/CD.
- **Spécialisation Statistiques** (**BC05**) : Analyses multivariées, réduction de dimension, tests statistiques (Silhouette Score).

---
### **🔹 3. Détection de Faux Billets**
**📌 Projet de Machine Learning** pour un cas de détection de risque.
- **Contexte** : Mission pour l’**ONFM** (Organisation Nationale de Lutte contre le Faux-Monnayage).
- **Objectifs** :
  - Développer un **modèle de classification binaire** (vrai/faux billet).
  - Atteindre un **recall de 100%** sur les faux billets (aucun faux négatif).

**📊 Résultats** :
- **Accuracy** : **88%**.
- **Recall (Faux Billets)** : **100%** *(objectif atteint)*.
- **F1-Score** : **0.91**.
- **Modèle exporté** : API FastAPI pour la prédiction.

**🔗 Liens** :
- [📄 Fiche Projet Détection de Faux Billets](https://github.com/ferialzamoun-afk/P12)
- [🔗 Dépôt GitHub](https://github.com/ferialzamoun-afk/P12)

**🎯 Compétences Demonstrées** :
- **Modélisation ML** (**BC05** : classification, évaluation).
- **API FastAPI** pour le déploiement.
- **Reproductibilité** (notebooks, documentation).

---
---
## **🎯 Compétences Data Analyst Demonstrées**
*(Alignées sur les **blocs RNCP 37837** et les attentes métiers)*
   **Compétence** | **Preuve** | **Indicateur / Livrable** | **Bloc RNCP** |
 |---------------|-----------|--------------------------|---------------|
 | **Cadrer un besoin métier** | Projet Bottleneck (sources ERP/Web/Liaison) | 3 sources consolidées, **825 produits analysés** | **BC04** |
 | **Contrôler la qualité des données** | Scripts Python + Notebook P13 Partie 1 | **18 contrôles qualité**, 11 OK, 1 correction stock finalisée | **BC02** |
 | **Produire des KPI exploitables** | Dashboard E-Commerce (Bottleneck) | **143 680 € de CA calculé**, 92 ruptures de stock évitées | **BC05** |
 | **Visualiser pour la décision** | Dashboard Power BI (SANITORAL) | Vues par persona, **seuil d’alerte > 15%** | **BC03** |
 | **Documenter et partager** | README, captures, liens publics, traçabilité IA | **Documentation consultable comme un espace partageable** | **BC04** |
 | **Modéliser et évaluer** | Projet Détection de Faux Billets | **Recall de 100%**, F1-score de 0.91 | **BC05** |
 | **Piloter un projet data** | Portfolio complet (P6, P8, P9, P10, P11, P12, P13) | **7 projets documentés**, CI/CD, veille technologique | **BC04** |

---
---
## **💻 Application Portfolio**
**🌐 [Application Streamlit du Portfolio](https://ton-lien-streamlit-app)** *(à remplacer par ton URL)*
- **Données descriptives internes** : [streamlit_app/projets_data.md](https://github.com/ferialzamoun-afk/Portfolio-Data/blob/main/streamlit_app/projets_data.md)
- **Dossiers projets** : [projets/](https://github.com/ferialzamoun-afk/Portfolio-Data/tree/main/projets)

**🎨 Fonctionnalités** :
- **Navigation intuitive** : Accès direct à chaque projet (P6, P8, P9, etc.).
- **Visualisations interactives** : Graphiques Plotly, matrices de confusion, etc.
- **Documentation intégrée** : Lien vers les README, notebooks et preuves.

---
---
## **🚀 Comment Naviguer dans ce Portfolio ?**
1. **Pour les recruteurs** :
   - Commence par la section **"À Propos"** pour comprendre mon parcours.
   - Consulte les **3 projets phares** pour voir mes compétences en action.
   - Explore l’**application Streamlit** pour une expérience interactive.

2. **Pour les évaluateurs France Compétences** :
   - Vérifie le **mapping des blocs RNCP 37837** dans le tableau des compétences.
   - Consulte les **README détaillés** de chaque projet pour les preuves tangibles.

3. **Pour les collaborateurs** :
   - Les **dépôts GitHub** sont publics (sauf données sensibles).
   - Les **notebooks** sont accessibles via [nbviewer](https://nbviewer.org/) (liens fournis).

---
---
## **📌 Fil Rouge Méthodologique**
*(Appliqué à tous mes projets)*

1. **🎯 Cadrer un besoin métier** :
   - Comprendre les **enjeux business** (ex: détection de fraude pour l’ONFM).
   - Traduire en **objectifs techniques** (ex: recall de 100% pour les faux billets).

2. **🧹 Fiabiliser les données** :
   - **Nettoyage** (valeurs manquantes, doublons).
   - **Rapprochement** de sources multiples (ERP + Web + Liaison).
   - **Contrôles qualité** (18 points validés dans P6 amélioré).

3. **📊 Produire des KPI exploitables** :
   - **CA, marges, rotation des stocks** (Bottleneck).
   - **Taux de pénétration, écarts genre/âge** (P8 – OpenClassrooms vs INSEE).

4. **📈 Visualiser pour la décision** :
   - **Dashboards Power BI/Streamlit** (SANITORAL, Portfolio).
   - **Graphiques interactifs** (Plotly, Matplotlib).

5. **📂 Documenter et partager** :
   - **README détaillés** pour chaque projet.
   - **Traçabilité complète** (IA, contrôles qualité, décisions).
   - **Preuves accessibles** (GitHub, nbviewer, liens publics).

---
---
## **📅 Roadmap et Prochaines Étapes**
 | **Projet** | **Statut** | **Prochaines Améliorations** |
 |-----------|------------|-----------------------------|
 | **P6 Amélioré (Bottleneck)** | ✅ Finalisé | Déploiement du dashboard Streamlit en production |
 | **P8 (OpenClassrooms vs INSEE)** | ✅ Finalisé | Intégration Power BI + API REST |
 | **P9 (Lapage)** | ✅ Finalisé | Optimisation UX du dashboard |
 | **P10 (Dashboard Eau)** | ✅ Finalisé | Ajout de données temps réel |
 | **P11 (Étude Marché)** | ✅ Finalisé | Benchmark des outils de clustering |
 | **P12 (Détection Faux Billets)** | ✅ Finalisé | Test de modèles Deep Learning |
 | **P13 (Portfolio)** | ✅ Finalisé | Ajout de projets supplémentaires |

---
---
## **💡 Pourquoi ce Portfolio ?**
- **Pour les recruteurs** :
  - **Démonstration concrète** de mes compétences en **Data Analysis, ML et Visualisation**.
  - **Preuves tangibles** (notebooks, dashboards, KPI).
  - **Approche métier** : Chaque projet répond à un **besoin business réel**.

- **Pour France Compétences** :
  - **Alignement sur les blocs RNCP 37837** (BC01 à BC05).
  - **Traçabilité complète** : De la collecte des données à la restitution.
  - **Documentation exhaustive** : README, notebooks, captures, liens.

- **Pour moi** :
  - **Vitrine de mon savoir-faire** en Data Science.
  - **Outil d’amélioration continue** (feedback, veille, nouvelles technologies).

---
---
## **📌 Liens Utiles**
 | **Type** | **Lien** | **Description** |
 |----------|----------|-----------------|
 | **GitHub** | [ferialzamoun-afk](https://github.com/ferialzamoun-afk) | Tous mes dépôts (P6, P8, P9, etc.) |
 | **LinkedIn** | [lien-vers-ton-linkedin](https://linkedin.com/in/tonprofil) | Profil professionnel |
 | **Portfolio Streamlit** | [ton-lien-streamlit](https://ton-lien-streamlit-app) | Application interactive |
 | **CV PDF** | [lien-vers-ton-cv.pdf](#) | Version téléchargeable |

---
---
## **🎯 Conclusion**
Ce portfolio est **conçu pour démontrer ma capacité à** :
✅ **Transformer des données brutes en insights actionnables**.
✅ **Piloter des projets data de A à Z** (de la collecte à la restitution).
✅ **Maitriser les outils modernes** (Python, dbt, Snowflake, Streamlit, Power BI).
✅ **Communiquer clairement** avec des **décideurs non-techniques**.

**🚀 Prêt pour une collaboration ?**
- **Alternance** : Je cherche un contrat en **Data Analyst / Data Scientist**.
- **Poste CDI** : Ouvert aux opportunités en **Data, BI ou IA**.
- **Freelance** : Disponible pour des missions ponctuelles.

---
**💬 Contactez-moi** pour discuter de vos besoins en **analyse de données, machine learning ou pilotage de projets data** !