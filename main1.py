from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from pyfiles.calorie import Calorie
from pyfiles.temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriePage(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template('calories_form_page.html', caloriesform=calorie_form)

    def post(self):
        calories_form = CalorieForm(request.form)

        temperatureO = Temperature(
            city=calories_form.city.data, country=calories_form.country.data).get()

        calorieO = Calorie(weight=float(calories_form.weight.data), age=float(calories_form.age.data),
                           height=float(calories_form.height.data), temperature=temperatureO)

        calories_x = calorieO.calculate()

        return render_template('calories_form_page.html', caloriesform=calories_form, calories=calories_x, result=True)


class CalorieForm(Form):
    weight = StringField(label="Weight: ", default="60")
    height = StringField(label="Height: ", default="170")
    age = StringField(label="Age: ", default="20")
    city = StringField(label="City: ", default="Minsk")
    country = StringField(label="Country: ", default="Belarus")
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriePage.as_view('calories_form_page'))
app.run(debug=True)
