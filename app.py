"""Flask app embedding the published Tableau Public dashboards and story."""
import os
from flask import Flask, render_template

app = Flask(__name__)

# Replace these with your Tableau Public "Share" URLs (or set environment variables).
# Use the plain view URL, e.g. https://public.tableau.com/views/<workbook>/<sheet>
TABLEAU = {
    "dashboard1": os.getenv("TABLEAU_DASHBOARD1_URL", ""),
    "dashboard2": os.getenv("TABLEAU_DASHBOARD2_URL", ""),
    "story": os.getenv("TABLEAU_STORY_URL", ""),
}


@app.context_processor
def inject_urls():
    return {"tableau": TABLEAU}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/story")
def story():
    return render_template("story.html")


if __name__ == "__main__":
    app.run(debug=True)
