# Fiabilisation des donnees d'une boutique en ligne

Projet de consolidation et de fiabilisation de donnees operationnelles d'une boutique en ligne afin de reduire les ecarts entre systemes et de mieux piloter les ventes.

## Contexte

Une boutique en ligne s'appuie sur plusieurs sources (ERP, web, gestion) qui peuvent generer des ecarts de prix, de stocks et de referentiels.
L'enjeu du projet est de produire une base plus fiable pour l'analyse et la decision.

## Objectif metier

Mettre en coherence les donnees pour:

- detecter les anomalies,
- consolider les indicateurs de vente,
- faciliter les arbitrages operationnels et commerciaux.

## Perimetre des donnees et sources

- Donnees issues de plusieurs systemes de gestion et de vente.
- Synthese des anomalies disponible dans le fichier de resultat de phase 1.
- Support de presentation pour formaliser le cadrage et les conclusions.

## Methode

1. Identification des ecarts entre sources.
2. Nettoyage et standardisation des donnees.
3. Consolidation d'une vue unique exploitable.
4. Detection des anomalies et categorisation des ecarts.
5. Formalisation des recommandations metier.

## Resultats et livrables

- Synthese des anomalies de phase 1.
- Support de presentation du projet.
- Base de travail consolidee pour la lecture des donnees de la boutique.

## Limites et suites

- La robustesse du dispositif depend de la qualite des regles de rapprochement entre systemes.
- Une suite utile est l'automatisation des controles de coherence et de la detection d'anomalies.
- L'etape suivante peut etre la mise en place d'un dashboard de suivi des ecarts.

## Preuve de competences

### Resultats de veille metier

- Veille sur les problemes classiques de fiabilite data en contexte e-commerce: prix, stocks, referentiels, ecarts multi-sources.
- Traduction en besoins metier: consolidations, controles, priorisation des anomalies.
- Apport metier: meilleure capacite a comprendre l'origine des ecarts et a agir vite.

### Resultats de veille technologique

- Veille sur les bonnes pratiques de nettoyage, reconciliation et controle de qualite des donnees.
- Choix retenus: approche progressive de consolidation et mise en evidence des anomalies les plus significatives.
- Apport technique: base plus robuste et plus lisible pour la suite des traitements.

### Tracabilite des preuves

- Competence: qualifier des ecarts de donnees | Action: synthese des anomalies detectees | Preuve: assets/phase1_anomalies_synthese.xlsx.
- Competence: formaliser une demarche data | Action: cadrage et restitution du projet | Preuve: assets/Zamoun_Férial_1_presentation_112025.pdf.
- Competence: produire une analyse exploitable | Action: consolidation et recommandations | Preuve: livrables du projet et support de synthese.

## Ressources du projet

- Synthese anomalies phase 1: assets/phase1_anomalies_synthese.xlsx
- Presentation: assets/Zamoun_Férial_1_presentation_112025.pdf

## Liens utiles

- Tableau de bord Optimisation des ventes d'une boutique: https://p6-dashboard-wdcn5o8grt39nqtim6mgym.streamlit.app/
- Depot source initial Bottleneck: https://github.com/ferialzamoun-afk/OC_P6_Optimisation_des_donnees_dune_boutique_en_Python
- Version portfolio a publier: P13 Partie 1 amelioree, avec notebook refactore, controles qualite, documentation IA et preuves de competences.
- Repo SOC monitoring: https://github.com/ferialzamoun-afk/soc-data-anomaly-monitoring
- Dashboard public: https://soc-data-anomaly-monitoring-of3oufewjpbvav6ekbs6wr.streamlit.app/

## Auteur

Ferial Zamoun
Formation Data Analyst - GRETA Promo 2025
Objectif: alternance en data
