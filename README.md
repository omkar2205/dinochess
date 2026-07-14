# Dino Chess

A browser-only, single-player chess game where classic pieces are redesigned as prehistoric fossil-bronze tokens.

- **T-Rex** — King
- **Spinosaurus** — Queen
- **Ankylosaurus** — Rook
- **Pteranodon** — Bishop
- **Velociraptor** — Knight
- **Compsognathus** — Pawn

## Features

- Standard legal movement, check, checkmate, castling, en passant, promotion and stalemate
- Three computer difficulty levels
- Style 5 fossil-bronze token artwork for the Ivory Herd and Obsidian Pack
- Static top-down pieces with a simple whole-token move transition
- Ancient stone chessboard with jungle atmosphere and torch effects
- Responsive mobile and desktop interface
- Move history, undo, board rotation and generated sound effects
- Automatic local browser saving
- No backend, account, database or API key

## Run locally

Serve the folder using a local web server because the game engine is loaded from local text modules:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## GitHub Pages

The included workflow deploys the root folder whenever `main` is updated. In the repository settings, GitHub Pages should use **GitHub Actions** as its source. The workflow also attempts first-time Pages enablement automatically.

## Artwork implementation

The twelve faction pieces are stored in one lightweight sprite sheet at `assets/style5-pieces.svg`. The SVG embeds the approved WebP token sheet, while `style5.css` maps each chess role and faction to the correct section. The earlier procedural SVG artwork remains in the game source as a fallback but is hidden by the Style 5 theme.

## Licence

MIT. The Dino Chess name, concept implementation and included artwork in this repository may be reused under the MIT licence.
