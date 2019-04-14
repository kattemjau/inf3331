#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import render_template
from temperature_CO2_plotter import plot_CO2 as CO2
from temperature_CO2_plotter import plot_temperature as tmp

app=Flask("name")

@app.route('/login', methods=['POST'])
def login():
    return render_template('noe.html')

@app.route('/handle_login', methods=['POST'])
def handle_login():


    assert request.method == 'POST'   # Check that we are really in a POST request
    # Acces the form data:
    month_val = request.form["Month"]
    yfrom = request.form["Year From"]
    yto = request.form["Year to"]
    m = request.form["Min"]
    ma = request.form["Max"]


    if month_val != "":
        month_val = int(month_val)
        if month_val > 12 or month_val < 0:
            month_val = 1
    else:
        month_val=1

    if yfrom == "":
        yfrom = 1800
    else :
        yfrom = int(yfrom)

    if yto == "":
        yto = 2050
    else :
        yto = int(yto)

    if m == "":
        m = 0
    else:
        m= int(m)
    if ma =="":
        ma=0
    else:
        ma=int(ma)
    # print(month)
    # print(yfrom)
    # print(yto)
    # print(m)
    # print(ma)
    tmp(month_val, yfrom, yto, m, ma)
    CO2(yfrom, yto, m, ma)

    return render_template("bilder.html")


@app.route('/')
def default():
    # tmp(10, 1970, 2011)
    # CO2(1, 1970, 2011)
    # month = request.form["month"]
    # Yfrom = request.form["from"]
    # Yto = request.form["to"]
    # m = request.form["min"]
    # ma = request.form["max"]

    # tmp(month, Yfrom, Yto, m, ma)
    # CO2(month, Yfrom, Yto, m, ma)

    return render_template("frontend.html")

@app.route('/help', methods=['POST'])
def helpme():
    return render_template("temperature_CO2_plotter.html")


app.run()
