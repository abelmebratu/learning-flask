from flask import Flask, render_template, request, redirect, session
from forms import NinjaMoneyForm
import random
import json
from datetime import datetime
app = Flask(__name__)

app.secret_key = "development2.0"

@app.route("/")
def index():
    total_gold = calculate_total_gold()
    form_for_farm = NinjaMoneyForm(place="farm")
    form_for_cave = NinjaMoneyForm(place="cave")
    form_for_house = NinjaMoneyForm(place="house")
    form_for_casino = NinjaMoneyForm(place="casino")
    activities = load_activities_from_session()

    return render_template("ninjamoney.html", total_gold = total_gold, activities=activities, 
                            form_for_farm = form_for_farm, form_for_cave = form_for_cave, 
                            form_for_house = form_for_house, form_for_casino=form_for_casino)
      

@app.route("/process_money", methods=["GET", "POST"])
def process_money():
    if request.method == 'POST':
        place_visited = request.form['place']
        time_visited = datetime.now().strftime('%Y/%m/%d %I:%M %p')
        gold_found = calculate_gold(place_visited)

        current_activity = {'amount':gold_found, 'place':place_visited, 'datetime':time_visited}            

        activities = load_activities_from_session()
        activities.append(current_activity)
        session['activities'] = json.dumps(activities)

    return redirect("/")

def load_activities_from_session():
    gold_activity = []
    if session.get("activities") is not None:
        gold_activity = json.loads(session['activities'])
    return gold_activity

def calculate_gold(place_visited):
    if place_visited == 'farm':
        gold_found = random.randint(10,20)
    elif place_visited == 'cave':
        gold_found = random.randint(5,10)
    elif place_visited == 'house':
        gold_found = random.randint(2,5)
    elif place_visited == 'casino':
        gold_found = random.randint(-50,50)
    return gold_found

def calculate_total_gold():
    total_gold = 0
    activities = load_activities_from_session()
    for activity in activities:
        total_gold = total_gold + activity['amount']
    return total_gold


if __name__ == "__main__":
     app.run(debug=True)
