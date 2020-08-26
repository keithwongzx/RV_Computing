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
        include_pw, include_mtl = request.form["include_pw"], request.form["include_mtl"]
        if include_pw == "yes":
            if include_mtl == "yes":
                return render_template("rp_calc_pw_mtl.html")
            else:
                return render_template("rp_calc_pw.html")
        else:
            if include_mtl == "yes":
                return render_template("rp_calc_mtl.html")
            else:
                return render_template("rp_calc_select.html")

if __name__ == "__main__":
    app.run(debug=True)