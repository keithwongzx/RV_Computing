from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/rp_calc/", methods=["GET", "POST"])
def rp_calc():
    if request.method == "GET":
        return render_template("rp_calc.html")
    else:
        include_mtl, include_pw = request.form["include_mtl"], request.form["include_pw"]
        return render_template("rp_calc_grades.html", include_mtl=include_mtl, include_pw=include_pw)


@app.route("/rp_display/", methods=["POST"])
def display():
    pass

if __name__ == "__main__":
    app.run(debug=True)