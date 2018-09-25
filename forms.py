from flask_wtf import Form
from wtforms import SubmitField, HiddenField

class NinjaMoneyForm(Form):
    place = HiddenField("Place")
    submit = SubmitField("Find Gold!")



    