from flask import render_template, request
from app import app
from auto_pete.output import output_formation


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    player_name = request.form.get("player_name")
    pref_defence = request.form.get("pref_defence")

    formation = output_formation()

    return render_template("team_selection.html", player_name=player_name, pref_defence=pref_defence, formation=formation)


if __name__ == "__main__":
    app.run(debug=True)