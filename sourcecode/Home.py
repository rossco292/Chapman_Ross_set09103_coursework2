from flask import Flask, render_template, url_for
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/storm")
def weather():
    return render_template('storm.html')

@app.route("/hurricane")
def hurricane():
    return render_template('hurricane.html')

@app.route("/supercell")
def supercell():
    return render_template('supercell.html')

@app.route("/ice_storm")
def ice_storm():
    return render_template('ice_storm.html')


@app.errorhandler(404)
def page_not_found(error):
    return "The page was not found.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
