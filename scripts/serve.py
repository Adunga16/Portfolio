#!/usr/bin/env python3
"""Serve the portfolio with client-side route fallback."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1] / 'dist'
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def do_GET(self):
        path = self.path.split('?', 1)[0]
        if not Path(self.translate_path(path)).exists() and '.' not in path.rsplit('/', 1)[-1]:
            self.path = '/index.html'
        super().do_GET()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=3000)
    args = parser.parse_args()
    print(f'Portfolio running at http://localhost:{args.port}/uiux', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), Handler).serve_forever()
