from flask import render_template, request, flash

from app import app
from app.forms import TeamSelectionForm
from auto_pete.output import output_formation


@app.route("/", methods=['GET', 'POST'])
def home():
    form = TeamSelectionForm()

    if form.is_submitted():
        flash(f'Team selection submitted!', 'success')
        app.logger.info("TeamSelectionForm submitted.")

    #     player_formation_prefs = form.PlayerList.data
    #
    #     # TODO: remove these comments once shifted AUTO_PETE code to optimise_team():
    #     #
    #     # OLD COMMENTS ON HOW TO RUN AUTO_PETE (superseded by optimise_team() )
    #
    #     # formation = run_auto_pete(player_formation_prefs)
    #     # INPUT: form.PlayerList.data – need to convert/format this so compatible with auto_pete code
    #     # OUTPUT: formation – formatted so can render on team_selection.html
    #
    #     # For now:
    #     # create dummy values so I can create HTML page formatting
    #
    #     # for field in form.PlayerList:
    #     #     print(field.player_name.data)
    #     #     print(field.pref_defence.data)
    #     #
    #     # for value in form.PlayerList.data:
    #     #     print(value)
    #
    #     formation = output_formation()
    #     defenders = formation['D']
    #     central   = formation['C']
    #     wingers   = formation['W']
    #     forwards  = formation['F']
    #     subs      = formation['S']
    #
    #     return render_template("team_selection.html",
    #                            formation=formation,
    #                            defenders=defenders,
    #                            central=central,
    #                            wingers=wingers,
    #                            forwards=forwards,
    #                            subs=subs)

    return render_template("index.html", form=form)


@app.route("/team_selection", methods=['GET', 'POST'])
def optimise_team():

    team_form = request.form

    # Create dictionaries to pass to HTML using dictionary comprehension
    # Syntax: {player: team_form[player] ... }
    # Gives key: value pairs
    player_name_submitted = {player: team_form[player] for player in team_form if "player_name" in player}
    pref_defence_submitted = {player: team_form[player] for player in team_form if "pref_defence" in player}
    pref_central_submitted = {player: team_form[player] for player in team_form if "pref_central" in player}
    pref_winger_submitted = {player: team_form[player] for player in team_form if "pref_winger" in player}
    pref_forward_submitted = {player: team_form[player] for player in team_form if "pref_forward" in player}

    # TODO: change above to send results from AUTO_PETE to team_selection.html
    #  - current test code simply sends form field inputs
    #  - I think: send team_form to AUTO_PETE, return results from output_formation() and pass to team_selection.html

    return render_template("team_selection.html",
                           player_name_submitted=player_name_submitted,
                           pref_defence_submitted=pref_defence_submitted,
                           pref_central_submitted=pref_central_submitted,
                           pref_winger_submitted=pref_winger_submitted,
                           pref_forward_submitted=pref_forward_submitted
                           )


if __name__ == "__main__":
    app.run(debug=True)
