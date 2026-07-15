# 🎯 Proof Point : P6 — Optimisation Bottleneck

## 1️⃣ Contexte
Bottleneck devait réconcilier trois sources de données (ERP, Web, Liaison) afin de fournir une vue exploitable au CODIR. L’enjeu était de fiabiliser les données et de transformer un livrable exploratoire en support décisionnel.

## 2️⃣ Données
- **Sources** : 825 lignes ERP, 1 513 Web, 825 Liaison.
- **Qualité** : doublons, incohérences, anomalies prix/stocks et contrôles qualité nécessaires.
- **Limites** : snapshot d’un mois, pas d’historique long, corrélations non causales.

## 3️⃣ Démarche
- Notebook Python/Pandas structuré en modules réutilisables.
- Nettoyage, rapprochement des sources, EDA, calcul de KPI et dataviz.
- IA utilisée de façon documentée pour accélérer l’itération et la traçabilité.

## 4️⃣ Résultats + Impact
- Notebook réduit à 49 cellules contre 148 initialement.
- Environ 1 min 11 s d’exécution.
- 18 contrôles qualité, 13 graphiques, 26 prompts IA tracés.
- KPI notables : CA total 143 680 EUR/mois, 689 produits avec CA, marge moyenne 47,32 %.

## 5️⃣ Limites & Pistes
- Fenêtre temporelle trop courte pour des tendances robustes.
- Migration prévue vers Great Expectations v19+.
- Poursuivre le suivi multi-mois et le monitoring des anomalies.

**Référence** : [README projet](README.md)
