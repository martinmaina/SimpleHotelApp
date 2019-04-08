from flask import Flask, request, flash, render_template, session
import sqlite3
from models import models as mm
app = Flask(__name__)


app.secret_key = b'What-cat-be-kept-here-*******//********\\**'

database = sqlite3.connect('message.db')

@app.route('/index')
def index():
    return render_template('index.html', title="Mukawa Wa Maina | karibu" )

@app.route('/about')
def about():
    return render_template('about.html', title="Mukawa Wa Maina | menya maingi")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Mukawa Wa Maina | araniria naithui")



@app.route('/message', methods=['GET', 'POST'])
def message_us():
    messa = None
    if request.method == 'POST':
        try:
                mm.addVerse(request.form['name'], request.form['email'], request.form['message'])
                messa = 'Thank you for your feedback ' + request.form['name'].capitalize()+'.'
        except sqlite3.IntegrityError:
                pass
        

    return render_template('contact.html', messa=messa)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)

