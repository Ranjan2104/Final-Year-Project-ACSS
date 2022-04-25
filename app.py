from flask import Flask, render_template, redirect, request
import os
import sqlite3
import cv2
import matplotlib.pyplot as plt
import numpy as np
from pytesseract import pytesseract
import app_ml


curr_loc = os.path.dirname(os.path.abspath(__file__))

myapp = Flask(__name__)

@myapp.route("/")
def homepage():
    return render_template("sign-in.html")

@myapp.route("/", methods = ["POST"])
def checklogin():
    UN = request.form['Username']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection(curr_loc + "\Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username, Password from Users WHERE Username = '{un}' AND Password = '{pw}'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) == 1:
        return render_template("index.html")
    
    else:
        return render_template("error.html")

@myapp.route("/register", methods = ["GET", "POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['DUsername']
        dPW = request.form['Dpassword']
        sqlconnection = sqlite3.Connection(curr_loc + "\Login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{u}', '{p}')".format(u = dUN, p = dPW)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("sign-up.html")


@myapp.route("/Cheque_form", methods = ["GET", "POST"])
def Cheque_data():
    if request.method == "POST":
        dN = request.form['fname']
        dA = request.form['Accno']
        dIF = request.form['IFSC']
        dAm = request.form['Amount']
        dB = request.form['BANK']
        sqlconnection = sqlite3.Connection(curr_loc + "\Cheque_data.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO information VALUES('{N}', '{A}', '{IF}', '{Am}', '{B}')".format(N = dN, A = dA, IF = dIF, Am = dAm, B = dB)
        cursor.execute(query1)
        sqlconnection.commit()
        app_ml.fun()
        return redirect("/thankyou")
    return render_template("Cheque.html")

@myapp.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@myapp.route("/about")
def about():
    return render_template("About.html")

@myapp.route("/Contact")
def contact():
    return render_template("Contact.html")

@myapp.route("/faq")
def faq():
    return render_template("faq.html")

@myapp.route("/ourpartner")
def ourpartner():
    return render_template("OurPartner.html")

@myapp.route("/sign-in")
def signin():
    return render_template("sign-in.html")

@myapp.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    myapp.run(debug=True)
