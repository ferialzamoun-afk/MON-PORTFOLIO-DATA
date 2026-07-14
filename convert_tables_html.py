#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convertir les tableaux Markdown en HTML pur pour Jekyll/Cayman
"""

import re

# Lire le fichier
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# ==================== TABLE 1: RÉSULTATS P9 ====================
old_resultats = r"""### \*\*📊 Résultats\*\*
\*\(Blocs RNCP37837BC02, BC03, BC05\)\*
\| \*\*Indicateur\*\* \| \*\*Valeur\*\* \| \*\*Interprétation\*\* \| \*\*Preuve\*\* \|
\|---\|---\|---\|---\|
\| \*\*Chiffre d'affaires annuel\*\* \| \*\*480 000 €\*\* \*\(atterrissage 2023\)\* \| ✅ \*\*3 pics saisonniers identifiés\*\* \| \[kpi_analysis\.py\]\(https://github\.com/ferialzamoun-afk/P9/blob/main/src/kpi_analysis\.py\) \|
\| \*\*Clients totaux\*\* \| \*\*8 600 clients\*\* \| ✅ \*\*Segmentation clients statistiquement validée , genre, recommandations par tranches d'âge\*\* \| \[eda_analysis\.py\]\(https://github\.com/ferialzamoun-afk/P9/blob/main/src/eda_analysis\.py\) \|
\| \*\*Concentration du CA \(Indice de Gini 0,40\)\*\* \| \*\*Dépendance marqué à la catégorie1\*\* \| ⚠️ \*\*Dépendance marqué à la catégorie1\*\* \| \[courbe_pareto_80_20\.html\]\(https://github\.com/ferialzamoun-afk/P9/raw/main/output/dataviz/courbe_pareto_80_20\.html\) \|"""

new_resultats = """### **📊 Résultats**
*(Blocs RNCP37837BC02, BC03, BC05)*

<table style="width: 100%; border-collapse: collapse; margin: 1.5em 0;">
  <thead style="background-color: #155799; color: white;">
    <tr>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;"><strong>Indicateur</strong></th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;"><strong>Valeur</strong></th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;"><strong>Interprétation</strong></th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;"><strong>Preuve</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 9px; border: 1px solid #ddd;"><strong>Chiffre d'affaires annuel</strong></td>
      <td style="padding: 9px; border: 1px solid #ddd;"><strong>480 000 €</strong> <em>(atterrissage 2023)</em></td>
      <td style="padding: 9px; border: 1px solid #ddd;">✅ <strong>3 pics saisonniers identifiés</strong></td>
      <td style="padding: 9px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9/blob/main/src/kpi_analysis.py">kpi_analysis.py</a></td>
    </tr>
    <tr>
      <td style="padding: 9px; border: 1px solid #ddd;"><strong>Clients totaux</strong></td>
      <td style="padding: 9px; border: 1px solid #ddd;"><strong>8 600 clients</strong></td>
      <td style="padding: 9px; border: 1px solid #ddd;">✅ <strong>Segmentation clients statistiquement validée, genre, recommandations par tranches d'âge</strong></td>
      <td style="padding: 9px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9/blob/main/src/eda_analysis.py">eda_analysis.py</a></td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 9px; border: 1px solid #ddd;"><strong>Concentration du CA (Indice de Gini 0,40)</strong></td>
      <td style="padding: 9px; border: 1px solid #ddd;"><strong>Dépendance marquée à la catégorie 1</strong></td>
      <td style="padding: 9px; border: 1px solid #ddd;">⚠️ <strong>Dépendance marquée à la catégorie 1</strong></td>
      <td style="padding: 9px; border: 1px solid #ddd;"><a href="https://github.com/ferialzamoun-afk/P9/raw/main/output/dataviz/courbe_pareto_80_20.html">courbe_pareto_80_20.html</a></td>
    </tr>
  </tbody>
</table>"""

content = re.sub(old_resultats, new_resultats, content, flags=re.MULTILINE)

# Écrire
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Tableau Résultats converti en HTML")
