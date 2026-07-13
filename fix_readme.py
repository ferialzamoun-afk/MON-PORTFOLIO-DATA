#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger les liens P9 et supprimer la section Bottleneck doublon
"""

import re

# Lire le fichier avec encodage UTF-8
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix P9 link markdown (space before parenthesis)
content = re.sub(
    r'\[🔗 P9 – Lapage\] \(',
    '[🔗 P9 – Lapage](',
    content
)

# Remove trailing space after repo URL
content = re.sub(
    r'\(https://github\.com/ferialzamoun-afk/P9_analyses_ventes_librairies \)',
    '(https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies)',
    content
)

# 2. Fix notebook links (old P9 -> P9_analyses_ventes_librairies)
content = re.sub(
    r'https://nbviewer\.org/github/ferialzamoun-afk/P9/blob/main/notebooks/01%20-%20Inspection%20des%20données\.ipynb',
    'https://nbviewer.org/github/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/lapage_project/notebooks/analyses/01_Exploration_et_nettoyage.ipynb',
    content
)

content = re.sub(
    r'https://nbviewer\.org/github/ferialzamoun-afk/P9/blob/main/notebooks/02%20-%20Préparation%20et%20nettoyage\.ipynb',
    'https://nbviewer.org/github/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/lapage_project/notebooks/analyses/02_Analyses_Marketing.ipynb',
    content
)

content = re.sub(
    r'https://nbviewer\.org/github/ferialzamoun-afk/P9/blob/main/notebooks/03%20-%20Analyses%20des%20groupements\.\.\.ipynb',
    'https://nbviewer.org/github/ferialzamoun-afk/P9_analyses_ventes_librairies/blob/main/lapage_project/notebooks/analyses/03_Analyses_Statistiques.ipynb',
    content
)

# 3. Fix reports paths to outputs
content = re.sub(
    r'https://github\.com/ferialzamoun-afk/P9/tree/main/reports/exports/',
    'https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/lapage_project/outputs',
    content
)

content = re.sub(
    r'https://github\.com/ferialzamoun-afk/P9/tree/main/reports/figures/',
    'https://github.com/ferialzamoun-afk/P9_analyses_ventes_librairies/tree/main/lapage_project/outputs/figures',
    content
)

# 4. Remove duplicate Bottleneck section (Section 4)
# This matches from "------\n------" before section 4 to just before "## **🎯 Compétences Data Analyst"
bottleneck_pattern = r'------\s+------\s+### \*\*🔹 4\. Fiabilisation de Données E-Commerce.*?(?=---\s+## \*\*🎯 Compétences Data Analyst Demonstrées\*\*)'
content = re.sub(bottleneck_pattern, '------\n---\n', content, flags=re.DOTALL)

# 5. Remove "Application Portfolio" placeholder section
app_portfolio_pattern = r'---\s+## \*\*💻 Application Portfolio\*\*.*?(?=---)'
content = re.sub(app_portfolio_pattern, '---\n', content, flags=re.DOTALL)

# Write back
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ README.md fixed successfully!")
