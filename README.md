# Dino Chess

A browser-only, single-player chess game where classic pieces are redesigned as animated dinosaurs.

- **T-Rex** — King
- **Spinosaurus** — Queen
- **Ankylosaurus** — Rook
- **Pteranodon** — Bishop
- **Velociraptor** — Knight
- **Compsognathus** — Pawn

## Features

- Standard legal movement, check, checkmate, castling, en passant, promotion and stalemate
- Three computer difficulty levels
- Layered top-down dinosaur miniatures with highlights, shadows, armour details and raised bases
- Idle and running movement animations
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

## Current scope

This version uses original, layered SVG miniature artwork to create a lightweight 2.5D appearance without external assets. Fully rendered frame-by-frame idle, run and attack sprite sheets can later replace the SVG art without changing the chess engine.

## Licence

MIT. The Dino Chess name, concept implementation and included SVG artwork in this repository may be reused under the MIT licence.
