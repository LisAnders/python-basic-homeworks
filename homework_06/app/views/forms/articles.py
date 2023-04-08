from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class ArticleForm(FlaskForm):
    code = StringField(
        label="Код товара",
        validators=[DataRequired(), Length(min=1, max=20)],
        render_kw={"placeholder": "Код товара"},
    )
    name = StringField(
        label="Наименование товара",
        validators=[DataRequired(), Length(min=3)],
        render_kw={"placeholder": "Наименование товара"},
    )
    status = BooleanField(
        label="Активно", 
    )