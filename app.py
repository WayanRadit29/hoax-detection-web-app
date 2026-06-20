from flask import Flask, render_template, request
from prediction import predict_hoax

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    result = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("text", "")
        result = predict_hoax(input_text)

    return render_template(
        "prediction.html",
        result=result,
        input_text=input_text
    )


@app.route("/information")
def information():
    return render_template("information.html")


if __name__ == "__main__":
    app.run(debug=True)