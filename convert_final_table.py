with open('README.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Créer la nouvelle table HTML
new_table_lines = [
    '---\n',
    '## **🎯 Compétences Data Analyst Demonstrées**\n',
    '*(Alignées sur les **blocs RNCP 37837** et les attentes métiers)*\n',
    '\n',
    '<table style="border-collapse: collapse; width: 100%; margin: 1.5em 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">\n',
    '  <thead>\n',
    '    <tr style="background-color: #155799; color: white;">\n',
    '      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;"><strong>Compétence</strong></th>\n',
    '      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;"><strong>Preuve</strong></th>\n',
    '      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;"><strong>Indicateur</strong></th>\n',
    '      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;"><strong>Bloc</strong></th>\n',
    '    </tr>\n',
    '  </thead>\n',
    '  <tbody>\n',
    '    <tr style="background-color: #f4f7fb;"><td style="padding: 9px; border: 1px solid #ddd;"><strong>Cadrer métier</strong></td><td style="padding: 9px; border: 1px solid #ddd;">Bottleneck</td><td style="padding: 9px; border: 1px solid #ddd;"><strong>825 produits</strong></td><td style="padding: 9px; border: 1px solid #ddd;"><strong>BC04</strong></td></tr>\n',
    '    <tr><td style="padding: 9px; border: 1px solid #ddd;"><strong>Contrôler qualité</strong></td><td style="padding: 9px; border: 1px solid #ddd;">P13</td><td style="padding: 9px; border: 1px solid #ddd;"><strong>18 contrôles</strong></td><td style="padding: 9px; border: 1px solid #ddd;"><strong>BC02</strong></td></tr>\n',
    '    <tr style="background-color: #f4f7fb;"><td style="padding: 9px; border: 1px solid #ddd;"><strong>Produire KPI</strong></td><td style="padding: 9px; border: 1px solid #ddd;">Dashboard</td><td style="padding: 9px; border: 1px solid #ddd;"><strong>143 680 €</strong></td><td style="padding: 9px; border: 1px solid #ddd;"><strong>BC05</strong></td></tr>\n',
    '    <tr><td style="padding: 9px; border: 1px solid #ddd;"><strong>Visualiser</strong></td><td style="padding: 9px; border: 1px solid #ddd;">Power BI</td><td style="padding: 9px; border: 1px solid #ddd;"><strong>Seuil > 15%</strong></td><td style="padding: 9px; border: 1px solid #ddd;"><strong>BC03</strong></td></tr>\n',
    '    <tr style="background-color: #f4f7fb;"><td style="padding: 9px; border: 1px solid #ddd;"><strong>Documenter</strong></td><td style="padding: 9px; border: 1px solid #ddd;">README</td><td style="padding: 9px; border: 1px solid #ddd;"><strong>Consultable</strong></td><td style="padding: 9px; border: 1px solid #ddd;"><strong>BC04</strong></td></tr>\n',
    '    <tr><td style="padding: 9px; border: 1px solid #ddd;"><strong>Modéliser</strong></td><td style="padding: 9px; border: 1px solid #ddd;">Faux Billets</td><td style="padding: 9px; border: 1px solid #ddd;"><strong>Recall 100%</strong></td><td style="padding: 9px; border: 1px solid #ddd;"><strong>BC05</strong></td></tr>\n',
    '    <tr style="background-color: #f4f7fb;"><td style="padding: 9px; border: 1px solid #ddd;"><strong>Piloter</strong></td><td style="padding: 9px; border: 1px solid #ddd;">Portfolio</td><td style="padding: 9px; border: 1px solid #ddd;"><strong>7 projets</strong></td><td style="padding: 9px; border: 1px solid #ddd;"><strong>BC04</strong></td></tr>\n',
    '  </tbody>\n',
    '</table>\n',
]

# Remplacer les lignes 300-312 par la nouvelle table
new_content = lines[:300] + new_table_lines + lines[312:]

with open('README.md', 'w', encoding='utf-8') as f:
    f.writelines(new_content)

print('✅ Dernière table convertie en HTML')
