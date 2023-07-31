# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'Rit_u' and password == 'Ritubabu#1':   
        account_sid = 'AC5e7ffbc50c1078aca2d72e0fc7db8462'
        auth_token = 'a1f0c5f786e52a9b59d6ed46b85acf99'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VAad20b1420b7fa2f0f9dae928beccc1e3') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'AC5e7ffbc50c1078aca2d72e0fc7db8462'
    auth_token = 'a1f0c5f786e52a9b59d6ed46b85acf99'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('VAad20b1420b7fa2f0f9dae928beccc1e3') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')    # Write code here
    else:
        return redirect("https://collab-notepad.onrender.com/")


if __name__ == "__main__":
    app.run()

