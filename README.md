# Global Olympic Sports Performance Analysis

Tableau dashboards and story on Olympic medals, athletes, investment and regional efficiency (1992–2026), embedded in a Flask web app.

## Repository structure
```
app.py                  Flask app (routes: /, /dashboard, /story)
templates/, static/     Jinja pages and assets (Bootstrap via CDN)
requirements.txt
docs/
  1. Ideation Phase/            Brainstorm, problem statements, empathy map
  2. Requirement Analysis/      Requirements, DFD & user stories, tech stack, journey map
  3. Project Design Phase/      Problem-solution fit, proposal, solution architecture
  4. Project Planning Phase/    Backlog, sprints
  5. Project Development Phase/Tableau/   Business questions, dashboard, story
  6. Performance Testing/       Tableau performance test
  7. Project Documentation/     Final report
  8.Project Demonstration/      Communication, features, demo plan, scalability, team
```
The Snowflake templates in the original zip are not included because this project uses Tableau and flat CSVs.

## Run locally
```
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Set the Tableau Public URLs in `app.py` or with the environment variables `TABLEAU_DASHBOARD1_URL`, `TABLEAU_DASHBOARD2_URL`, `TABLEAU_STORY_URL`. Until then the pages show a placeholder and a preview image. The embed uses Tableau's JavaScript embedding script; confirm the script URL and `<tableau-viz>` attributes against the current Tableau Public embedding docs.

## Push to GitHub
```
git init
git add .
git commit -m "Initial commit: Olympic performance analysis"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

