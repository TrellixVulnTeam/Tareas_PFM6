from flask import Flask,render_template, request
##from flask_login import LoginManager

class User:
    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password
    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id = 1, username='Alex', password='password'))
users.append(User(id = 2, username='Alan', password='secret'))

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')
