# Matrice portfolio - P13 Partie 2

## Mission

**Realiser un portfolio data publie sur GitHub** afin de valoriser les projets du parcours, les competences de Data Analyst et la demarche professionnelle.

Cette matrice permet de suivre la preparation du portfolio, la qualite des preuves et l'avancement des 14 projets.

Mise a jour : 2026-08-03.

## Mission 2 - Narration des preuves

Le portfolio doit raconter chaque preuve selon le fil : **contexte -> besoin metier -> demarche -> resultats -> impact**.

Les resultats de veille sont integres dans la narration pour justifier les choix d'outils, les methodes d'analyse, les criteres de selection et les limites.

## Legende des statuts

- [ ] A faire
- [~] En cours
- [x] Realise

## 1. Indicateurs portfolio et preuves attendues

| Indicateur | Ma preuve | Metriques possibles | Statut |
|---|---|---|---|
| Le portfolio presente clairement le profil Data Analyst. | README principal : presentation, objectif professionnel, competences, outils, lien de contact. | Sections presentes ; temps de lecture ; clarté du pitch. | [ ] |
| Les projets sont organises et consultables. | Arborescence propre : un dossier ou une section par projet, liens fonctionnels, noms explicites. | Nombre de projets documentes ; nombre de liens verifies. | [ ] |
| Les projets demontrent les competences du titre professionnel. | Chaque projet relie a des competences : collecte, nettoyage, analyse, visualisation, restitution, SQL, Python, BI, gestion de projet. | Nombre de competences couvertes ; nombre de projets par competence. | [ ] |
| Les livrables sont comprehensibles par un recruteur ou client non technique. | README projet avec contexte, objectif, demarche, resultats, captures et recommandations. | Nombre de README complets ; presence de captures ; lisibilite. | [ ] |
| Les resultats et impacts sont valorises. | Section resultats : KPI, insights, decision metier, limites, prochaines etapes. | Nombre de resultats quantifies ; nombre de recommandations. | [ ] |
| Le portfolio respecte les bonnes pratiques GitHub. | README, structure claire, liens relatifs, fichiers inutiles retires, documentation d'execution. | Liens morts ; taille repo ; presence .gitignore si utile. | [ ] |
| L'accessibilite et la lisibilite sont prises en compte. | Titres hierarchises, textes alternatifs pour images, contrastes/captures lisibles, langage clair. | Nombre d'images avec description ; niveau de structure Markdown. | [ ] |
| La demarche d'amelioration continue est visible. | Issues GitHub, backlog, changelog, TODO, matrice de suivi, versionnement. | Nombre d'issues/taches ; nombre de commits utiles ; jalons. | [ ] |
| La difference correction / evolution est explicite. | TNR GitHub Pages + suivi des corrections de liens/rendus/chiffres vs evolutions de contenu. | Nombre de corrections bloquantes ; nombre d'evolutions planifiees. | [~] |

## 2. Matrice de suivi des 14 projets

| Projet | Type de preuve attendue | Competences a valoriser | Metriques possibles | Statut |
|---|---|---|---|---|
| Projet 1 - Presentation | [README P1](../../P1_presentation/README.md) + preuve de positionnement | Communication pro, narration, positionnement | Clarte du pitch, lisibilite, coherence du profil | [~] |
| Projet 2 - Analyse e-commerce | [README P2](../../P2_analyse_ecommerce/README.md) + livrables d'analyse | Collecte, nettoyage, KPI, visualisation | Volume traite, KPI commerciaux, recommandations | [~] |
| Projet 3 - Requetes SQL | [README P3](../../P3_requetes_sql/README.md) + scripts/requetes | SQL, modelisation, extraction | Nombre de requetes, complexite SQL, qualite des sorties | [~] |
| Projet 4 - Etude sante publique | [README P4](../../P4_etude_sante_publique/README.md) + restitution | Analyse exploratoire, dataviz, insights | Nombre d'indicateurs, qualite des visualisations, recommandations | [~] |
| Projet 5 - Base immobiliere SQL | [README P5](../../P5_base_immobiliere_sql/README.md) + requetes | SQL avance, qualite donnees, restitution | KPI immobiliers, requetes metier, robustesse des controles | [~] |
| **Projet 6 - Bottleneck ⭐ preuve technique phare** | [README P6](../../P6_Optimisation_Bottleneck/README.md) + notebook P6 ameliore + dashboard + documentation Partie 1 | Python, Pandas, nettoyage, rapprochement, EDA, detection anomalies, BC05, dashboard, IA critique | CA 143.7k EUR, 825 produits, 714 web match, 18 controles qualite, 36 alertes BC05, matrice stricte 1 critique / 172 a surveiller / 652 normaux, 65 cellules | [x] |
| Projet 7 - Dashboard Power BI | [README P7](../../P7_dashboard_powerbi/README.md) + rapport visuel | BI, storytelling, decisionnel | Nombre de pages KPI, lisibilite dashboard, recommandations | [~] |
| Projet 8 - Egalite femmes hommes | [README P8](../../P8_egalite_femmes_hommes/README.md) + analyse RH | ETL, data quality, indicateurs RH | KPI egalite, ecarts detectes, qualite du reporting | [x] |
| Projet 9 - Librairie | [README P9](../../P9_librairie/README.md) + app/livrables | Pipeline data, UX analytique, dataviz | Interactions app, KPI suivis, qualite des insights | [x] |
| Projet 10 - Eau potable | [README P10](../../P10_eau_potable/README.md) + analyses thematiques | Analyse sectorielle, qualite donnees, dataviz | KPI eau potable, couverture geographique, recommandations | [x] |
| Projet 11 - Etude marche | [README P11](../../P11_etude_marche/README.md) + synthese business | Etude de marche, segmentation, priorisation | Critere de ciblage, scoring, decisions proposees | [x] |
| Projet 12 - Faux billets | [README P12](../../P12_faux_billets/README.md) + notebook + docs | Classification, modelisation, evaluation | Precision modele, robustesse validation, tracabilite decisions | [x] |
| **Projet 13 - Portfolio + IA ⭐ preuve de pilotage** | [README P13](../README.md) + Mission 2 + matrice RNCP + GitHub Pages | Pilotage projet, IA governance, documentation, veille technologique, valorisation portfolio | GitHub Project, dossier projet unique, Mission 2, mapping RNCP, TNR GitHub Pages, correction vs evolution | [x] |
| Projet 14 - Stage | [README P14](../../P14_stage/README.md) + livrables de mission | Cadre pro, analyse metier, restitution | Livrables produits, adoption metier, impact operationnel | [x] |

