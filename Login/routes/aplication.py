from flask import Flask,render_template, request, redirect, url_for
##from flask_login import LoginManager

class User:
    def __init__(self,id,username,password,email,address,occupation,age,birth):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.occupation = occupation
        self.birth = birth
        self.age = age
    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id = 1, username='Alex', password='password',email='email@a',address='casa',occupation= 'gamer',age='23',birth='24-5-7'))
users.append(User(id = 2, username='Alan', password='secret',email='email@a',address='casa',occupation= 'gamer',age='23',birth='24-5-7'))

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():

    return render_template('login.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('nombre')
        password = request.form.get('contrasena')
        email = request.form.get('correo')
        address = request.form.get('direccion')
        occupation = request.form.get('ocupacion')
        age = request.form.get('edad')
        birth = request.form.get('fecha_nacimiento')
        
        users.append(User(id = len(users)+1, username=name, password=password,email=email,address=address,occupation= occupation,age=age, birth = birth))

    return render_template('profile.html',nombre=name, contrasena=password,correo=email,direccion=address,ocupacion= occupation,edad=age, fecha_nacimiento= birth)