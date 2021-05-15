from backend.credential_temp import Receiver
from flask import Flask,render_template,request
from flask import Flask, render_template
from backend import code
import datetime

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/subscribe', methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        fname = request.form.get("firstName")
        lname = request.form.get("lastName")
        pincd = request.form.get("pincode")
        email = request.form.get("email")
        date = request.form.get("date")
        date = date.split("-")
        date = "-".join([date[2],date[1],date[0]])

        # print(fname,lname,email,pincd,date)
        rcv = Receiver(fname,lname,email,pincd,date)
        code.subcription(rcv)

    return render_template('subscribe.html')

if __name__ == "__main__":
    app.run(debug=True)
