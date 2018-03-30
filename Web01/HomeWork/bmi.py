from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:weigth>/<int:height>')
def bmi(weigth, height):
    bmi = float((weigth/(float(height/100)))**2)
    if bmi < 16:
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi< 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

@app.route('/bmi1/<int:weigth>/<int:height>')
def bmi1(weigth, height):
    bmi = float((weigth/(float(height/10)))**2)
    return render_template("bmi.html", bmi = bmi)

if __name__ == '__main__':
    app.run(debug=True)
