from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class FeedForm(FlaskForm):
    name = StringField('RSS Feed Name', validators=[DataRequired()])
    link = StringField('RSS Feed Link', validators=[DataRequired()])
    article_1 = StringField('RSS Feed Tag 1', validators=[DataRequired()])
    article_2 = StringField('RSS Feed Tag 2')
    submit = SubmitField('Add Article')