# 🏪 P14 — Stage : Analyse de Données Retail (Intermarché)

> **Type** : Stage · Retail analytics · Python · Power BI · Streamlit
> **Contexte** : Mission de stage en entreprise — données retail / assortiment
> **Date** : 2025–2026

---

## 🎯 1. Contexte et besoin métier

Mission de stage dans un contexte retail (périmètre Intermarché), centré sur le pilotage de la **disponibilité produit**, la **performance assortiment** et la **gouvernance des indicateurs**.

**Problème** : les données opérationnelles sont dispersées entre plusieurs sources, sans socle analytique consolidé permettant un pilotage métier fiable et reproductible.

**Enjeux** :
- Structurer les données depuis les sources brutes jusqu'aux jeux exploitables
- Produire des analyses reproductibles via notebooks et scripts
- Alimenter des restitutions métier via Power BI et une application Streamlit
- Conserver une documentation projet claire pour la maintenance et la transmission

**Thématiques métier couvertes** :
- Disponibilité produit et alertes assortiment
- Performance opérationnelle par rayon / segment
- Gouvernance des indicateurs et traçabilité des décisions

---

## 🧭 2. Démarche analytique

### **📊 Structure du Projet**
```text
P14/
├── data/
├── docs/
├── intermarche_notebook/
├── powerbi/
├── streamlit_app/
├── .gitignore
├── bilan_reflexif_stage_P14.md
├── feuille_de_route_stage_P5.md
├── modele_mail_note_livraison.md
└── README.md
```

**Architecture du pipeline** :

`data/raw/ -> préparation -> data/processed/ -> analyse -> Power BI / Streamlit`

**Couches du pipeline** :
- data/raw/ : données sources non modifiées (jamais transformées)
- data/processed/ : données nettoyées et standardisées prêtes pour l'analyse
- data/Fichiers transformés/DLP/ : jeux transformés liés au périmètre DLP

**Conventions qualité** :
- Journaliser les contrôles (doublons, clés, granularité, valeurs manquantes)
- Expliciter les prérequis d'exécution dans chaque sous-module
- Documenter toute transformation majeure dans docs/
- Séparer clairement les données brutes, transformées et publiées

**Flux de travail** :
1. **Ingestion et préparation** : nouvelles sources dans `data/raw/`, exécution notebooks/scripts, sorties dans `data/processed/`
2. **Analyse** : notebooks intermarche_notebook/ et powerbi/notebooks/, hypothèses tracées dans docs/
3. **Restitution** : mise à jour artefacts Power BI, cohérence avec l'application Streamlit

---

## 📊 3. Résultats et livrables

| Livrable | Description |
|---------|-------------|
| Notebooks d'analyse | Exploration et analyse sur le périmètre Intermarché |
| Application Streamlit | Vue applicative pour la restitution métier opérationnelle |
| Rapports Power BI | Tableaux de bord décisionnels avec KPI pilotage |
| Documentation projet | docs/, conventions, procédures |
| Bilan réflexif de stage | Retour d'expérience et formalisation des apprentissages |
| Feuille de route | Cadrage et contexte de la mission (euille_de_route_stage_P5.md) |
| Modèle de livraison | Template de communication de livraison (modele_mail_note_livraison.md) |

---

## 🎓 4. Compétences RNCP 37837 mobilisées

| Bloc | Compétence | Ce qui a été fait | Preuve |
|------|-----------|------------------|--------|
| **BC02** | Identifier et collecter | Exploitation données retail brutes Intermarché | data/raw/ |
| **BC02** | Extraire et agréger | Pipeline de transformation raw → processed | Scripts de préparation |
| **BC02** | Vérifier la cohérence | Contrôles qualité : doublons, clés, granularité, NaN | Journaux de contrôle |
| **BC02** | Analyse univariée/multivariée | Analyse disponibilité, performance, KPI assortiment | Notebooks |
| **BC03** | Créer un tableau de bord | Rapports Power BI et application Streamlit | powerbi/ + streamlit_app/ |
| **BC03** | Reporting des tendances | KPI pilotage, alertes assortiment, suivi temporel | Rapports Power BI |
| **BC04** | Organiser un projet data | Architecture raw/processed, documentation, conventions | docs/ |
| **BC04** | Gérer la documentation | README, bilan réflexif, feuille de route, rapports | Tous les livrables docs |
| **BC04** | Adapter sa posture | Positionnement professionnel en contexte réel | Bilan réflexif de stage |

---

## 💡 5. Impact et apprentissages

**Ce que ça a apporté** : un socle analytique opérationnel permettant une meilleure priorisation des actions sur la disponibilité produit et la performance assortiment.

**Veille métier** : problématiques retail (disponibilité produit, performance assortiment, pilotage des alertes) → indicateurs priorisés, règles de gestion, critères d'arbitrage documentés.

**Veille technologique** : Python (pandas/notebooks), Streamlit, Power BI → structuration raw/processed, fiabilisation des transformations, documentation des hypothèses.

**Bilan de stage** : expérience en contexte professionnel réel — mise en pratique de l'ensemble du pipeline analytique de la collecte à la restitution décisionnelle. Voir ilan_reflexif_stage_P14.md.

---

## 🔗 Points d'entrée utiles

- streamlit_app/README.md : cadre applicatif Streamlit
- powerbi/README.md : cadre de la partie BI
- docs/README.md : socle documentaire transverse
- ilan_reflexif_stage_P14.md : retour d'expérience de stage
- euille_de_route_stage_P5.md : feuille de route et contexte de cadrage

---

*Férial Zamoun · Stage Data Analyst · [GitHub](https://github.com/ferialzamoun-afk)*
