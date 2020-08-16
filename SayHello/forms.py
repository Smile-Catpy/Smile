from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

'''表单模板'''


class HelloForm(FlaskForm):
    name = StringField('名字', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('留言', validators=[DataRequired(), Length(1, 300)])
    submit = SubmitField()
