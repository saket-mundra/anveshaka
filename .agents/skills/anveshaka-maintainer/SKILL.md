---
name: anveshaka-maintainer
description: Skill for local Hermes agent (Gemma4) to maintain, write posts, optimize images, and deploy the Anveshaka Hugo static website.
---

# Anveshaka Maintainer Skill (Gemma4 / Hermes Local Agent)

This skill equips the Hermes local LLM agent (running Gemma4) to maintain the **Anveshaka** Hugo codebase (`c:\Anveshaka`), create new blog posts, auto-optimize images, and execute Git deployments.

---

## 1. Creating a New Blog Post

When the user asks to write or publish a new post:

1. Create a new Markdown file inside `content/posts/`:
   - File path format: `content/posts/my-post-title.md`
   - Frontmatter template:
     ```markdown
     ---
     title: "Your Post Title Here"
     date: YYYY-MM-DDT12:00:00Z
     description: "A short 1-2 sentence summary of the post."
     tags: ["Reflection", "Investing"]
     draft: false
     ---

     Your essay content in Markdown format goes here...
     ```

2. Note: **No cover photo is required** for new blog posts! The essay stream layout (`list.html`) automatically renders posts beautifully using pure typography and spacing.

---

## 2. Automatic Image Optimization Workflow

If the user provides raw photography (e.g., placing `.jpg` or `.png` files in `Website Images/`):

1. Execute the automated Python processing script:
   ```powershell
   python scratch/auto_process_images.py
   ```
2. The script automatically crops and resizes images into `static/images/` as web-optimized 3:2 cards (`-card.jpg`) and 16:9 banners (`-banner.jpg`).

---

## 3. Local Development & Preview Commands

- **Start Preview Server**:
  ```powershell
  hugo server --port 1313
  ```
  Open `http://localhost:1313/` in your browser.

- **Check Hugo Build Status**:
  ```powershell
  hugo
  ```

---

## 4. Toggling Blog Visibility (`enableBlog`)

- **Hide Blog (Homepage Only Launch)**: Set `enableBlog = false` in `hugo.toml`.
- **Show Blog (Live Essays Stream)**: Set `enableBlog = true` in `hugo.toml`.

---

## 5. Deploying to GitHub & Cloudflare Pages

When the user asks to push changes or publish live:

```powershell
# 1. Stage changes
git add .

# 2. Commit with descriptive message
git commit -m "content: add new post and deploy site"

# 3. Push to remote main branch (triggers Cloudflare Pages build)
git push origin main
```

---

## 6. Invariant Architecture Rules

- **Header Navigation**: Always maintain `.site-header` with `position: absolute; top: 0; right: 0;`. Navigation links (`HOME` / `BLOG`) sit over top banners and scroll off-screen completely when reading body text.
- **Blog Header & Footer Palette**: Minimal header bands (`.blog-header-minimal` & `.post-header-minimal`) and the floating footer card MUST share the exact same `#172b24` dark sage background and crisp white typography.
- **LinkedIn Button**: Always use official LinkedIn blue (`#0a66c2`) with `#084e96` hover state.
- **Subheadings**: Never italicize blog header subheadings; always use regular `Playfair Display` serif (`font-style: normal`).
- **Symmetrical 1200px Grid**: All pages (Home, Blog List, Post detail) MUST use `.container { width: 100%; max-width: 1200px; padding: 0 2rem; margin: 0 auto; }`.
