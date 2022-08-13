from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class TeamSelectionForm(FlaskForm):
    player_name  = StringField('Player Name', validators=[DataRequired(), Length(min=2, max=20)])
    pref_defence = IntegerField('Defender', validators=[DataRequired()])
    pref_central = IntegerField('Central', validators=[DataRequired()])
    pref_winger  = IntegerField('Winger', validators=[DataRequired()])
    pref_forward = IntegerField('Forward', validators=[DataRequired()])
    submit       = SubmitField('Generate Formation')