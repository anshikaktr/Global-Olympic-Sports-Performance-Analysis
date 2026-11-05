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

## Run locally
```
cd tableau_flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Pages
- `/` home with project summary
- `/dashboards` Dashboard 1 and Dashboard 2 (interactive, filters work inside the embed)
- `/story` Tableau story (6 scenes)

## Push to GitHub
```
git init
git add .
git commit -m "Initial commit: Olympic performance analysis"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

