from flask import Flask,render_template,request
from flask import Flask, render_template


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
        age = request.form.get("age")

        print(fname,lname,email,age,pincd)

    return render_template('subscribe.html')

if __name__ == "__main__":
    app.run(debug=True)
