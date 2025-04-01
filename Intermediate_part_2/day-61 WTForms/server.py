from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey' # Required for CSRF protection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///submissions.db'
db = SQLAlchemy(app)



# ------------------------ db -----------------------------------
# Define a database model for form submissions
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Creating the database
with app.app_context():
    db.create_all()
# ------------------------------------wtf-------------------------
class Myform(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')








@app.route('/', methods=['GET', 'POST'])
def home():
    form = Myform()
    if form.validate_on_submit():
        submission = Submission(name=form.name.data, email=form.email.data)
        db.session.add(submission)
        db.session.commit()
        return redirect('success')
    return render_template('index.html' , form = form)

@app.route('/success')
def success():
    return 'Form submitted successfully'

@app.route('/history')
def history():
    submissions = Submission.query.all()  
    return render_template('history.html', submissions=submissions)

@app.route('/history/<name>')
def history_by_email(name):
    submissions = Submission.query.filter_by(name=name).all()  # Filter by email
    return render_template('history.html', submissions=submissions)



if __name__ =="__main__":
    app.run(debug=True)