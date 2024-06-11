from flask import Flask, render_template, request
import backend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("predict.html")

    if request.method == "POST":
        day = request.form.get('textbox')
        day = int(day)
        output = backend.days_feet(day)

        return render_template("predict.html",output = output,user_text = day)

if __name__ == "__main__":
    app.run(port=5001,debug=True)