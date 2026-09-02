# 🧭 P15 — Observatoire Territorial des Métiers Data & IA

> **Type** : Projet Personnel / Recherche appliquée · Marché de l'emploi & Compétences · DuckDB · Power BI · Streamlit
> **Contexte** : Observatoire indépendant et interactif pour cartographier les métiers Data & IA, confronter les offres réelles aux besoins BMO et auditer le mapping des certifications RNCP
> **Période** : 2026
> **Application en ligne** : 🌐 **[Observatoire Streamlit P15](https://8i4kbcfrhfrty7p8ivapeu.streamlit.app/)**
> **Dépôt GitHub** : 💻 **[GitHub - P15](https://github.com/ferialzamoun-afk/P15)**

---

## 🎯 1. Contexte et problématique métier

Le marché de l'emploi dans les métiers de la **Data et de l'Intelligence Artificielle** (Data Analyst, Data Engineer, Data Scientist, Business Analyst) souffre d'un manque de visibilité fine :
- Les nomenclatures officielles (codes ROME France Travail) génèrent des **incohérences de classification** (ex. offres intitulées *« Ingénieur Data Analyst »* classées sous *Yield Manager - G1302* ou *Performance sportive - G1211*).
- Les **intentions d'embauche déclarées** (Enquête BMO 2026) diffèrent fortement des flux d'annonces en ligne, révélant un **marché caché** ou des circuits de recrutement directs.
- Le rapprochement avec les **titres RNCP** de France Compétences présente des écarts de couverture selon les spécialités.

**Objectifs du projet** :
1. **Collecter et unifier** les offres d'emploi (API France Travail), les intentions d'embauche (BMO 2026) et les référentiels de compétences/certifications (France Compétences).
2. **Construire un socle analytique OLAP** haute performance avec **DuckDB** et le format **Parquet**.
3. **Fournir une double restitution** : décisionnelle sur **Power BI Desktop** et interactive publique via une **application Web Streamlit**.

---

## 🧭 2. Démarche et architecture technique

```text
Sources Open Data / APIs
├── France Travail (API Offres & Flux Sortants)
├── Enquête BMO 2026 (Besoins en Main-d'Œuvre)
└── France Compétences (Fiches & Référentiels RNCP)
                │
                ▼ (Pipeline Python modulaire)
     [ data/processed/ ]
                │
                ▼
      p15_analytics.duckdb (Moteur OLAP)
                │
                ├── Vues relationnelles & Modélisation Étoile + Bridges (N:N)
                │
                ▼ (Exports Marts Parquet)
      data/processed/marts/ (43 tables)
                │
        ┌───────┴───────────────────┐
        ▼                           ▼
📊 Power BI Desktop          🌐 Application Streamlit
 (Tableaux de bord locaux)    (Restitution Publique Cloud)
```

---

## 🌟 3. Preuve de compétences

### A. Veille Métier & Business Analysis
- **Cadrage décisionnel** : Rédaction d'un cahier des charges et d'un wireframe 5 pages répondant aux questions stratégiques du recrutement Data.
- **Audit des faux positifs** : Identification et traçabilité des anomalies d'appariement ROME (intitulé vs code affecté).
- **Confrontation Offre / Besoin** : Construction d'une matrice quadrant *Tension déclarée vs Visibilité marché*.

### B. Veille Technologique & Data Engineering
- **Architecture OLAP DuckDB** : Stockage relationnel compact, exécution vectorisée et requêtage SQL in-process.
- **Standardisation Parquet** : Remplacement des flux CSV par des marts Parquet typés, divisant par 10 les temps de chargement et supprimant les verrous de fichiers ODBC.
- **Modélisation relationnelle avancée** : Schéma en étoile avec tables de faits (`fact_offres`, `fact_bmo`, `fact_sortants`) et tables de ponts N:N (`bridge_offres_competences`, `bridge_offres_certifications_all`).

### C. Traçabilité des preuves & Déploiement
- **Application Web publique** : Déploiement sur Streamlit Cloud avec gestion dynamique des chemins de données et mise en cache (`@st.cache_data`).
- **Journal de bord & documentation** : Répertoire complet de spécifications, métadonnées et règles de gestion dans `docs/`.

---

## 📊 4. Les 5 Pages du Dashboard Analytique

<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.08); font-size: 0.95em;">
	<thead>
		<tr style="background-color: #155799; color: white;">
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Page</strong></th>
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Question Métier</strong></th>
			<th style="padding: 12px 12px; text-align: left; border: 1px solid #ddd;"><strong>Insights Clés & Dataviz</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr style="background-color: #f4f7fb;">
			<td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>1. Synthèse décisionnelle</strong></td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Où se situe le volume d'offres et quels signaux de tension émergent ?</td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Concentration IDF/ARA (>60 %), comparaison Offres vs BMO par région, matrice quadrant tension.</td>
		</tr>
		<tr>
			<td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>2. Marché des offres</strong></td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Quels contrats et employeurs dominent et quelles anomalies sont détectées ?</td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Treemap hiérarchique avec poste dominant en infobulle, détection des faux positifs ROME (G1302, M1423).</td>
		</tr>
		<tr style="background-color: #f4f7fb;">
			<td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>3. Compétences & RNCP</strong></td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Quelles compétences techniques sont requises et quel est le taux de couverture RNCP ?</td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Top 15 Compétences (SQL, Python, Power BI), Heatmap Métiers x Skills, table d'audit des correspondances RNCP.</td>
		</tr>
		<tr>
			<td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>4. Formation & Profils</strong></td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Quel retour à l'emploi pour les sortants et quelle typologie sociodémographique ?</td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Taux d'accès à l'emploi (64.5 %), projection factorielle ACP (3 clusters Âge/Genre), croisement sortants/compétences.</td>
		</tr>
		<tr style="background-color: #f4f7fb;">
			<td style="padding: 10px 12px; border: 1px solid #ddd;"><strong>5. Suivi historique</strong></td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Comment évoluent les offres entre les collectes et quelle est la durée de vacance ?</td>
			<td style="padding: 10px 12px; border: 1px solid #ddd;">Durée médiane de publication (34 jours), identification de la tension accrue sur les profils seniors (48 jours).</td>
		</tr>
	</tbody>
</table>

---

## 🛠️ 5. Stack technologique

- **Stockage & Traitement OLAP** : DuckDB, PyArrow, Parquet
- **Langages & Traitement** : Python (Pandas, Numpy)
- **Restitution Décisionnelle** : Power BI Desktop (modèle en étoile + DAX)
- **Restitution Web Interactive** : Streamlit Community Cloud, Plotly Express
- **Contrôle Qualité & Versioning** : Git, GitHub Pages, pytest

---

## 🔗 Liens & Accès

- 🌐 **[Accéder à l'application Streamlit en direct](https://8i4kbcfrhfrty7p8ivapeu.streamlit.app/)**
- 💻 **[Consulter le code source sur GitHub (P15)](https://github.com/ferialzamoun-afk/P15)**
- 📄 **[Retour au Portfolio principal](../../README.md)**
