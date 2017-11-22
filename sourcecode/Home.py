from flask import Flask, render_template, url_for#These are the items needed for loading static and template files
app = Flask(__name__)#This intilises the site

@app.route("/")#This is the home route
def home():
    return render_template('home.html')

@app.route("/storm")#This is the storm page route
def weather():
    return render_template('storm.html')

@app.route("/hurricane")#This is the hurricane page route
def hurricane():
    return render_template('hurricane.html')

@app.route("/supercell")#This is the supercell page route
def supercell():
    return render_template('supercell.html')

@app.route("/ice_storm")#This is the icestorm page route
def ice_storm():
    return render_template('ice_storm.html')


@app.errorhandler(404)#This throws a meaningfull error if the page is not found
def page_not_found(error):
    return "The page was not found.", 404

if __name__ == "__main__":#This runs the page
  app.run(host='0.0.0.0', debug=True)
