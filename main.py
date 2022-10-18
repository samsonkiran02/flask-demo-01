from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("Index.html")

@app.route("/n=<name>+<by>")
def wish(name,by):
  return render_template("Index.html",name=name,by=by)

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=8600,debug=True)
  