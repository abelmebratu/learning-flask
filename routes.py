from flask import Flask, render_template
#from models import db
from forms import SignupForm

app = Flask(__name__)

# app.config('SQLALCHEMY_DATABASE_URI') = 'postgresql://localhost/learningflask'
# db.init_app(app)

app.secret_key = "development"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup")
def signup():
    form = SignupForm()
    form.total_gold = calculate_total_gold()
    activities = get_activities()
    return render_template("signup.html", form=form, activities = activities)

def calculate_total_gold():
    #TODO: Implement method
    return 25
def get_activities():
    #TODO: Implement method
    activities = [
        {'amount':15,
        'place':'farm',
        'datetime':'2013/09/03 6:15pm'
        },
        {'amount':7,
        'place':'cave',
        'datetime':'2013/09/03 4:13pm'
        },
        {'amount':5,
        'place':'house',
        'datetime':'2013/09/03 4:05pm'
        },
        {'amount':-50,
        'place':'casino',
        'datetime':'2013/09/03 4:04pm'
        },
        {'amount':-30,
        'place':'casino',
        'datetime':'2013/09/03 4:03pm'
        }
    ]
    return activities
if __name__ == "__main__":
     app.run(debug=True)
