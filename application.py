from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
app = application
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gudmundurmj:gudmundur@localhost/project_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Hhy999626@database-3.citzedvikw2a.us-east-1.rds.amazonaws.com/flaskaws'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password@contact.cdxlgoybrmsi.us-east-1.rds.amazonaws.com/flaskawl'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "somethingunique"

db = SQLAlchemy(app)

class Student(db.Model):
    auto_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    uni = db.Column(db.String(100), unique=True, nullable=False)
    contact_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    tele = db.Column(db.String(100), unique = True)

    def __init__(self, uni, contact_name, email, tele):
        self.uni = uni
        self.contact_name = contact_name
        self.email = email
        self.tele = tele

@app.route("/")
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add/', methods =['POST'])
def insert_book():
    if request.method == "POST":
        student = Student(
            uni = request.form.get('uni'),
            contact_name = request.form.get('contact_name'),
            email = request.form.get('email'),
            tele = request.form.get('tele'),
        )
        db.session.add(student)
        db.session.commit()
        flash("Student added successfully")
        return redirect(url_for('index'))


@app.route('/update/', methods = ['POST'])
def update():
    if request.method == "POST":
        my_data = Student.query.get(request.form.get('auto_id'))

        my_data.uni = request.form['uni']
        my_data.contact_name = request.form['contact_name']
        my_data.email = request.form['email']
        my_data.tele = request.form['tele']

        db.session.commit()
        flash("Student is updated")
        return redirect(url_for('index'))


@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(auto_id):
    my_data = Student.query.get(auto_id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Student is deleted")
    return redirect(url_for('index'))


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)
    #host='0.0.0.0'
