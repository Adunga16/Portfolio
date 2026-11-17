#!/usr/bin/env python3
"""Apply editable AfriScale collection data to the published application bundle."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = json.loads((root / 'content/afriscale.json').read_text())
bundle = root / 'dist/assets/app.js'
text = bundle.read_text()
start = text.index('{"slug":"afriscale-branding"')
_, length = json.JSONDecoder().raw_decode(text[start:])
end = start + length
bundle.write_text(text[:start] + json.dumps(content, ensure_ascii=False, separators=(',', ':')) + text[end:])
print('Updated AfriScale collection.')
