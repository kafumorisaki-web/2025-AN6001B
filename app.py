from flask import Flask,render_template,request
import joblib

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q=request.form.get("q")
    print(q)
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))


@app.route("/dbs_prediction",methods=["GET","POST"])
def dbs_prediction():
    q=float(request.form.get("q"))
    model=joblib.load("dbs.pkl")
    r=model.predict([[1.3]])
    return(render_template("dbs_prediction.html",r=r[0][0]))

@app.route("/credit",methods=["GET","POST"])
def credit():
    q=float(request.form.get("q"))
    model=joblib.load("german_credit.pkl")
    r=model.predict([[20]])
    return(render_template("credit.html",r=r[0][0]))

if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0', port=5000)
