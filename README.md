# Dino Chess

A browser-only, single-player chess game where classic pieces are redesigned as scalable dinosaur SVG icons.

- **Brachiosaurus** — King
- **T-Rex** — Queen
- **Triceratops** — Rook
- **Pterodactyl** — Bishop
- **Parasaurolophus** — Knight
- **Dinosaur Egg** — Pawn

## Features

- Standard legal movement, check, checkmate, castling, en passant, promotion and stalemate
- Three computer difficulty levels
- True vector dinosaur artwork for the Ivory Herd and Obsidian Pack
- Static side-view and three-quarter-view piece silhouettes
- Simple whole-piece movement transition
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

The full set is stored in `assets/dino-pieces.svg` as one editable SVG symbol sprite. Each piece is made from vector paths, fills, gradients and strokes rather than an embedded raster image. The game inserts the correct symbol using an external SVG `<use>` reference, keeping the artwork sharp at every board size while avoiding twelve separate network requests.

## Licence

MIT. The Dino Chess name, concept implementation and included SVG artwork in this repository may be reused under the MIT licence.