## 3. Niveau de profondeur par projet

| Niveau | Projets concernes | Objectif | Preuve minimum |
|---|---|---|---|
| Niveau 1 | Projet 6 - Bottleneck | Projet phare relie a la Partie 1 | README complet, notebook ameliore, preuves IA, avant/apres, captures, matrice indicateurs. |
| Niveau 2 | 3 a 4 projets forts | Montrer la polyvalence Data Analyst | README detaille, captures, resultats, competences, outils. |
| Niveau 3 | Autres projets | Montrer le parcours complet sans surcharge | Resume court, outils, competences, lien vers livrable. |

## 4. Gabarit de README pour chaque projet

| Section | Contenu attendu | Statut |
|---|---|---|
| Contexte | Situation metier, donnees, utilisateur cible. | [ ] |
| Objectif | Question a resoudre ou decision a aider. | [ ] |
| Donnees | Source, format, volume, qualite, limites. | [ ] |
| Methodologie | Nettoyage, analyse, visualisation, modelisation si applicable. | [ ] |
| Outils | Python, SQL, Power BI, Tableau, Excel, GitHub, etc. | [ ] |
| Resultats | KPI, insights, graphiques, recommandations. | [ ] |
| Competences | Competences du titre professionnel demontrees. | [ ] |
| Limites | Biais, donnees manquantes, prudence d'interpretation. | [ ] |
| Captures/liens | Images, notebook, dashboard, rapport, depot GitHub. | [ ] |

## 5. Matrice competences x projets

| Competence | Projets qui la prouvent | Preuve a ajouter | Statut |
|---|---|---|---|
| Collecter et integrer des donnees | **P6 Bottleneck** | Sources ERP/Web/Liaison, rapprochement 825 produits. | [x] |
| Nettoyer et preparer les donnees | **P6 Bottleneck** | 18 controles qualite, stocks corriges, anomalies documentees. | [x] |
| Analyser les donnees | **P6 Bottleneck** | EDA, Pareto rang 435, BC05, matrice stricte. | [x] |
| Visualiser et restituer | **P6 Dashboard + P13 GitHub Pages** | Dashboard Streamlit, 25 visuels, portfolio public. | [x] |
| Utiliser SQL | **P3 Requetes SQL + P5 Base immobiliere SQL** | Requetes metier, schema, resultats. | [x] |
| Utiliser Python | **P6 Bottleneck** | Notebook 65 cellules, scripts, pandas, sklearn, SHAP. | [x] |
| Communiquer des recommandations | **P13 + P6** | Synthese, conclusions, dashboard decisionnel, soutenance. | [x] |
| Documenter et versionner | **P13 + portfolio** | README, GitHub Pages, dossier unique, TNR, commits. | [x] |
| Piloter un projet data | **P13 Partie 1** | GitHub Project, planning, backlog, risques, matrice indicateurs. | [x] |
| Utiliser l'IA de maniere critique | **P13 + P6** | Prompts, variantes, decisions humaines, limites, arbitrage `critical_score` / `surveillance_score`. | [x] |

## 5.1 Statut des blocs RNCP 37837

| Bloc | Intitule | Statut |
|---|---|---|
| BC01 | Structurer et gerer une base de donnees | [x] Termine |
| BC02 | Collecter, traiter et analyser les donnees | [x] Termine |
| BC03 | Visualiser et restituer les resultats | [x] Termine |
| BC04 | Piloter un projet data et documenter | [x] Termine |
| BC05 | Realiser des analyses statistiques avancees | [x] Termine |

## 6. Actions immediates

| Priorite | Action | Livrable cible | Statut |
|---|---|---|---|
| 1 | Lister les noms exacts des 14 projets du portfolio. | Matrice projets completee | [x] |
| 2 | Identifier les 3 a 4 projets les plus forts apres Bottleneck. | Niveau de profondeur defini | [ ] |
| 3 | Creer ou harmoniser le README principal du portfolio. | README portfolio | [ ] |
| 4 | Ajouter une capture ou preuve visuelle pour chaque projet prioritaire. | Assets/captures | [ ] |
| 5 | Verifier les liens GitHub et chemins relatifs. | Portfolio publiable | [ ] |