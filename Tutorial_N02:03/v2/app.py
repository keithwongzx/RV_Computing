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
    grade_list = []
    rp_list = []
    data = []
    for i in request.form:
        sub_list.append(i)
        grade_list.append(request.form[i])
        if i == "General Paper" or i == "Project Work" or i == "Mother Tongue" or i == "H1 Subject":
            if request.form[i] == "A":
                rp_list.append("10.00")
            elif request.form[i] == "B":
                rp_list.append("8.75")
            elif request.form[i] == "C":
                rp_list.append("7.50")
            elif request.form[i] == "D":
                rp_list.append("6.25")
            elif request.form[i] == "E":
                rp_list.append("5.00")
            elif request.form[i] == "S":
                rp_list.append("2.50")
            elif request.form[i] == "U":
                rp_list.append("0.00")
        else:
            if request.form[i] == "A":
                rp_list.append("20.00")
            elif request.form[i] == "B":
                rp_list.append("17.50")
            elif request.form[i] == "C":
                rp_list.append("15.00")
            elif request.form[i] == "D":
                rp_list.append("12.50")
            elif request.form[i] == "E":
                rp_list.append("10.00")
            elif request.form[i] == "S":
                rp_list.append("5.00")
            elif request.form[i] == "U":
                rp_list.append("0.00")
    print(sub_list)
    print(grade_list)
    print(rp_list)
    for i in range(len(sub_list)):
        temp = []
        temp.append(sub_list[i])
        temp.append(grade_list[i])
        temp.append(rp_list[i])
        data.append(temp)
    print(data)
    include_pw = ""
    include_mtl = ""
    if "Project Work" in sub_list:
        include_pw = "yes"
    if "Mother Tongue" in sub_list:
        include_mtl = "yes"
    total_rp = 0.00
    total_rp_mtl = 0.00
    if include_pw == "yes":
        if include_mtl == "yes":
            for i in range(len(rp_list)):
                total_rp_mtl += float(rp_list[i])
            for i in range(len(rp_list) -1):
                total_rp += float(rp_list[i])
            total_rp_mtl = (total_rp_mtl / 100.00) * 90.00
            if total_rp_mtl > total_rp:
                total_rp = total_rp_mtl
            if len(str(total_rp)) == 4:
                total_rp = str(total_rp) + "0 / 90.00"
            else:
                total_rp = str(total_rp) + " / 90.00"
        else:
            for i in range(len(rp_list)):
                total_rp += float(rp_list[i])
            total_rp = str(total_rp)
            if len(total_rp) == 4:
                total_rp = total_rp + "0 / 90.00"
            else:
                total_rp = total_rp + " / 90.00"
    else:
        if include_mtl == "yes":
            for i in range(len(rp_list)):
                total_rp_mtl += float(rp_list[i])
            for i in range(len(rp_list) -1):
                total_rp += float(rp_list[i])
            total_rp_mtl = (total_rp_mtl / 90.00) * 80.00
            if total_rp_mtl > total_rp:
                total_rp = total_rp_mtl
            if len(str(total_rp)) == 4:
                total_rp = str(total_rp) + "0 / 80.00"
            else:
                total_rp = str(total_rp) + " / 80.00"
        else:
            for i in range(len(rp_list)):
                total_rp += float(rp_list[i])
            total_rp = str(total_rp)
            if len(total_rp) == 4:
                total_rp = total_rp + "0 / 80.00"
            else:
                total_rp = total_rp + " / 80.00"
    return render_template("rp_display.html", include_pw=include_pw, include_mtl=include_mtl, data=data, total_rp=total_rp)

if __name__ == "__main__":
    app.run(port=5005, debug=True)