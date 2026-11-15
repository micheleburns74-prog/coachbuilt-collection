# The Coachbuilt Collection

An interactive history of coachbuilt **Rolls-Royce, Bentley and Italian** cars and the craftsmen who bodied them: Barker, Hooper, H.J. Mulliner, Touring, Zagato, Pininfarina, Scaglietti and others.

It is a single self-contained web page. Open `index.html` in any browser and it works, with no install, no build step and no server.

![Home page](docs/screenshots/01-home.png)

## What is inside

- **23 cars** across three marques (13 Rolls-Royce, 4 Bentley, 6 Italian), each with its own colour theme and a full page of its own.
- **Quiz** with 51 built-in questions, filterable by topic.
- **Compare** two cars side by side, plus a Glossary, Prices guide, Timeline, Coachbuilders, People and Sources section.
- **Search** across cars, people, coachbuilders and glossary terms.
- **Identify a Car** (photo in, best-guess answer out) and a **News** tab.
- Responsive layout that works on a phone as well as a desktop.

## Screenshots

### The three marques

Each marque has its own palette and a list of cars grouped by decade.

| Rolls-Royce | Bentley | Italian |
|---|---|---|
| ![Rolls-Royce](docs/screenshots/02-rolls-royce.png) | ![Bentley](docs/screenshots/03-bentley.png) | ![Italian](docs/screenshots/04-italian.png) |

### A page for every car

Every car has eight sub-tabs: Story, Specs, Cost and Value, Photos, Owners and Racing, Famous Owners and Scandal, Prices and For Sale, and Why It Ended. Each car also has its own landing-page links.

![Car story](docs/screenshots/05-car-story.png)

| Specs | Photos |
|---|---|
| ![Specs](docs/screenshots/06-car-specs.png) | ![Photos](docs/screenshots/07-car-photos.png) |

| Famous owners and scandal | Prices and for sale |
|---|---|
| ![Famous owners](docs/screenshots/08-car-famous-owners.png) | ![Prices](docs/screenshots/09-car-prices.png) |

### Learn and explore

| Quiz | Compare |
|---|---|
| ![Quiz](docs/screenshots/10-quiz.png) | ![Compare](docs/screenshots/11-compare.png) |

| Timeline | Coachbuilders |
|---|---|
| ![Timeline](docs/screenshots/12-timeline.png) | ![Coachbuilders](docs/screenshots/13-coachbuilders.png) |

| People | Glossary |
|---|---|
| ![People](docs/screenshots/14-people.png) | ![Glossary](docs/screenshots/15-glossary.png) |

### Search, identify and sources

| Site-wide search | Identify a Car | Sources |
|---|---|---|
| ![Search](docs/screenshots/18-search.png) | ![Identify](docs/screenshots/16-identify.png) | ![Sources](docs/screenshots/17-sources.png) |

### On a phone

| Home | Car page |
|---|---|
| ![Mobile home](docs/screenshots/19-mobile-home.png) | ![Mobile car](docs/screenshots/20-mobile-car.png) |

## Languages and technologies

Everything in the page is written by hand with no frameworks and no libraries.

| Language | Used for | Where |
|---|---|---|
| **HTML5** | Page structure, tabs, forms, inline SVG background art | `index.html` |
| **CSS3** | Layout (flexbox and grid), per-marque colour themes using CSS variables, responsive phone layout | inside `index.html` |
| **JavaScript** (vanilla, ES2020, no libraries) | All behaviour: navigation and Back button, car pages, search, quiz, compare, timeline, photo handling, input escaping and safe-link checks | inside `index.html` |
| **Python 3** (test tooling only) | Automated smoke test and screenshot generator, using Playwright | `tests/`, `tools/` |
| **Markdown** | This documentation | `README.md` |

Other facts:

- The page is one file of roughly 2.8 MB. About 90 photos are embedded as base64 images, so it works offline.
- The page has a strict Content Security Policy: no remote scripts, fonts, images or frames. External links open in a new tab and only `https` links are allowed.
- No cookies and no tracking.

## Run it

Open `index.html` in a browser. That is all.

## Test it

```bash
pip install playwright
playwright install chromium
python tests/smoke_test.py
```

The smoke test opens every tab at desktop and phone width, checks for JavaScript errors, empty pages and sideways scrolling, and tests the search box. To regenerate the screenshots in this README run `python tools/make_screenshots.py`.

## Notes on live features

The **Identify a Car** tab, the **News** tab, the automatic quiz updates and the **Update questions** button need the Claude artifact runtime that hosts the live version of this page. In a plain copy opened from disk those parts show an offline message or stay hidden, and everything else works normally.

## Project layout

```
index.html                  the whole app (HTML, CSS and JavaScript)
docs/screenshots/           images used in this README
tests/smoke_test.py         Python + Playwright smoke test
tools/make_screenshots.py   regenerates the screenshots
```

## Photo credits and rights

Car photos come from Wikimedia Commons and are used under their Creative Commons or public-domain licences. Each photo carries its author and licence in the page's photo credits and in the Sources tab. Brand logos are intentionally not used, and the background outlines are generic body styles rather than specific cars.

Figures and prices come from public sources and are rounded; check auction results before quoting any value.

The code and written content are (c) 2026 Michele Burns. All rights reserved. The photos remain under their original licences.

Created by Michele Burns.
