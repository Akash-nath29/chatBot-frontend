from flask import Flask, render_template, request, redirect, session
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "Krw90{veookke]mn!34m" #Use Storng Secret Key for Production
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(100), nullable = True)
    message = db.Column(db.Text, nullable = False)
    
    def __init__(self, user, message):
        self.user = user
        self.message = message

@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

@app.route('/process', methods=['GET', 'POST'])
def process():
    # print(request.form.get('userQuery'))
    if request.method == 'POST':
        message = request.form.get('userQuery')
        user = session.get("name")
        newMessage = Message(user=user, message=message)
        db.session.add(newMessage)
        db.session.commit()
        # print(userQuery)
        
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)