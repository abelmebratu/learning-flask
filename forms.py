from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, DecimalField, HiddenField

class SignupForm(Form):
    total_gold = DecimalField("Total Gold")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Sign up")


class NinjaMoneyForm(Form):
    place = HiddenField("Place")
    submit = SubmitField("Find Gold!")



    