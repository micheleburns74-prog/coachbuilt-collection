"""Regenerates the images in docs/screenshots (needs: pip install playwright; playwright install chromium)."""
import os
from playwright.sync_api import sync_playwright
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
O=ROOT+'/docs/screenshots/'
def car(pg,tab,cid,sub):
    pg.evaluate(f"go('{tab}')");pg.wait_for_timeout(150)
    pg.evaluate(f"state.car='{cid}';state.sub='{sub}';drawList('{tab}');drawDetail()");pg.wait_for_timeout(400)
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1280,'height':860}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+ROOT+'/index.html');pg.wait_for_timeout(800)
    def shot(name,tab=None,full=False):
        if tab: pg.evaluate(f"go('{tab}')");pg.wait_for_timeout(300)
        pg.evaluate("window.scrollTo(0,0)");pg.screenshot(path=O+name,full_page=full)
    shot('01-home.png')
    shot('02-rolls-royce.png','rr'); shot('03-bentley.png','bentley'); shot('04-italian.png','italian')
    car(pg,'rr','rr1','story');pg.screenshot(path=O+'05-car-story.png')
    car(pg,'rr','rr1','specs');pg.screenshot(path=O+'06-car-specs.png')
    car(pg,'rr','rr1','photos');pg.screenshot(path=O+'07-car-photos.png')
    car(pg,'rr','rr1','fame');pg.screenshot(path=O+'08-car-famous-owners.png')
    car(pg,'italian','i1','market');pg.screenshot(path=O+'09-car-prices.png')
    for n,t in [('10-quiz','quiz'),('11-compare','compare'),('12-timeline','timeline'),('13-coachbuilders','builders'),('14-people','people'),('15-glossary','glossary'),('16-identify','identify'),('17-sources','sources')]:
        shot(n+'.png',t)
    pg.evaluate("go('home')");pg.wait_for_timeout(200)
    pg.fill('#sq','Zagato');pg.wait_for_timeout(500);pg.screenshot(path=O+'18-search.png')
    m=b.new_page(viewport={'width':390,'height':800},device_scale_factor=2)
    m.goto('file://'+ROOT+'/index.html');m.wait_for_timeout(800)
    m.screenshot(path=O+'19-mobile-home.png')
    m.evaluate("go('rr');state.car='rr1';state.sub='story';drawList('rr');drawDetail()");m.wait_for_timeout(400)
    m.screenshot(path=O+'20-mobile-car.png')
    print('errors',errs)
    b.close()
