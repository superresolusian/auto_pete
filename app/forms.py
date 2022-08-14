from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Length


class PlayerPrefForm(FlaskForm):
    player_name  = StringField('Player Name', validators=[DataRequired(), Length(min=2, max=20)])
    pref_defence = IntegerField('Defender', validators=[DataRequired()])
    pref_central = IntegerField('Central', validators=[DataRequired()])
    pref_winger  = IntegerField('Winger', validators=[DataRequired()])
    pref_forward = IntegerField('Forward', validators=[DataRequired()])


class TeamSelectionForm(FlaskForm):
    PlayerList = FieldList(FormField(PlayerPrefForm), min_entries=2)
    submit = SubmitField('Generate Formation')