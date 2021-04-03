from random import random
import math
import mysql
import requests
from flask import Flask, render_template, request, session, redirect, url_for
from mysql.connector import connect
 
app = Flask(__name__)
app.secret_key = 'ApnoKissan'
 
@app.route('/')
def home():
    if 'email' in session:
        return redirect('/homecustomer')
    if 'userphonenumber' in session:
        return redirect('/homefarmer')
    return render_template("index.html")
 
 
@app.route('/homefarmer')
def homeFarmer():
    if 'userphonenumber' in session:
        num = session['userphonenumber']
        connection = mysql.connector.connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                                             database="kissan")
        query = "select * from UserDetailsSignup where userphonenumber = '{}'".format(session['userphonenumber'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template("Homefarmer.html", nm=data[1])
    return render_template("loginask.html")
 
 
@app.route('/homecustomer')
def homeCustomer():
    if 'email' in session:
        emailid = session['email']
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "select * from CustomerDetailsSignup where useremail = '{}'".format(emailid)
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template("Homecustomer.html", nm=data[1])
    return render_template("loginask.html")
 
 
@app.route('/Loginask')
def LoginAsk():
    if 'email' in session:
        return redirect('/homecustomer')
    if 'userphonenumber' in session:
        return redirect('/homefarmer')
    return render_template("loginask.html")
 
 
@app.route('/Signupask')
def SignupAsk():
    if 'email' in session:
        return redirect('/homecustomer')
    if 'userphonenumber' in session:
        return redirect('/homefarmer')
    return render_template("signupask.html")
 
 
@app.route('/Login')
def login():
    if 'userphonenumber' in session:
        return redirect('/homefarmer')
    return render_template("login.html")
 
 
@app.route('/Signup')
def signup():
    if 'userphonenumber' in session:
        return redirect('/homefarmer')
 
    return render_template("signup.html")
 
 
@app.route('/Customerlogin')
def CustomerLogin():
    if 'email' in session:
        return redirect('/homecustomer')
    return render_template("customerlogin.html")
 
 
@app.route("/uphaar")
def Uphaar():
    if 'userphonenumber' in session:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "select * from UserDetailsSignup where userphonenumber = '{}'".format(session['userphonenumber'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template("uphaar.html", nm=data[1])
    return redirect('/Login')
 
 
@app.route('/Farmersell')
def FarmerSell():
    if 'userphonenumber' in session:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "select * from UserDetailsSignup where userphonenumber = '{}'".format(session['userphonenumber'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template('farmersell.html', nm=data[1])
    return redirect('/Login')
 
 
@app.route('/Customerprofile')
def CustomerProfile():
    if 'email' in session:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "select * from CustomerDetailsSignup where useremail = '{}'".format(session['email'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template('customerprofile.html', nm=data[1], ema=data[2], pho=data[4])
    elif 'userphonenumber' in session:
        return redirect('/Farmerprofile')
    else:
        return redirect('/Loginask')
 
 
@app.route('/Farmerprofile')
def FarmerProfile():
    if 'userphonenumber' in session:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "select * from UserDetailsSignup where userphonenumber = '{}'".format(session['userphonenumber'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template('customerprofile.html', nm=data[1], ema=data[2], pho=data[4])
    elif 'email' in session:
        return redirect('/Customerprofile')
    else:
        return redirect('/Loginask')
 
 
@app.route('/Customersignup')
def CustomerSignup():
    if 'email' in session:
        return redirect('/homecustomer')
    return render_template("customersignup.html")
 
@app.route('/Ordernow')
def Order():
    if 'userphonenumber' in session:
        return redirect('/farmerBuy')
    elif 'email' in session:
        return redirect('/customerBuy')
    else:
        return redirect('/Loginask')
 
@app.route('/farmerBuy')
def FarmerBuy():
    if 'userphonenumber' in session:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "select * from UserDetailsSignup where userphonenumber = '{}'".format(session['userphonenumber'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template("oldinstrument.html", nm=data[1])
    else:
        return redirect('/Loginask')
 
 
 
@app.route('/customerBuy')
def CustomerBuy():
    if 'email' in session:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "select * from CustomerDetailsSignup where useremail = '{}'".format(session['email'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template("customerbuy.html", nm=data[1])
    else:
        return redirect('/Loginask')
 
 
@app.route('/Checkout')
def CheckOut():
    if 'userphonenumber' in session:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                         host="mykissandatabase.mysql.database.azure.com", port=3306,
                         database="kissan")
        query = "select * from UserDetailsSignup where userphonenumber = '{}'".format(session['userphonenumber'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template("checkout.html", nm=data[1])
    elif 'email' in session: 
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                            host="mykissandatabase.mysql.database.azure.com", port=3306,
                            database="kissan")
        query = "select * from CustomerDetailsSignup where useremail = '{}'".format(session['email'])
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return render_template("checkout.html", nm=data[1])
    return render_template('/Loginask')
 
 
@app.route('/Checkotp')
def checkotp():
    otp = request.args.get("otp")
    if otp == otpf:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "insert into UserDetailsSignup (username,useremail,userpassword,userphonenumber) values('{}','{}','{}','{}')".format(
            nm,
            em, pas, pnum)
        cur = connection.cursor()
        cur.execute(query)
        connection.commit()
        session['userphonenumber'] = pnum
        return render_template("Homefarmer.html")
    else:
        return render_template('signup.html', error="Incorrect OTP Entered")
 
 
@app.route('/customerCheckotp')
def customercheckotp():
    otp = request.args.get("otp")
    if otp == otpc:
        connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                             host="mykissandatabase.mysql.database.azure.com", port=3306,
                             database="kissan")
        query = "insert into CustomerDetailsSignup (username,useremail,userpassword,userphonenumber) values('{}','{}','{}','{}')".format(
            namec, emailc, passwc, pnumberc)
        cur = connection.cursor()
        cur.execute(query)
        connection.commit()
        session['email'] = emailc
        return render_template("Homecustomer.html", nm=namec)
    else:
        return render_template('customersignup.html', error="Incorrect OTP Entered")
 
 
@app.route('/Checklogin')
def checklogin():
    if 'userphonenumber' in session:
        return redirect('/homefarmer')
    pnumbers = request.args.get('user_phone')
    passw = request.args.get('password')
    connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                         host="mykissandatabase.mysql.database.azure.com", port=3306, database="kissan"
                         )
    query1 = "select * from UserDetailsSignup where userphonenumber = '{}'".format(pnumbers)
    cur = connection.cursor()
    cur.execute(query1)
    data = cur.fetchone()
    if data == None:
        return render_template("login.html", error="Account doesn't exist ! SignUp 👇")
    else:
        if pnumbers == data[4] and passw == data[3]:
            session['userphonenumber'] = pnumbers
            return redirect('/homefarmer')
        else:
            return render_template("login.html", error="Incorrect Phone Number or Password")
 
@app.route('/Checksignup')
def checksignup():
    global nm, em, pas, pnum, otpf
    nm = request.args.get('username')
    em = request.args.get('email')
    pas = request.args.get('password')
    cpas = request.args.get('cpassword')
    pnum = request.args.get('number')
    if pas != cpas:
        return render_template("signup.html", error="  Passord and confirm password doesn't match !!")
    connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                         host="mykissandatabase.mysql.database.azure.com", port=3306,
                         database="kissan")
    query1 = "select * from UserDetailsSignup where userphonenumber = '{}'".format(pnum)
    cur1 = connection.cursor()
    cur1.execute(query1)
    data = cur1.fetchone()
    if(pnum==''):
        return render_template("signup.html",error="Field Required")
    if (data != None):
        return render_template("signup.html", error="Account already exists ! Login 👇")
    otpf = OTPassword()
    url = "https://www.fast2sms.com/dev/bulk"
    querystring = {"authorization": "2PZiMfQSWdGU3pDAstr95HcJzljenv8T60RgqumaBFbXyCKN4hPZgAWXiMsqJBoladpur9CjED5LU8SQ",
                   "sender_id": "FSTSMS", "language": "english", "route": "qt",
                   "numbers": pnum, "message": "43212",
                   "variables": "{BB}", "variables_values": otpf}
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template('CheckOpt.html')
 
 
@app.route('/ChecksignupCustomer')
def Checksignupcustomer():
    global namec, emailc, passwc, cpasswc, pnumberc, otpc
    namec = request.args.get('username')
    emailc = request.args.get('email')
    passwc = request.args.get('password')
    cpasswc = request.args.get('cpassword')
    pnumberc = request.args.get('number')
    if passwc != cpasswc:
        return render_template("customersignup.html", error="  Passord and confirm password doesn't match !!")
    connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                         host="mykissandatabase.mysql.database.azure.com", port=3306, database="kissan")
    query1 = "select * from CustomerDetailsSignup where userphonenumber = '{}'".format(pnumberc)
    cur1 = connection.cursor()
    cur1.execute(query1)
    data = cur1.fetchone()
    if data != None:
        return render_template("customersignup.html", error="Account already exists! Login 👇")
    otpc = OTPassword()
    url = "https://www.fast2sms.com/dev/bulk"
    querystring = {"authorization": "2PZiMfQSWdGU3pDAstr95HcJzljenv8T60RgqumaBFbXyCKN4hPZgAWXiMsqJBoladpur9CjED5LU8SQ",
                   "sender_id": "FSTSMS", "language": "english", "route": "qt",
                   "numbers": pnumberc, "message": "43212",
                   "variables": "{BB}", "variables_values": otpc}
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template('/CustomerCheckOpt.html')
 
 
@app.route('/CheckloginCustomer')
def checklogincustomer():
    if 'email' in session:
        return redirect('/homecustomer')
    email = request.args.get('user_email')
    passw = request.args.get('password')
    connection = connect(user="kissanadmin@mykissandatabase", password="Admin@123",
                         host="mykissandatabase.mysql.database.azure.com", port=3306, database="kissan")
    query1 = "select * from CustomerDetailsSignup where useremail = '{}'".format(email)
    cur = connection.cursor()
    cur.execute(query1)
    data = cur.fetchone()
    if (data == None):
        return render_template("customerlogin.html", error="Account doesn't exist ! SignUp 👇")
    else:
        if (email == data[2] and passw == data[3]):
            session['email'] = email
            session['cuserid'] = data[0]
            return redirect('/homecustomer')
        else:
            return render_template("customerlogin.html", error="Incorrect email address or Password")
 
 
def OTPassword():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random() * 10)]
    return OTP
 
 
@app.route('/customerlogout')
def CustomerLogout():
    session.pop('email', None)
    session.pop('cuserid', None)
    return render_template('loginask.html')
 
 
@app.route('/farmerlogout')
def FarmerLogout():
    session.pop('userphonenumber', None)
    session.pop('userid', None)
    return render_template('loginask.html')
 
 
if __name__ == "__main__":
    app.run()