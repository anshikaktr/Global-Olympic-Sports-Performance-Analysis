from flask import Flask, render_template

app = Flask(__name__)

# Published Tableau Public workbook (same workbook for all three views)
WORKBOOK = "GlobalOlympicSportsPerformanceAnalysis_17932858582970"
VIEWS = {
    "dashboard1": f"{WORKBOOK}/Dashboard1",   
    "dashboard2": f"{WORKBOOK}/Dashboard2",   
    "story": f"{WORKBOOK}/Story1",
}
STATIC = {k: f"Gl/{v}/1.png" for k, v in VIEWS.items()}

STATS = [
    ("19", "Olympic Games (1992-2026)"),
    ("218", "National Olympic Committees"),
    ("11,106", "Medals awarded"),
    ("80,435", "Athletes in the data"),
]


@app.route("/")
def index():
    return render_template("index.html", stats=STATS)


@app.route("/dashboards")
def dashboards():
    return render_template("dashboard.html", views=VIEWS, static=STATIC)


@app.route("/story")
def story():
    return render_template("story.html", views=VIEWS, static=STATIC)


if __name__ == "__main__":
    app.run(debug=True)
