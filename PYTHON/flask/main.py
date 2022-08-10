from flask import Flask,render_template,request, template_rendered
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
local_server=True
with open('config.json','r') as f:
    params = json.load(f)["params"]

app = Flask(__name__)
app.config.update(
    MAIL_SERVER =  'smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD= params['gmail_password']
)
mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['production_uri']

db = SQLAlchemy(app)

class Contacts(db.Model):
    '''sno , name, email, phone_no, msg, date '''
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(20),nullable=False)
    phone_no = db.Column(db.String(20),nullable=False)
    msg = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(12),nullable=True)
@app.route("/")
def home():
    posts= Posts.query.filter_by().all()[0:params['no_post']]
    return render_template('index.html',params=params,posts=posts)
@app.route("/content")
def content():
    return render_template('content.html',params=params)
    
@app.route("/about")
def about():
    return render_template('about.html',params=params)

@app.route("/login")
def dashboard():
    return render_template('login.html',params=params)
@app.route("/contact", methods = ["GET","POST"])
def contacts():
    if(request.method == 'POST'):
        '''add entry to the database'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message') 
        '''sno , name, email, phone_no, msg, date '''
        entry = Contacts(name=name,phone_no=phone,email=email,msg=message,date = datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message("New message from "+ name,
        sender=email,
        recipients =[params['gmail_user']],
        body= message+ "\n"+phone
        )
    return render_template('contact.html',params=params)

class Posts(db.Model):
    '''sno , name, email, phone_no, msg, date '''
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    sub_heading = db.Column(db.String(80),nullable=False)
    slug = db.Column(db.String(30),nullable=False)
    content = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(12),nullable=True)
    img_file = db.Column(db.String(20),nullable=True)

@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post=Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html',params=params,post=post)

app.run(debug=True)