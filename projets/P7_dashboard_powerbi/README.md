# 📊 P7 — Dashboard Décisionnel Power BI — SANITORAL

> **Type** : Dashboard Power BI · Reporting décisionnel · Multi-persona
> **Date** : 2025
> **Outil** : Power BI Desktop

---

## 🎯 1. Contexte et besoin métier

**Mission** : produire un reporting décisionnel pour SANITORAL afin de faciliter les arbitrages de pilotage projets à trois niveaux de gouvernance.

**Pour qui** :

| Profil | Besoin |
|--------|--------|
| **Directeur Général** | Vision portefeuille, arbitrage stratégique (poursuite / priorisation / arrêt) |
| **Directeur Régional** | Isolation des projets en risque, alertes sur dépassements coût/délai/livrables |
| **Directeur Pays** | Suivi opérationnel détaillé, comparaison prévisionnel/réalisé, actions correctives |

**Problème** : les informations de coût, délai et avancement sont éparpillées — aucune vue consolidée ne permet des arbitrages rapides en comité de pilotage.

**Enjeux** :
- Prioriser les projets en alerte (seuil : écart > 15%)
- Segmenter l'analyse par département (IT vs Marketing), régions et phases
- Réduire le temps de décision en comité de pilotage

**Périmètre** :
- Axes de comparaison : IT vs Marketing · régions · pays · phases projet
- Granularité : portefeuille → projet → phase
- Phases suivies : A à F selon le modèle de données retenu

---

## 🧭 2. Démarche analytique

**Étapes de conception** :
1. Cadrage des besoins par persona (DG, DR, DP) via Product Strategy Canvas
2. Modélisation des données (relations, ajustements, référentiel de phases)
3. Construction des dashboards différenciés par profil utilisateur
4. Définition des indicateurs d'alerte et des KPI par niveau
5. Intégration d'un onglet de documentation (canvas, procédure de mise à jour, modèle de données)
6. Validation de la narration métier pour la soutenance

**Choix de conception** :
- Dashboards différenciés par persona → réduction du bruit informationnel
- Seuil d'alerte 15% explicite → priorisation immédiate des actions
- Vues structurées pour l'action et non pour la contemplation

**Limites et points d'attention** :
- Valider définitivement le référentiel de phases (A-F ou 1-4) pour stabiliser les comparaisons
- Industrialiser le processus de mise à jour des données
- Ajouter un suivi temporel des alertes pour mesurer l'efficacité des actions correctives

---

## 📊 3. Résultats et livrables

| Livrable | Description |
|---------|-------------|
| Dashboard DG | Vision portefeuille, alertes stratégiques, comparaison IT/Marketing |
| Dashboard DR | Projets en risque par région, alertes phases, dépassements |
| Dashboard DP | Détail opérationnel par projet, prévisionnel vs réalisé |
| Onglet documentation | Product Strategy Canvas + procédure mise à jour + modèle de données |
| Support de soutenance | Storytelling incluant prise de parole orientée décision |

---

## 🎓 4. Compétences RNCP 37837 mobilisées

| Bloc | Compétence | Ce qui a été fait | Preuve |
|------|-----------|------------------|--------|
| **BC02** | Identifier et collecter | Collecte données coût/délai/avancement SANITORAL | Sources projet |
| **BC02** | Vérifier la cohérence | Validation référentiel phases et relations | Modèle de données |
| **BC03** | Solution de visualisation | 3 dashboards Power BI différenciés par profil | Dashboards DG / DR / DP |
| **BC03** | Créer un tableau de bord | Dashboard multi-pages opérationnel sous Power BI | Fichier PBIX |
| **BC03** | Reporting des tendances | Seuil d'alerte 15%, KPI cards, comparaisons IT/Marketing | Pages KPI |
| **BC03** | Présenter les résultats | Support storytelling pour soutenance devant jury | Présentation |
| **BC04** | Identifier le besoin métier | Product Strategy Canvas — 3 personas définis | Onglet documentation |
| **BC04** | Formaliser le cahier des charges | Procédure de mise à jour et modèle de données documentés | Onglet documentation |
| **BC04** | Adapter sa posture | Positionnement consultant — challenger les besoins | Canvas + dashboard |

---

## 💡 5. Impact et apprentissages

**Ce que ça a apporté** : un dispositif de pilotage consolidé permettant des arbitrages plus rapides en comité de direction, avec une lisibilité immédiate des priorités et des alertes.

**Veille métier** : pratiques de pilotage de portefeuille projets et gouvernance multi-niveaux (global, régional, local) → traduction en besoins analytiques concrets par profil décisionnaire.

**Veille technologique** : bonnes pratiques de visualisation décisionnelle Power BI (hiérarchie des indicateurs, infobulles, lisibilité des alertes) → vues différenciées pour l'action.

---

## 🔗 Ressources

- Dashboards Power BI : ssets/
- Support de soutenance : ssets/

---

*Férial Zamoun · Formation Data Analyst GRETA Promo 2025 · [GitHub](https://github.com/ferialzamoun-afk)*
