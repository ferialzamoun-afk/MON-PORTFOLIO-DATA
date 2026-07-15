# 🎯 Proof Point : P11 — Étude de Marché

## 1️⃣ Contexte
La mission consistait à prioriser des pays d’export pour des poulets biologiques afin d’orienter la stratégie commerciale.

## 2️⃣ Données
- **Sources** : données multi-sources FAO / Banque Mondiale / textes réglementaires.
- **Qualité** : couverture partielle et données lourdes non embarquées dans le dépôt.
- **Limites** : clustering non labellisé et dépendance à la qualité des sources externes.

## 3️⃣ Démarche
- Préparation et EDA.
- Feature engineering sur les textes FAOLEX.
- ACP, CAH, KMeans, tests unitaires et CI GitHub Actions.

## 4️⃣ Résultats + Impact
- 138 pays, 16 variables candidates.
- 11 variables actives en ACP, 3 composantes principales.
- 89,90 % de variance conservée et top 5 pays à approfondir, dont la Suisse.

## 5️⃣ Limites & Pistes
- Affiner les clusters si l’on enrichit le jeu de données.
- Compléter par des données commerciales réelles.
- Valider la stratégie terrain avant décision finale.

**Référence** : [README projet](README.md)
