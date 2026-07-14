import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Trouver et remplacer la table Compétences Data Analyst
pattern = r'\| \*\*Compétence\*\* \| \*\*Preuve\*\* \|.*?(?=\n------)'

new_table = '''<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <thead>
    <tr style="background-color: #155799; color: white;">
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;"><strong>Compétence</strong></th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;"><strong>Preuve</strong></th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;"><strong>Indicateur</strong></th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;"><strong>Bloc</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f4f7fb;"><td style="padding: 8px; border: 1px solid #ddd;"><strong>Cadrer métier</strong></td><td style="padding: 8px; border: 1px solid #ddd;">Bottleneck</td><td style="padding: 8px; border: 1px solid #ddd;"><strong>825 produits</strong></td><td style="padding: 8px; border: 1px solid #ddd;"><strong>BC04</strong></td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;"><strong>Contrôler qualité</strong></td><td style="padding: 8px; border: 1px solid #ddd;">P13</td><td style="padding: 8px; border: 1px solid #ddd;"><strong>18 contrôles</strong></td><td style="padding: 8px; border: 1px solid #ddd;"><strong>BC02</strong></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 8px; border: 1px solid #ddd;"><strong>Produire KPI</strong></td><td style="padding: 8px; border: 1px solid #ddd;">Dashboard</td><td style="padding: 8px; border: 1px solid #ddd;"><strong>143 680 €</strong></td><td style="padding: 8px; border: 1px solid #ddd;"><strong>BC05</strong></td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;"><strong>Visualiser</strong></td><td style="padding: 8px; border: 1px solid #ddd;">Power BI</td><td style="padding: 8px; border: 1px solid #ddd;"><strong>Seuil > 15%</strong></td><td style="padding: 8px; border: 1px solid #ddd;"><strong>BC03</strong></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 8px; border: 1px solid #ddd;"><strong>Documenter</strong></td><td style="padding: 8px; border: 1px solid #ddd;">README</td><td style="padding: 8px; border: 1px solid #ddd;"><strong>Consultable</strong></td><td style="padding: 8px; border: 1px solid #ddd;"><strong>BC04</strong></td></tr>
    <tr><td style="padding: 8px; border: 1px solid #ddd;"><strong>Modéliser</strong></td><td style="padding: 8px; border: 1px solid #ddd;">Faux Billets</td><td style="padding: 8px; border: 1px solid #ddd;"><strong>Recall 100%</strong></td><td style="padding: 8px; border: 1px solid #ddd;"><strong>BC05</strong></td></tr>
    <tr style="background-color: #f4f7fb;"><td style="padding: 8px; border: 1px solid #ddd;"><strong>Piloter</strong></td><td style="padding: 8px; border: 1px solid #ddd;">Portfolio</td><td style="padding: 8px; border: 1px solid #ddd;"><strong>7 projets</strong></td><td style="padding: 8px; border: 1px solid #ddd;"><strong>BC04</strong></td></tr>
  </tbody>
</table>'''

fixed = re.sub(pattern, new_table, content, flags=re.DOTALL)

if fixed == content:
    print("❌ AUCUN MATCH")
else:
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print("✅ Table Compétences Data Analyst convertie")
