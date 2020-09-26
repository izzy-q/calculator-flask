from flask import Flask, render_template, request
import calculator


app = Flask(__name__)


# home page
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


# results page
@app.route("/result/", methods=['GET', 'POST'])
def calc():
    func = request.form['func']
    variables = request.form['variables']
    return render_template("result.html", results=calculator.calc(func, variables))


app.run(debug=True)
