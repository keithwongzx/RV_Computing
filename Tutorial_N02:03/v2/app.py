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
    if "pw" in sub_list:
        include_pw = "yes"
    if "mt" in sub_list:
        include_mtl = "yes"
    if "pw" in sub_list:
        if "mt" in sub_list:
            h2_1, h2_2, h2_3, h1, gp, pw, mt = request.form["h2_1"], request.form["h2_2"], request.form["h2_3"], request.form["h1"], \
                request.form["gp"], request.form["pw"], request.form["mt"]
            return render_template("rp_display", include_pw=include_pw, include_mtl=include_mtl, h2_1=h2_1, h2_2=h2_2, h2_3=h2_3, h1=h1, gp=gp, pw=pw, mt=mt)
        else:
            h2_1, h2_2, h2_3, h1, gp, pw = request.form["h2_1"], request.form["h2_2"], request.form["h2_3"], request.form["h1"], \
                request.form["gp"], request.form["pw"]
            return render_template("rp_display", include_pw=include_pw, include_mtl=include_mtl, h2_1=h2_1, h2_2=h2_2, h2_3=h2_3, h1=h1, gp=gp, pw=pw)
    else:
        if "mt" in sub_list:
            h2_1, h2_2, h2_3, h1, gp, mt = request.form["h2_1"], request.form["h2_2"], request.form["h2_3"], request.form["h1"], \
                request.form["gp"], request.form["mt"]
            return render_template("rp_display", include_pw=include_pw, include_mtl=include_mtl, h2_1=h2_1, h2_2=h2_2, h2_3=h2_3, h1=h1, gp=gp, mt=mt)
        else:
            h2_1, h2_2, h2_3, h1, gp = request.form["h2_1"], request.form["h2_2"], request.form["h2_3"], request.form["h1"], \
                request.form["gp"]
            return render_template("rp_display", include_pw=include_pw, include_mtl=include_mtl, h2_1=h2_1, h2_2=h2_2, h2_3=h2_3, h1=h1, gp=gp)

if __name__ == "__main__":
    app.run(port=5002, debug=True)