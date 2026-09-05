# Anveshaka: Local Hermes Agent (Gemma4) Maintenance Guide

This guide explains how to use your local **Hermes Agent running Gemma4** to maintain, update, write posts, and deploy **Anveshaka** directly without relying on third-party tools.

---

## 1. Structure Created for Hermes / Gemma4
- **Skill Instructions**: [.agents/skills/anveshaka-maintainer/SKILL.md](file:///c:/Anveshaka/.agents/skills/anveshaka-maintainer/SKILL.md)
- **Agent Rules**: [.agents/AGENTS.md](file:///c:/Anveshaka/.agents/AGENTS.md)
- **Image Optimizer**: [scratch/auto_process_images.py](file:///c:/Anveshaka/scratch/auto_process_images.py)

---

## 2. Prompts You Can Give Hermes (Gemma4)

### A. To Add a New Post:
> *"Hermes, please write a new post titled 'Reflections on Silence' under content/posts/reflections-on-silence.md with tags Reflection and Stillness."*

### B. To Process New Photos:
> *"Hermes, I added new photos to Website Images. Please run the image optimization script to process them into web formats."*

### C. To Preview the Site:
> *"Hermes, launch the local preview server."* (Runs `hugo server --port 1313`)

### D. To Publish Changes Live:
> *"Hermes, commit all changes and push to GitHub."* (Runs `git add .`, `git commit`, `git push origin main` -> triggers Cloudflare Pages auto-build).

---

### E. To Reveal / Hide the Blog:
> *"Hermes, set enableBlog = true in hugo.toml and push live."* (Toggles blog visibility instantly)

---

## 3. Maintenance Rules Registered
1. **Blog Visibility Toggle (`enableBlog`)**: Controlled via `enableBlog = false` (Homepage launch) or `enableBlog = true` (Reveal Blog) in `hugo.toml`.
2. **Zero-Image Professional Layout**: Default `headerStyle = "minimal"` renders a clean typographic dark sage header band (`#172b24`) with regular non-italic `Playfair Display` serif subheadings.
3. **Header & Footer Palette**: Top header bands and bottom floating card footer share `#172b24` dark sage background and crisp white typography.
4. **LinkedIn Button**: Always rendered in official LinkedIn brand blue (`#0a66c2`) with `#084e96` hover state.
5. **Symmetrical 1200px Grid**: Left AND right margins are locked to `2rem` padding on a `1200px` container grid across Home, Blog, and Post pages.
6. **Header Navigation**: Links (`HOME` / `BLOG`) use `position: absolute; top: 0; right: 0;` and scroll off-screen completely during reading.
