from flask import render_template, request, redirect, flash, session, url_for

from app import app
from app.forms import TeamSelectionForm
from auto_pete.output import output_formation


@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        form = TeamSelectionForm()

        if form.is_submitted():
            flash(f'Team selection submitted!', 'success')
            app.logger.info("TeamSelectionForm submitted.")

        return render_template("index.html", form=form)


@app.route("/set_match_format", methods=['GET', 'POST'])
def set_match_format():

    # Retrieve number of players based on match format (5-a-side, 11-a-side, etc.)
    num_players = request.form['num_players']
    session['num_players'] = int(num_players)

    return redirect(url_for('home'))
    # return redirect(request.referrer)  # effectively: return redirect(url_for('home'))


@app.route("/set_num_subs", methods=['GET', 'POST'])
def set_num_subs():

    # Retrieve number of subs input
    num_subs = request.form['num_subs']
    session['num_subs'] = int(num_subs)

    return redirect(url_for('home'))
    # return redirect(request.referrer)  # effectively: return redirect(url_for('home'))


@app.route("/team_selection", methods=['GET', 'POST'])
def optimise_team():

    # initialise if match format or number of subs not specified
    if not session['num_players']:
        session['num_players'] = 7
    if not session['num_subs']:
        session['num_subs'] = 3

    app.logger.info('route: optimise_team')
    app.logger.info(f'num_players: {session["num_players"]}')
    app.logger.info(f'num_subs: {session["num_subs"]}')

    # Retrieve team preference form inputs
    team_form = request.form

    # Convert form to lists
    player_name_submitted = [team_form[player] for player in team_form if "player_name" in player]
    pref_defence_submitted = [team_form[player] for player in team_form if "pref_defence" in player]
    pref_central_submitted = [team_form[player] for player in team_form if "pref_central" in player]
    pref_winger_submitted = [team_form[player] for player in team_form if "pref_winger" in player]
    pref_forward_submitted = [team_form[player] for player in team_form if "pref_forward" in player]

    # Pass list of lists to AUTO_PETE
    num_players = len(player_name_submitted)
    team_preferences = []
    for n in range(num_players):
        team_preferences.append([
            player_name_submitted[n],
            pref_defence_submitted[n],
            pref_central_submitted[n],
            pref_winger_submitted[n],
            pref_forward_submitted[n]
        ])

    # Run AUTO_PETE
    formation = output_formation(team_preferences)

    # Parse AUTO_PETE formation for display
    defenders = formation['D']
    central   = formation['C']
    wingers   = formation['W']
    forwards  = formation['F']
    subs      = formation['S']

    return render_template("team_selection.html",
                           formation=formation,
                           defenders=defenders,
                           central=central,
                           wingers=wingers,
                           forwards=forwards,
                           subs=subs
                           )


if __name__ == "__main__":
    app.run(debug=True)
