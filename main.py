from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route ("/")
def index():
    print ("bloger mellstroy")
    return render_template("index.html")




app.run()