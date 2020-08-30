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
    sub_list = []
    for i in request.form:
        sub_list.append(i)
    data = request.form
    print(data)
    if "pw" in sub_list:
        include_pw = "yes"
    if "mt" in sub_list:
        include_mtl = "yes"
    if "pw" in sub_list:
        if "mt" in sub_list:
            return render_template("rp_display.html", include_pw=include_pw, include_mtl=include_mtl, data=data)
        else:
            return render_template("rp_display.html", include_pw=include_pw, include_mtl=include_mtl, data=data)
    else:
        if "mt" in sub_list:
            return render_template("rp_display.html", include_pw=include_pw, include_mtl=include_mtl, data=data)
        else:
            return render_template("rp_display.html", include_pw=include_pw, include_mtl=include_mtl, data=data)

if __name__ == "__main__":
    app.run(port=5003, debug=True)