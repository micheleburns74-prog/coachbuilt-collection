"""Builds dist/coachbuilt-collection.html: index.html with styles.css and app.js inlined,
so the whole app is one portable file (this is the form that was published as a Claude artifact).
Run:  python tools/build_single_file.py"""
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
read = lambda n: open(os.path.join(ROOT, n), encoding='utf-8').read()
html = read('index.html')
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + read('styles.css') + '</style>')
html = html.replace('<script src="app.js"></script>', '<script>\n' + read('app.js') + '</script>')
os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
out = os.path.join(ROOT, 'dist', 'coachbuilt-collection.html')
open(out, 'w', encoding='utf-8').write(html)
print('wrote', out, len(html), 'bytes')
