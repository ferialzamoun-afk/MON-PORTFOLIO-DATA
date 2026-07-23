# 📚 **P9 : Analyse des Ventes – Librairie Lapage**
**Projet d'analyse de données et de visualisation pour suivre la performance commerciale, comprendre les comportements clients et fournir des livrables exploitables par le CODIR.**

**📅 Date** : 04/2026
**🏷️ Type** : Analyse Statistique / Dashboard Streamlit
**🔗 Liens** :
- [🔗 Dépôt GitHub - Analyses](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies)
- [🎯 Mission du jour (dépôt racine)](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies)
- [🌐 Dashboard Streamlit (Production)](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/)
- [📁 Code Source Dashboard](https://github.com/ferialzamoun-afk/P9-lapage-streamlit)
- [📓 Notebooks Jupyter](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/notebooks/analyses/)
- [📁 Documentation](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/docs/)
- [✅ Workflow Tests (pytest)](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml)

---

## **🎯 Contexte et Objectifs**
*(Bloc RNCP37837BC04 : Piloter un projet data)*

> **Contexte** :
> *"Projet réalisé pour la **librairie Lapage**, dans le cadre d’une **analyse data-driven** visant à optimiser la performance commerciale et la stratégie client. La librairie cherche à **comprendre ses données de vente** pour prendre des décisions éclairées en matière de **marketing, gestion des stocks et expérience client**."*

> **Objectifs Métier** :
> - **Suivre la performance commerciale** :
>   - Chiffre d’affaires (CA), panier moyen, concentration des ventes.
>   - Analyse des **tendances temporelles** (mensuelles, saisonnières).
> - **Comprendre les comportements clients** :
>   - Segmentation des clients (fréquence d’achat, catégories préférées).
>   - Identification des **segments clés** (ex: clients réguliers vs occasionnels).
> - **Fournir des livrables exploitables** :
>   - **Notebooks** d’analyse statistique (axes Marketing et BI).
>   - **Dashboard Streamlit** multi-pages pour le CODIR.
>   - **Exports KPI** (Excel) et **figures de reporting**.

> **Public Cible** :
> - **CODIR** (Comité de Direction) : Tableaux de bord et rapports synthétiques.
> - **Équipes Marketing/BI** : Notebooks et analyses détaillées.

---

## **📊 Structure du Projet**
```text
P9/
├── api/
├── dashboard/
├── data/
├── docs/
├── graphiques/
├── models/
├── multi-pages/
├── notebooks/
├── reports/
├── src/
├── Streamlit/
├── tests/
├── ACP.md
├── packages.yml
├── profiles.yml
├── PROJECT_BRIEF.md
├── README.md
└── requirements.txt
```

### **🔹 Données Sources (`data/raw/`)**

[Dépôt GitHub - Données](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/data/raw)

> **Note de publication** :
> Les donnees partagees dans le cadre du portfolio sont destinees a la demonstration pedagogique.
> Aucun nom, email, telephone ou identifiant client directement nominatif n'est expose dans cette documentation publique.

```
data/raw/
├── customers.csv                          # Clients (ID, genre, âge, etc.)
├── products.csv                           # Produits (ID, catégorie, prix, etc.)
└── Transactions.csv                       # Transactions (date, client, produit, montant)
```

### **🔹 Figures de Reporting (`reports/figures/`)**

[Dépôt GitHub - Figures](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/reports/figures)

```
reports/figures/
├── ca_mensuel.png                         # CA mensuel (tendance)
├── evolution_du_ca_mensuel.png            # Évolution du CA (série temporelle)
├── ca_par_categorie.png                   # CA par catégorie de produits
├── btob_btoc_pie.png                      # Répartition B2B/B2C
├── lorenz_ca.png                          # Courbe de Lorenz (concentration)
├── pareto_clients.png                     # Courbe de Pareto clients
├── segmentation_ca_boxplot.png            # Segmentation CA par client
├── fig3_repartition_categorie.png         # Répartition catégories
├── fig9_clients_actifs.png                # Clients actifs
├── fig10_volume_transactions_produits.png # Volume transactions
├── julie_42_scatter_age_ca.png            # Scatter: Âge vs CA
├── julie_43_scatter_freq.png              # Scatter: Fréquence d'achat
├── julie_44_scatter_panier.png            # Scatter: Panier moyen
├── julie_45_boxplot_categ.png             # Boxplot catégories
└── ... (31 fichiers PNG au total)
```
---
## **🔧 Compétences RNCP 37837 Demonstrées**

### **📌 Mapping des Blocs RNCP**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead>
      <tr style="background-color: #155799; color: white;">
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Bloc RNCP</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Compétence</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuves</strong></th>
      </tr>
   </thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC01</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Structurer et gérer la base de données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pipeline de données : transformation des données brutes vers des données exploitables.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/src/data_loader.py">src/data_loader.py</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Identifier et collecter les données</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Utilisation des données de vente Lapage : CA, panier, fréquence clients.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/data/raw">data/raw/</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Extraire et agréger</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Nettoyage et agrégation : calcul du CA, du panier moyen et de la concentration des ventes.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb">02_Analyses_Marketing.ipynb</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Explorer et pré-traiter</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Feature engineering pour la segmentation clients.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/01_Exploration_EDA.ipynb">01_Exploration_EDA.ipynb</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC02</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse univariée / multivariée</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse des tendances : CA mensuel et panier par segment client.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb">02_Analyses_Marketing.ipynb</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Solution de visualisation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard Streamlit avec visualisations interactives.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/">Dashboard en ligne</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC03</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Créer un tableau de bord</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard multi-pages pour le CODIR.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9-lapage-streamlit/blob/main/Streamlit/app.py">Streamlit/app.py</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Veille métier / technologique</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Benchmark des outils et méthodologie documentée.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/MON-PORTFOLIO-DATA/blob/main/projets/P9_librairie/assets/veille/benchmark_outils_p9.md">Benchmark</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Formaliser le cahier des charges</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Documentation complète : notebooks, dashboard et exports.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies">Dépôt GitHub</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Organiser un projet data</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pipeline CI et structure modulaire du projet.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml">ci.yml</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC04</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Gérer la documentation</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Livrables documentés : notebooks, scripts et dashboard.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies">Dépôt GitHub</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses multivariées</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Segmentation clients : fréquence, CA et catégories.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb">02_Analyses_Marketing.ipynb</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>BC05</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Tests statistiques</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Validation des KPI et du filtrage multi-critères.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/tests/test_app.py">tests/test_app.py</a></td></tr>
   </tbody>
</table>

---
## **📊 Méthodologie**
*(Blocs RNCP37837BC02, BC03, BC05)*

### **🔹 Pipeline de Données**
1. **Collecte et nettoyage** *(BC02)* :
   - Chargement des données de vente (CA, panier, clients).
   - Nettoyage : gestion des valeurs manquantes, doublons, incohérences.

2. **Analyse exploratoire** *(BC02, BC05)* :
   - **Performance commerciale** : CA mensuel, panier moyen, concentration des ventes.
   - **Comportements clients** : Segmentation (fréquence d’achat, catégories préférées).

3. **Visualisation et Reporting** *(BC03)* :
   - **Dashboard Streamlit** : Vues interactives pour le CODIR.
   - **Exports Excel** : KPI et rapports pour les équipes métiers.
   - **Figures** : Graphiques statiques (PNG) pour les présentations.

4. **Tests et Validation** *(BC04, BC05)* :
   - **Pipeline CI** : Tests automatisés ([pytest](https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml)) pour valider la cohérence des KPI.
   - **Validation manuelle** : Vérification des résultats avec les équipes Lapage.

---
## **📈 Résultats et Livrables**
*(Blocs RNCP37837BC03, BC04)*

### **🔹 Dashboard Streamlit**
**URL de production** : [https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/](https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/)
**Fonctionnalités** :
- **Page 1 : Performance Commerciale** :
  - CA mensuel/annuel (graphique en aires ou barres).
  - Panier moyen par segment client.
  - Concentration des ventes (top 20% produits/clients).
- **Page 2 : Comportements Clients** :
  - Segmentation des clients (fréquence d’achat, CA moyen).
  - Catégories de produits les plus achetées.
  - Analyse RFM (Récence, Fréquence, Monétaire).
- **Page 3 : Reporting KPI** :
  - Tableau de bord des **KPI clés** (CA, panier, taux de rétention).
  - Export des données en **Excel** (bouton de téléchargement).


*Exemple : Segmentation RFM des clients Lapage.*

### **🔹 Tests & Déploiement**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead>
      <tr style="background-color: #155799; color: white;">
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Composant</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Lien</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th>
      </tr>
   </thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Tests (pytest)</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml">ci.yml - Workflow</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Validation automatisée des KPI et cohérence des données.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>Dashboard Streamlit</strong></td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9-lapage-streamlit">Code Source</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Repository avec application Streamlit déployée.</td></tr>
   </tbody>
</table>

### **🔹 Notebooks d'Analyse**
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead>
      <tr style="background-color: #155799; color: white;">
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Notebook</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Objectif</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Lien</strong></th>
      </tr>
   </thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">analyse_ventes.ipynb</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyse des performances commerciales : CA et panier.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb">02_Analyses_Marketing.ipynb</a></td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">analyse_clients.ipynb</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Segmentation et comportements clients.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/01_Exploration_EDA.ipynb">01_Exploration_EDA.ipynb</a> + <a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/02_Analyses_Marketing.ipynb">02_Analyses_Marketing.ipynb</a></td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">tests_statistiques.ipynb</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Validation des KPI et tests statistiques.</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/notebooks/analyses/03_Analyses_Statistiques.ipynb">03_Analyses_Statistiques.ipynb</a></td></tr>
   </tbody>
</table>

📂 Preuves et Documentation
(Bloc RNCP37837BC04 : Piloter un projet data)
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead>
      <tr style="background-color: #155799; color: white;">
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Type</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Lien</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Description</strong></th>
      </tr>
   </thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Dépôt GitHub</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies">P9_analyses_ventes_librairies</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Code source, notebooks, dashboard et tests.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Données de travail</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/data/raw">data/raw/</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Jeux de donnees utilises pour l'analyse, publies sans information nominative directe.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Dashboard Streamlit</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://p9-lapage-app-9jzz7bhjbzdalqkrzaiz62.streamlit.app/">Production</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Application web opérationnelle.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Notebooks</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/notebooks/analyses/">analyses/</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Analyses statistiques Marketing/BI.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Figures & Graphiques</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/reports/figures">reports/figures/</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">31 PNG : CA, segmentation et analyses.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Fonctions Réutilisables</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/src/">src/</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Modules Python mutualisés.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Tests & CI</td><td style="padding: 10px 12px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/.github/workflows/ci.yml">Workflow (pytest)</a></td><td style="padding: 10px 12px; border: 1px solid #ddd;">Validation automatisée des KPI.</td></tr>
   </tbody>
</table>

---
## **🛠 Configuration et Exécution**
*(Bloc RNCP37837BC04 : Organiser un projet data)*

### **📌 Prérequis**
- Python 3.11+
- `pip`

### **📌 Installation**
```bash
# Depuis le dossier racine du projet (lapage_project)
pip install -r requirements.txt
```

### **📌 Lancement Local**
1. Notebooks

```bash
cd notebooks
jupyter notebook
```

Ouvre ensuite Jupyter dans ton navigateur, puis execute les notebooks dans l'ordre.

2. Dashboard Streamlit

```bash
# Depuis le dossier racine (lapage_project)
streamlit run Streamlit/app.py
```

URL locale attendue : `http://localhost:8501`

### **📌 Tests**
```bash
# Depuis le dossier racine (lapage_project)
python -m pytest tests/test_app.py -v --tb=short
```

Couverture des tests :
- Chargement des données.
- Cohérence des KPI de base (CA, panier, fréquence).
- Filtrage multi-critères du dashboard.

### **🔐 Politique de publication**
- Le portfolio decrit les traitements, KPI et visualisations sans exposer de secret, de cle d'acces ou de configuration privee.
- Les donnees clients sont presentees sous une forme compatible avec une diffusion pedagogique, sans information nominative directe dans la documentation publique.
- Les environnements de production et leurs parametres d'acces restent separes du contenu du depot public.

### **🔹 Points de Vigilance**
*(Bloc RNCP37837BC02 : Identifier, collecter et analyser les données)*
<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
   <thead>
      <tr style="background-color: #155799; color: white;">
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Problème</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Solution Appliquée</strong></th>
         <th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Impact</strong></th>
      </tr>
   </thead>
   <tbody>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Données manquantes</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Imputation par moyenne ou médiane.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Réduction des biais dans les analyses.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Doublons</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Suppression via <code>drop_duplicates()</code>.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Données propres pour les KPI.</td></tr>
      <tr style="background-color: #f4f7fb;"><td style="padding: 10px 12px; border: 1px solid #ddd;">Incohérences CA</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Vérification des totaux : CA = somme des ventes.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Fiabilité des indicateurs.</td></tr>
      <tr><td style="padding: 10px 12px; border: 1px solid #ddd;">Segments clients</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Validation via RFM : récence, fréquence, monétaire.</td><td style="padding: 10px 12px; border: 1px solid #ddd;">Pertinence de la segmentation.</td></tr>
   </tbody>
</table>

### **🔹 Audits Effectués**

✅ Cohérence des KPI : CA = somme(ventes), panier moyen = CA / nombre de transactions.
✅ Filtrage multi-critères : Tests pytest pour valider les filtres du dashboard.
✅ Validation des segments : Vérification que la segmentation RFM couvre 100% des clients.

### **🔄 Maintenance et Mises à Jour**

#### **📌 Recalcul Complet**

- Placer les nouvelles données dans `data/raw/`.
- Exécuter les notebooks dans l’ordre :

```bash
jupyter notebook notebooks/analyse_ventes.ipynb
jupyter notebook notebooks/analyse_clients.ipynb
```

Les sorties (KPI, figures) seront generees dans `reports/`.

#### **📌 Enrichissements Possibles**

- Ajout de données : intégrer des données externes (ex: tendances marché du livre).
- Nouveaux KPI : taux de rétention, panier moyen par catégorie.
- Amélioration UX : simplification du dashboard (version business).
- Automatisation : planification des mises à jour (ex: mensuelles).

### **📌 Mapping RNCP 37837**

Blocs couverts par ce projet :

- ✅ BC01 : Structurer et gérer la base de données (pipeline de données, tables nettoyées)
- ✅ BC02 : Identifier, collecter et analyser les données (nettoyage, EDA, segmentation)
- ✅ BC03 : Visualiser des données et interpréter des résultats (Dashboard Streamlit, exports KPI)
- ✅ BC04 : Piloter un projet data (documentation, CI, organisation, veille)
- ✅ BC05 : Spécialisation Statistiques (analyses multivariées, tests statistiques, RFM)







