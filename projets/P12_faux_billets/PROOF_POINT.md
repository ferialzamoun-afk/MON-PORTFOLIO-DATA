# 🎯 Proof Point : P12 — Détection de Faux Billets

## 1️⃣ Contexte
Le projet répond à un besoin ONFM de détection rapide de faux billets pour réduire les faux négatifs et automatiser le tri.

## 2️⃣ Données
- **Sources** : dataset ONFM avec labels et mesures géométriques.
- **Qualité** : pas de base SQL, pas de séries temporelles, structure simple et exploitable.
- **Limites** : périmètre limité aux billets en euros.

## 3️⃣ Démarche
- Notebook unique structuré : chargement, nettoyage, EDA, modélisation, évaluation.
- Scikit-learn pour la pipeline, le split stratifié et les modèles.
- Préparation d’une intégration API FastAPI.

## 4️⃣ Résultats + Impact
- Accuracy 88 %.
- Recall 100 % sur les faux billets.
- F1-score 0,91 et précision 89 %.
- Livrables : notebook, dépôt GitHub, slides et visualisations.

## 5️⃣ Limites & Pistes
- Tester d’autres modèles comme XGBoost ou Random Forest.
- Ajouter du monitoring et du logging en production.
- Explorer un pipeline CNN ou d’automatisation FastAPI.

**Référence** : [README projet](README.md)
