from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi():
    bmi = None

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi = round(weight / (height ** 2), 2)

    return render_template("index.html", bmi=bmi)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
