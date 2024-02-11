from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DateRequired()])
    password = PasswordField('Password', validators=[DateRequired()])
    remember_me = Booleanield('Remember Me')
    submit = SubmitField('Sign In')
