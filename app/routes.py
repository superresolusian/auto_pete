from flask import render_template, request, redirect, flash, session, url_for
from wtforms import FieldList, FormField

from app import app
from app.forms import TeamSelectionForm, PlayerPrefForm
from auto_pete.output import output_formation


@app.route("/", methods=['GET', 'POST'])
def home():

    # initialise session parameters to control number of rows in displayed TeamSelectionForm
    session['num_players'] = 5
    session['num_subs'] = 0

    if request.method == 'GET':
        team_form = TeamSelectionForm()

        if team_form.is_submitted():
            flash(f'Team selection submitted!', 'success')
            app.logger.info("TeamSelectionForm submitted.")

        return render_template("index.html", form=team_form)


@app.route("/set_match_format", methods=['GET', 'POST'])
def set_match_format():

    # Retrieve number of players based on match format (5-a-side, 11-a-side, etc.)
    num_players = int(request.form['num_players'])
    session['num_players'] = num_players

    num_subs = session['num_subs']

    # TODO: remove -1 once goalkeeper added as position
    team_form = dynamically_update_form(num_players - 1 + num_subs)

    return render_template("index.html", form=team_form)


@app.route("/set_num_subs", methods=['GET', 'POST'])
def set_num_subs():

    # Retrieve number of subs input
    num_subs = int(request.form['num_subs'])
    session['num_subs'] = int(num_subs)

    num_players = session['num_players']

    # TODO: remove -1 once goalkeeper added as position
    team_form = dynamically_update_form(num_players - 1 + num_subs)

    return render_template("index.html", form=team_form)


@app.route("/team_selection", methods=['GET', 'POST'])
def optimise_team():

    app.logger.info(f'route: optimise_team()')
    app.logger.info(f'session["num_players"]: {session["num_players"]}')
    # TODO: reminder - ensure session['num_players'] consistent with num_players further in function
    app.logger.info(f'session["num_players"]: {session["num_subs"]}')

    # Retrieve team preference form inputs
    team_form = request.form

    # Convert form to lists
    player_name_submitted = [team_form[player] for player in team_form if "player_name" in player]
    pref_defence_submitted = [team_form[player] for player in team_form if "pref_defence" in player]
    pref_central_submitted = [team_form[player] for player in team_form if "pref_central" in player]
    pref_winger_submitted = [team_form[player] for player in team_form if "pref_winger" in player]
    pref_forward_submitted = [team_form[player] for player in team_form if "pref_forward" in player]

    # Pass list of lists to AUTO_PETE
    num_players = len(player_name_submitted)  # TODO: update once goalkeeper added as position
    team_preferences = []
    for n in range(num_players):
        team_preferences.append([
            player_name_submitted[n],
            pref_defence_submitted[n],
            pref_central_submitted[n],
            pref_winger_submitted[n],
            pref_forward_submitted[n]
        ])

    # Run auto_pete
    formation = output_formation(team_preferences)

    # Parse auto_pete formation for display
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


def dynamically_update_form(min_entries):
    """
    Dynamically update TeamSelectionForm

    **IMPORTANT**
    It is not possible to dynamically update min_entries in a FieldList.
    Workaround: https://stackoverflow.com/a/54958358/20867242

    :min_entries: number of player entries in TeamSelectionForm
    :return: new form object
    """

    # Subclass form
    class LocalForm(TeamSelectionForm):
        pass

    # Bind new field
    LocalForm.PlayerList = FieldList(FormField(PlayerPrefForm), min_entries=min_entries)

    # Use new form
    form = LocalForm()

    return form


if __name__ == "__main__":
    app.run(debug=True)
