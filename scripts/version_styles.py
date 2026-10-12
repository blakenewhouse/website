"""Give the deployed stylesheet a content-specific URL to avoid stale CSS."""
from hashlib import sha256
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1] / 'personal-site' / 'dist'
css = (root / 'styles.css').read_bytes()
filename = f'styles.{sha256(css).hexdigest()[:12]}.css'
(root / filename).write_bytes(css)
for page in root.glob('*.html'):
    html = page.read_text()
    html = re.sub(r'href="styles(?:\.[a-f0-9]{12})?\.css(?:\?[^" ]*)?"',
                  f'href="{filename}"', html)
    page.write_text(html)
print(f'Versioned stylesheet: {filename}')
