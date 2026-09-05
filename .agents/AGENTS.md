# Local Hermes Agent Guidelines (Gemma4) - Anveshaka Codebase

This document defines system instructions and rules for the local **Hermes Agent (powered by Gemma4)** operating in `c:\Anveshaka`.

---

## Core System Directives

1. **Keep Layout & Flow 100% Consistent**:
   - Navigation links (`HOME` / `BLOG`) use `position: absolute; top: 0; right: 0;`. Header links sit over top banners and scroll off-screen completely when reading body text.
   - Symmetrical container alignment across all pages (`max-width: 1200px; padding: 0 2rem; margin: 0 auto;`).

2. **Zero-Image Professional Layout Default**:
   - Header style defaults to `headerStyle = "minimal"` in `hugo.toml`, rendering a clean typographic dark sage header band (`#172b24`) with regular non-italic `Playfair Display` serif subheadings.

3. **Footer & Button Styling**:
   - Floating card footer uses `#172b24` dark sage background, rounded corners (`1.5rem`), scroll-to-top button, and crisp white sans-serif email text.
   - LinkedIn icon always uses official brand blue (`#0a66c2`) with `#084e96` hover state.

4. **Blog Visibility Toggle (`enableBlog`)**:
   - Set `enableBlog = false` in `hugo.toml` to launch Homepage only. Set `enableBlog = true` to reveal Blog.

5. **Useful Maintenance Commands**:
   - Preview: `hugo server --port 1313`
   - Build: `hugo`
   - Optimize Images: `python scratch/auto_process_images.py`
   - Deploy: `git add .` -> `git commit -m "update"` -> `git push origin main`
