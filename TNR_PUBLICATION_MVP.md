# Cahier de Recette TNR Publication MVP

## Objet
Figer un etat des lieux du portfolio avant publication intermediaire GitHub Pages, afin d'eviter les regressions de rendu, de navigation et de publication.

## Perimetre MVP
- Depot de publication : `MON-PORTFOLIO-DATA`
- Cible : GitHub Pages + verification locale Jekyll
- Pages prioritaires : accueil, P13, P12, P11, P10, P9, P8
- Hors MVP : refonte editoriale complete, industrialisation des liens via manifest, publication des depots autonomes

## Legende
- `OK` : verifie et conforme dans le build local
- `CORRIGE` : defect confirme puis corrige, rebuild valide
- `A_RECHECK` : point connu encore a verifier avant publication
- `HORS_MVP` : volontairement reporte

## Decision MVP
- Statut global : `PUBLIER AVEC RESERVE`
- Raison : les principales regressions de rendu sont corrigees, mais un controle final de navigation accueil reste necessaire avant push public

## Matrice TNR

| ID | Zone | Controle attendu | Local Jekyll | GitHub Pages cible | Statut | Risque | Action / remarque |
|----|------|------------------|--------------|--------------------|--------|--------|-------------------|
| TNR-001 | Boot Jekyll local | `bundle install` puis build fonctionnels | OK | N/A | CORRIGE | Moyen | `Gemfile` ajoute et build valide |
| TNR-002 | URL locale | La page d'accueil s'ouvre sur `/` et non `/MON-PORTFOLIO-DATA/` | OK | N/A | CORRIGE | Faible | Documentation locale mise a jour |
| TNR-003 | Performance locale | Build local raisonnable pour revue | OK | N/A | CORRIGE | Faible | Mode dev valide autour de 35-40 s |
| TNR-004 | Accueil / Couverture RNCP 37837 | Tableau HTML visible et aligne | OK | A confirmer au prochain deploy | OK | Moyen | Verifie dans `_site/index.html` |
| TNR-005 | Accueil / Projets phares acces rapide | Liens vers pages rendues et non `README.md` bruts | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Index Jekyll ajoutes pour P13/P12/P11/P10/P9/P8 |
| TNR-006 | Accueil / Recruteur-Client / lien P13 | Lien renvoie vers page rendue P13 | OK | A confirmer au prochain deploy | CORRIGE | Faible | Pointe maintenant vers `/projets/P13_portfolio/` |
| TNR-007 | Accueil / Synthese Proof Points | Lien ouvre une page rendue lisible | OK | A confirmer au prochain deploy | OK | Faible | Sortie observee en `.html` |
| TNR-008 | Accueil / Veille techno-metier | Liens resolus et lisibles | OK | A confirmer au prochain deploy | CORRIGE | Faible | Pointe maintenant vers `/veille/techno/` et `/veille/métier/` |
| TNR-009 | P13 | Rendu global lisible | OK | A confirmer au prochain deploy | OK | Faible | Aucun defect bloquant remonte |
| TNR-010 | P12 / tableaux RNCP | Tableaux rendus en HTML | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Tables normalisees + rebuild valide |
| TNR-011 | P12 / Preuves et Livrables | Tableau rendu correctement | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Valide dans HTML genere |
| TNR-012 | P11 / Demarrage rapide | Bloc commandes rendu proprement | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Bloc stabilise |
| TNR-013 | P11 / Qualite Logicielle | Section independante et lisible | OK | A confirmer au prochain deploy | CORRIGE | Faible | Titre et listes corrigees |
| TNR-014 | P11 / Mapping RNCP 37837 | Liste / structure non fusionnee | OK | A confirmer au prochain deploy | CORRIGE | Faible | HTML genere correct |
| TNR-015 | P10 / Installation | Bloc `bash` et structure homogènes | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Section reecrite |
| TNR-016 | P10 / Qualite des Donnees | Tableau rendu en HTML | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Defect capture utilisateur corrige |
| TNR-017 | P10 / Mapping RNCP 37837 | Liste proprement alignee | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Defect capture utilisateur corrige |
| TNR-018 | P9 / Configuration et Execution | Sections et blocs commandes lisibles | OK | A confirmer au prochain deploy | CORRIGE | Faible | Structure normalisee |
| TNR-019 | P9 / Publication des donnees | Mention explicite d'absence de donnees nominatives directes | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Garde-fou editorial ajoute |
| TNR-020 | P8 / Stack Technique | Tableau rendu en HTML | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Defect capture utilisateur corrige |
| TNR-021 | P8 / Modele de Donnees (3 couches) | Schema rendu dans un bloc texte propre | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Bloc `text` ajoute |
| TNR-022 | P8 / Processus dbt | Sections 1/2/3 et blocs SQL rendus correctement | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Blocs fermes et titres normalises |
| TNR-023 | P8 / Pipeline CI-CD et Artefacts | Tableaux et sous-sections alignes | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Reecriture de la seconde moitie du README |
| TNR-024 | P8 / Mapping RNCP 37837 | Liste finale non aplatie | OK | A confirmer au prochain deploy | CORRIGE | Moyen | Verifie dans `_site` |
| TNR-025 | Publication publique / secrets | Aucun secret exploitable dans la documentation publique | OK | A confirmer au prochain deploy | CORRIGE | Eleve | P8 assaini, scan texte sans secret reel detecte |
| TNR-026 | Publication publique / donnees perso | Pas de donnees nominatives directes documentees dans P8/P9 | OK | A confirmer au prochain deploy | CORRIGE | Eleve | Verification texte des README P8/P9: aucun nom, email ou identifiant client nominatif expose |
| TNR-027 | Depot portfolio / bruit de build | `_site`, `.jekyll-metadata`, `Gemfile.lock` etc. non pousses par erreur | Partiel | N/A | CORRIGE | Faible | `_site/`, `.jekyll-metadata` et `.sass-cache/` ignores; verifier simplement le scope du commit |

## Points de vigilance avant freeze MVP
1. Faire un dernier controle manuel sur les liens d'accueil apres rebuild.
2. Conserver un controle ponctuel des pages P8/P9 sur les aspects publication publique et donnees non nominatives si les sources changent.
3. Verifier le scope exact du commit MVP avant push public.

## Critere de Go / No-Go

### Go MVP
- Tous les statuts `CORRIGE` restent conformes apres rebuild local
- Les points `A_RECHECK` critiques de l'accueil sont leves
- Aucun secret exploitable ni detail d'acces prive dans les pages publiees

### No-Go MVP
- Un tableau cle redevient texte brut
- Un lien d'accueil renvoie encore vers un `README.md` brut au lieu d'une page rendue
- Un contenu de build local ou une information sensible se retrouve dans le commit public

## Commandes de verification minimales
```bash
bundle exec jekyll clean
bundle exec jekyll build --config _config.yml,_config.dev.yml
bundle exec jekyll serve --config _config.yml,_config.dev.yml --livereload --incremental
```

## Suite recommandee
1. Lever les `A_RECHECK` accueil
2. Committer uniquement le scope MVP
3. Publier une version intermediaire GitHub Pages
4. Ouvrir un second lot pour harmonisation editoriale et industrialisation des liens