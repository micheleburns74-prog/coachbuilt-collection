"""Smoke test: opens every tab at desktop and phone width, checks for JavaScript errors,
empty pages and sideways scrolling, then tests the search box.
Run:  pip install playwright && playwright install chromium && python tests/smoke_test.py"""
import os, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
URL = 'file://' + ROOT + '/index.html'
TABS = ['home', 'rr', 'bentley', 'italian', 'quiz', 'compare', 'glossary', 'market',
        'timeline', 'builders', 'people', 'identify', 'sources', 'news']
failed = []

with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h in [(1200, 900), (390, 800)]:
        pg = b.new_page(viewport={'width': w, 'height': h})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(URL); pg.wait_for_timeout(500)
        for t in TABS:
            pg.evaluate(f"go('{t}')"); pg.wait_for_timeout(80)
            sel = '#' + t + ('Detail' if t in ('rr', 'bentley', 'italian') else '')
            if len(pg.inner_text(sel)) < 20:
                failed.append(f'{w}px {t}: empty')
            if pg.evaluate('document.documentElement.scrollWidth') > w + 2:
                failed.append(f'{w}px {t}: sideways scroll')
        for term, minimum in [('Barnato', 1), ('Scaglietti', 1), ('Zagato', 1)]:
            pg.fill('#sq', term)
            if pg.evaluate("document.querySelectorAll('#sres button').length") < minimum:
                failed.append(f'{w}px search {term}: no results')
        failed += [f'{w}px JS error: {e}' for e in errs]
    b.close()

print('PASS' if not failed else 'FAIL\n' + '\n'.join(failed))
sys.exit(1 if failed else 0)
