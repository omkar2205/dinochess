# Dino Chess

A browser-only, single-player chess game using a custom dinosaur-themed chess set.

- **Brachiosaurus** — King
- **T-Rex** — Queen
- **Triceratops** — Rook
- **Pterodactyl** — Bishop
- **Parasaurolophus** — Knight
- **Dinosaur Egg** — Pawn

## Features

- Standard legal movement, check, checkmate, castling, en passant, promotion and stalemate
- Three computer difficulty levels
- Final supplied artwork for the Ivory Herd and Obsidian Pack
- Static side-view and three-quarter-view pieces
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

The final supplied sheet has been cleaned, separated and normalised into a precise 6 × 2 transparent sprite at `assets/dino-pieces-final.svg`. The first row contains the Ivory Herd and the second row contains the Obsidian Pack. `style5.css` maps each chess role to the correct section of the sprite, keeping the board lightweight and ensuring all twelve pieces remain aligned consistently.

## Licence

MIT. The Dino Chess implementation and included artwork may be reused under the MIT licence.
