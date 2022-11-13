from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Length


class PlayerPrefForm(FlaskForm):
    player_name  = StringField('Player Name', default='Player Name', validators=[DataRequired(), Length(min=2, max=20)])
    pref_defence = IntegerField('Defender', default=0, validators=[DataRequired()])
    pref_central = IntegerField('Central', default=0, validators=[DataRequired()])
    pref_winger  = IntegerField('Winger', default=0, validators=[DataRequired()])
    pref_forward = IntegerField('Forward', default=0, validators=[DataRequired()])


class TeamSelectionForm(FlaskForm):
    PlayerList = FieldList(FormField(PlayerPrefForm), min_entries=6)
    submit = SubmitField('Generate Formation')