# Tala Banan Baghalian — Site personnel

Site statique hébergé sur **GitHub Pages**. Construit en HTML/CSS/JS pur — aucun framework, aucune dépendance serveur.

---

## ✍️ Publier un nouvel article

### Il suffit de deux étapes :

**1. Créer le fichier Markdown**

Dans le dossier `posts/`, créez un fichier `.md` avec ce format :

```markdown
---
title: Titre de l'article
category: Didactique
date: 2026-05-01
excerpt: Une phrase de résumé visible sous le titre sur la page d'accueil.
---

Votre contenu ici, en Markdown libre.

## Sous-titre

Paragraphes, listes, tableaux — tout est supporté.
```

**Nom du fichier :** minuscules, tirets, sans accents.
Exemple : `apprendre-avec-la-musique.md`

**Catégories disponibles :** `Didactique` · `Littérature` · `Culture` · `Linguistique` · `Réflexion personnelle`

---

**2. Pousser sur GitHub**

```bash
git add posts/apprendre-avec-la-musique.md
git commit -m "Nouvel article : Apprendre avec la musique"
git push
```

C'est tout. GitHub Actions se charge automatiquement de mettre à jour `posts/index.json` et de déployer le site en ~1 minute.

---

## ⚙️ Ce que fait GitHub Actions automatiquement

À chaque push d'un fichier `.md` dans `posts/` :

1. Lit le frontmatter YAML de chaque article
2. Reconstruit `posts/index.json` trié par date décroissante
3. Committe et pousse l'index mis à jour
4. GitHub Pages redéploie le site

Workflow : `.github/workflows/update-posts.yml`

---

## 🖼️ Image de fond (panneaux latéraux)

Déposez une image dans `assets/` puis, dans `index.html`, modifiez `TWEAK_DEFAULTS` :

```json
"wallpaperUrl": "assets/votre-image.jpg",
"wallpaperOpacity": "0.30"
```

---

## 📁 Structure du projet

```
index.html                          → Page principale
posts/
  index.json                        → Généré automatiquement, ne pas éditer
  nom-article.md                    → Vos articles (frontmatter + Markdown)
uploads/
  profile.jpeg                      → Photo de profil
.github/
  workflows/
    update-posts.yml                → Workflow d'automatisation
```

---

## 🚀 Activer GitHub Pages

1. **Settings → Pages**
2. Source : `Deploy from a branch`
3. Branch : `main` · Dossier : `/ (root)`
4. Sauvegarder

Site en ligne sur : `https://votre-nom.github.io/nom-repo/`
