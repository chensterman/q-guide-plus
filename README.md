# QGuide+

QGuide+ is a search app for Harvard course evaluations. The live site is [https://q-guide-plus.vercel.app](https://q-guide-plus.vercel.app). The About page and the term list cover evaluations through 2023 Spring.

The frontend is a Vue 2 and Vuetify app in `app/`. Search requests go to a Vercel serverless function, which reads courses from MongoDB.

## Layout

| Path | Role |
| --- | --- |
| `app/` | Vue app and Vercel serverless API |
| `app/api/query.js` | `GET /api/query` |
| `app/api/db.js` | MongoDB connection (`DB_URI`) |
| `python/qscrape.py` | Scrapes Q reports into a CSV |
| `python/dbinsert.py` | Loads a CSV into MongoDB |
| `python/departments.py` | Prints the unique departments in a CSV |

## Frontend

From `app/`:

```bash
npm install
npm run serve
npm run build
```

`npm run serve` starts the Vue dev server. The client always requests `https://q-guide-plus.vercel.app/api/query`, including during local development, so search uses the production database. The dev-server proxy in `app/vue.config.js` targets `http://localhost:5000`. This repo does not include a process on that port.

## Environment

Create a `.env` file in the repo root. That file is gitignored.

| Variable | Used by |
| --- | --- |
| `DB_URI` | `app/api/db.js` and `python/dbinsert.py` |
| `USER_LOGIN` | `python/qscrape.py` (Harvard email) |
| `USER_PASSWORD` | `python/qscrape.py` |

`python/dbinsert.py` writes to the `test` database and the `courses` collection. `DB_URI` must also be set in the Vercel project environment for the live API.

## Data scripts

The Python scripts import `pymongo`, `python-dotenv`, `beautifulsoup4`, `selenium`, and `flair`. There is no `requirements.txt`. `python/qscrape.py` also expects Chrome and a ChromeDriver binary at `/usr/local/bin/chromedriver`.

Each script hardcodes its CSV path. `python/qscrape.py` writes `spring2023.csv`. `python/dbinsert.py` and `python/departments.py` read that same file.

## Deploy

Production is the Vercel project at [https://q-guide-plus.vercel.app](https://q-guide-plus.vercel.app). The Vue app and `app/api` are deployed together. This repo has no `vercel.json`. Project settings live in Vercel.

## Current behavior

Search returns the full course collection. Filters from the query page are not applied.

`app/api/query.js` stores operators as numeric object keys. `Object.entries` yields those keys as strings, and the handler compares them with numeric `===` checks, so no text filter is added and the MongoDB query stays empty. Range filters arrive as names like `courseRating.overall.min`. The handler splits only on the first dot, so those fields never match the filter map.

Recommendability, workload, comment sentiment, instructor feedback, and timeliness appear in the query page and are written by `python/dbinsert.py`. They are absent from the API filter map. The Mongoose model in `app/api/models/course.js` also omits `courseEval` and those extra instructor-rating fields.
