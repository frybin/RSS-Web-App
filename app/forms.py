from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class AddFeedForm(FlaskForm):
    name = StringField('RSS Feed Name', validators=[DataRequired()])
    link = StringField('RSS Feed Link', validators=[DataRequired()])
    article_1 = StringField('RSS Feed Tag 1', validators=[DataRequired()])
    article_2 = StringField('RSS Feed Tag 2')
    submit = SubmitField('Add Article')

class EditFeedForm(FlaskForm):
    name = StringField('RSS Feed Name', validators=[DataRequired()])
    link = StringField('RSS Feed Link', validators=[DataRequired()])
    article_1 = StringField('RSS Feed Tag 1', validators=[DataRequired()])
    article_2 = StringField('RSS Feed Tag 2')
    submit = SubmitField('Edit Article')