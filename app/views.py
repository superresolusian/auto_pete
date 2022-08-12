from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    player_name = request.form.get("player_name")
    pref_defence = request.form.get("pref_defence")

    return render_template("team_selection.html", player_name=player_name, pref_defence=pref_defence)


if __name__ == "__main__":
    app.run(debug=True)