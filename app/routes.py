from flask import render_template, request, flash
from app import app
from app.forms import TeamSelectionForm
from auto_pete.output import output_formation
import logging


@app.route("/", methods=['GET', 'POST'])
def home():
    form = TeamSelectionForm()

    if form.is_submitted():
        flash(f'Team selection submitted!', 'success')
        app.logger.info("TeamSelectionForm submitted.")

        player_formation_prefs = form.PlayerList.data

        # TODO: Run AUTO_PETE, e.g.:
        #
        # formation = run_auto_pete(player_formation_prefs)
        # INPUT: form.PlayerList.data – need to convert/format this so compatible with auto_pete code
        # OUTPUT: formation – formatted so can render on team_selection.html

        # For now:
        # create dummy values so I can create HTML page formatting

        # for field in form.PlayerList:
        #     print(field.player_name.data)
        #     print(field.pref_defence.data)
        #
        # for value in form.PlayerList.data:
        #     print(value)

        formation = output_formation()
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
                               subs=subs)

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
