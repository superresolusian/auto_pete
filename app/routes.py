from flask import render_template, request
from app import app
from app.forms import RegistrationForm, TeamSelectionForm
from auto_pete.output import output_formation


@app.route("/", methods=['GET', 'POST'])
def home():
    form = TeamSelectionForm()
    if form.validate_on_submit():
        flash(f'Team selection submitted!', 'success')
        return redirect(url_for('home'))
    return render_template("index.html", form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/submit", methods=["POST"])
def generate_team_selection():
    player_name = request.form.get("player_name")
    pref_defence = request.form.get("pref_defence")

    formation = output_formation()

    return render_template("team_selection.html",
                           player_name=player_name, pref_defence=pref_defence, formation=formation)


if __name__ == "__main__":
    app.run(debug=True)