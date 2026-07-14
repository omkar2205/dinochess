(() => {
  "use strict";
  const parts = [1, 2, 3, 4, 5, 6].map((number) => `game-parts/part-${number}.txt`);
  Promise.all(parts.map(async (url) => {
    const response = await fetch(url, { cache: "no-cache" });
    if (!response.ok) throw new Error(`Could not load ${url}`);
    return response.text();
  }))
    .then((sourceParts) => {
      const source = sourceParts.join("\n");
      Function(source)();
    })
    .catch((error) => {
      console.error(error);
      const board = document.getElementById("board");
      if (board) board.innerHTML = `<p style="padding:2rem;color:white">Dino Chess could not load. Please refresh the page.</p>`;
    });
})();
