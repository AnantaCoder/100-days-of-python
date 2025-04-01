from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'secretkey'
db = SQLAlchemy(app)




# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'anirbansarkar.slg18@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'tkrf jtuw rmei fryy'  # App-specific password
app.config['MAIL_DEFAULT_SENDER'] = ('Admin', 'anirbansarkar.slg18@gmail.com')

mail = Mail(app)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(10000))

    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message

# Creating the database
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Check if the user email already exists
        if User.query.filter_by(email=email).first():
            flash("Email already taken", "danger")
            return render_template('index.html')
        else:
            new_user = User(name, email, phone, message)
            db.session.add(new_user)
            db.session.commit()
            flash("User created successfully!", "success")
            
            send_email(email,name,message)
            return redirect('/')  # Redirect to the home or another page

    return render_template('index.html')

def send_email(user_email,name,message):
    subject = "User Query Form"
    body = f"Hello Admin,\n\nYou have received a new message from {name}.\n\nMessage:\n{message}\n\nReply to {user_email}."
    
    msg = Message(subject=subject,recipients=['anirbansarkar.slg18@gmail.com'])
    msg.body = body
    msg.reply_to = user_email
    mail.send(msg)




if __name__ == '__main__':
    app.run(debug=True)

# tkrf jtuw rmei fryy