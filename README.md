# Dominic Onuminya :  Portfolio

A locally hosted copy of the published portfolio at https://dominic-onuminya.figma.site/uiux, preserving its existing React application, styling, content, routes and interactions.

## Run locally

```sh
python3 scripts/serve.py
```

Open http://localhost:3000/uiux. On macOS, you can also run `./start.command`. Use `--port 3001` to select another port.

## Files

- `dist/index.html`: page shell and metadata.
- `dist/assets/app.js`: published React application bundle.
- `dist/assets/styles.css`: published styles, with local image and font references.
- `dist/assets/fonts.css`: local font definitions.
- `dist/`: downloaded portfolio images and artwork.
- `scripts/serve.py`: local server with SPA fallback for direct links and refreshes.

Routes include `/uiux`, `/graphic`, `/about`, project pages and graphic collection pages. External project, scheduling, email and social links retain their original destinations.

This is the published build, not the original Figma TypeScript source. Figma does not expose that source through the public page. There is no Node dependency installation or compilation step. Keep the server running while viewing the site; press Ctrl+C to stop it.

## AfriScale collection

Edit the design explanation and gallery entries in `content/afriscale.json`, then run `python3 scripts/update-content.py` and refresh the browser. The 13 supplied artworks are served from `dist/assets/afriscale/` as optimized JPEGs, preserving their full compositions. Original files remain unchanged.

Carousel slide manifests are in `content/carousels.json`. MeatNG has 5 slides and Mercy Agbeti Wrapped has 15 slides. Their social cards open dedicated pages. Project navigation stores the previous scroll position, and project pages include links to the next two projects.
