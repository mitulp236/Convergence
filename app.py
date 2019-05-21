import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, render_template, jsonify, redirect, session, url_for
import sqlalchemy
import random, re
import string
import pymysql
from functools import wraps
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import asc, desc
from datetime import datetime

app = Flask(__name__)
app.secret_key = "jhsldfsakdfh23kjnk23h1j23g12kj3b12"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/convergence'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# password from admin to check campaigner's password
display_password = "123@abc"


class Colleges(db.Model):
    sr_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    college = db.Column(db.String(500), nullable=False)

    def __init__(self, sr_no, college):
        self.sr_no = sr_no
        self.college = college

    def __repr__(self):
        return '<User %r>' % self.sr_no


class Users(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EMAIL = db.Column(db.String(80), unique=True, nullable=False)
    PASSWORD = db.Column(db.String(120), nullable=False)
    PRIVILEGE = db.Column(db.String(30), nullable=False)

    def __init__(self, EMAIL, PASSWORD, PRIVILEGE):
        self.EMAIL = EMAIL
        self.PASSWORD = PASSWORD
        self.PRIVILEGE = PRIVILEGE

    def __repr__(self):
        return '<User %r>' % self.EMAIL


class Campaigner(db.Model):
    CAMP_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EMAIL = db.Column(db.String(80), primary_key=True)
    PASSWORD = db.Column(db.String(120))
    FIRSTNAME = db.Column(db.String(50))
    LASTNAME = db.Column(db.String(50))
    ENROLLMENT_NO = db.Column(db.String(15))
    BRANCH = db.Column(db.String(50))
    SEM = db.Column(db.Integer)
    MOBILE = db.Column(db.BigInteger)
    STATUS = db.Column(db.String(10))

    def __init__(self, EMAIL, PASSWORD, FIRSTNAME, LASTNAME, ENROLLMENT_NO, BRANCH, SEM, MOBILE, STATUS):
        self.EMAIL = EMAIL
        self.PASSWORD = PASSWORD
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.ENROLLMENT_NO = ENROLLMENT_NO
        self.BRANCH = BRANCH
        self.SEM = SEM
        self.MOBILE = MOBILE
        self.STATUS = STATUS

    def __repr__(self):
        return '<User %r>' % self.EMAIL


class Student_data(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    STUDENT_KEY = db.Column(db.String(16), primary_key=True)
    FIRSTNAME = db.Column(db.String(50))
    LASTNAME = db.Column(db.String(50))
    ENROLLMENT_NO = db.Column(db.String(15))
    BRANCH = db.Column(db.String(50))
    SEM = db.Column(db.Integer, nullable=True)
    COLLEGE = db.Column(db.String(200))
    EMAIL = db.Column(db.String(80), unique=True)
    MOBILE = db.Column(db.BigInteger)
    REG_DATE = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    EVENT_1 = db.Column(db.String(80))
    EVENT_2 = db.Column(db.String(80))
    CAMP_ID = db.Column(db.Integer)
    LAST_LOGIN = db.Column(db.String(50))

    def __init__(self, STUDENT_KEY, FIRSTNAME, LASTNAME, ENROLLMENT_NO, BRANCH, SEM, COLLEGE, EMAIL, MOBILE, EVENT_1,
                 EVENT_2, CAMP_ID, LAST_LOGIN):
        self.STUDENT_KEY = STUDENT_KEY
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.ENROLLMENT_NO = ENROLLMENT_NO
        self.BRANCH = BRANCH
        self.SEM = SEM
        self.COLLEGE = COLLEGE
        self.EMAIL = EMAIL
        self.MOBILE = MOBILE
        self.EVENT_1 = EVENT_1
        self.EVENT_2 = EVENT_2
        self.CAMP_ID = CAMP_ID
        self.LAST_LOGIN = LAST_LOGIN

    def __repr__(self):
        return '<User %r>' % self.EMAIL


class Log__deleted__students(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    STUDENT_KEY = db.Column(db.String(16))
    FIRSTNAME = db.Column(db.String(50))
    LASTNAME = db.Column(db.String(50))
    ENROLLMENT_NO = db.Column(db.String(15))
    BRANCH = db.Column(db.String(50))
    SEM = db.Column(db.Integer, nullable=True)
    COLLEGE = db.Column(db.String(200))
    EMAIL = db.Column(db.String(80))
    MOBILE = db.Column(db.BigInteger)
    REG_DATE = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    EVENT_1 = db.Column(db.String(80))
    EVENT_2 = db.Column(db.String(80))
    CAMP_ID = db.Column(db.Integer)
    DELETED_DATE = db.Column(db.String(100))

    def __init__(self, STUDENT_KEY, FIRSTNAME, LASTNAME, ENROLLMENT_NO, BRANCH, SEM, COLLEGE, EMAIL, MOBILE, EVENT_1,
                 EVENT_2, CAMP_ID, LAST_LOGIN):
        self.STUDENT_KEY = STUDENT_KEY
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME
        self.ENROLLMENT_NO = ENROLLMENT_NO
        self.BRANCH = BRANCH
        self.SEM = SEM
        self.COLLEGE = COLLEGE
        self.EMAIL = EMAIL
        self.MOBILE = MOBILE
        self.EVENT_1 = EVENT_1
        self.EVENT_2 = EVENT_2
        self.CAMP_ID = CAMP_ID
        self.LAST_LOGIN = LAST_LOGIN

    def __repr__(self):
        return '<User %r>' % self.EMAIL


class Events(db.Model):
    ID = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    NAME = db.Column(db.String(50))
    DATE = db.Column(db.String(50))
    TIME = db.Column(db.String(50))
    VENUE = db.Column(db.String(80))
    DESCRIPTION = db.Column(db.String(5000))
    RULES = db.Column(db.String(5000))
    DEPARTMENT = db.Column(db.String(50))

    def __init__(self, ID, NAME, DATE, DEPARTMENT, TIME, VENUE, DESCRIPTION, RULES):
        self.ID = ID
        self.NAME = NAME
        self.DATE = DATE
        self.DEPARTMENT = DEPARTMENT
        self.TIME = TIME
        self.VENUE = VENUE
        self.DESCRIPTION = DESCRIPTION
        self.RULES = RULES

    def __repr__(self):
        return '<User %r>' % self.NAME


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('main/index.html')


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    try:
        if request.method == "POST":
            email = request.form['email'];
            password = request.form['password'];
            admin_info = Users.query.filter_by(EMAIL=email, PASSWORD=password).first()
            if admin_info:
                id = admin_info.ID
                credential = admin_info.PRIVILEGE
                session['admin_id'] = id
                session['admin_credential'] = credential
                if credential == 'root':
                    student = Student_data.query.all()
                    myCampaigner = Campaigner.query.all()
                    myEvents = Events.query.all()
                else:
                    student = Student_data.query.filter_by(BRANCH=credential)
                    myCampaigner = Campaigner.query.filter_by(BRANCH=credential)
                    myEvents = Events.query.filter_by(DEPARTMENT=credential)

                return render_template('admin/dashboard.html', student=student, myCampaigner=myCampaigner,
                                       myEvents=myEvents)
            else:
                return render_template("backend/admin_login.html", message='Incorrect Username or Password !')
        else:
            return render_template("backend/admin_login.html")
    except:
        return render_template("backend/admin_login.html",
                       message='Problem occurred in login ! Try again later or contact admin !')


def auth(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'auth' in session:
            return f(*args, **kwargs)
        else:

            return redirect(url_for('home'))

    return wrap


@app.route('/logout')
@auth
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route('/camp_dashboard/<camp_id>', methods=['POST', 'GET'])
def camp_dashboard(camp_id):
    try:
        if request.method == "POST":
            return "camp post"
        else:
            if 'camp_logged_in' in session:
                query = Campaigner.query.filter_by(CAMP_ID=camp_id).first()
                if query.STATUS != "active":
                    message = "You Are Not Active At This Time ! contact Admin ! "
                    return render_template("backend/camp_login.html", message=message)
                else:
                    return render_template("backend/camp_dashboard.html")
            return redirect("camp/")
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/camp', methods=['POST', 'GET'])
def camp():
    try:
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']

            if email == "" and password == "":
                message = "Email or password not Allowed To Empty!"
                return render_template("backend/camp_login.html", message=message)
            query = Campaigner.query.filter_by(EMAIL=email, PASSWORD=password).first()
            if query is None:
                message = "Email or password wrong ! "
                return render_template("backend/camp_login.html", message=message)
            if query.STATUS != "active":
                message = "You Are Not Active At This Time ! contact Admin ! "
                return render_template("backend/camp_login.html", message=message)
            camp_id = query.CAMP_ID
            session['camp_logged_in'] = True
            session['auth'] = True
            session['camp_id'] = camp_id
            return redirect("camp_dashboard/" + str(session['camp_id']))
        else:
            if 'camp_logged_in' in session:
                return redirect("camp_dashboard/" + str(session['camp_id']))
            return render_template("backend/camp_login.html")
    except:
        message = ""
        return render_template("backend/404.html", message=message)


def key_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/generatekey', methods=['POST'])
def generatekey():
    if 'camp_id' not in session:
        return render_template('backend/camp_login.html')

    key = key_generator()
    return jsonify({"key": key})


@app.route('/process', methods=['POST'])
def process():
    try:
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobile = request.form['mobile']
        key = request.form['key']
        camp_id = session['camp_id']
        print(str(camp_id))
        query = Campaigner.query.filter_by(CAMP_ID=camp_id, STATUS="active").first()
        if query is None:
            return jsonify({"result": "You Are on Frezze mode ! contact Admin"})
        if fname == "":
            return jsonify({"result": "First Name required !"})
        if lname == "":
            return jsonify({"result": "Last Name required !"})
        elif email == "":
            return jsonify({"result": "email required"})
        elif mobile.isdigit() != True or len(mobile) != 10:
            return jsonify({"result": "Mobile Number is Not Valid !"})
        elif key == "":
            return jsonify({"result": "key is required"})
        else:
            query = Student_data.query.filter_by(STUDENT_KEY=key).first()
            if query is not None:
                return jsonify({"result": "key is Alredy Assigned ! generate other key!"})
            mobile = int(mobile)

            query = Student_data.query.filter_by(EMAIL=email).first()
            print(query)
            if query is not None:
                return jsonify({"result": "Email is Already Registed ! type Othe Email !"})

            try:
                print('hello')
                query = Student_data(STUDENT_KEY=key, FIRSTNAME=fname, LASTNAME=lname, ENROLLMENT_NO='', BRANCH='',
                                     SEM=0,
                                     COLLEGE='', EMAIL=email, MOBILE=mobile, EVENT_1='', EVENT_2='', CAMP_ID=camp_id,
                                     LAST_LOGIN='')
                db.session.add(query)
                db.session.commit()
                msg = "<h2 style='color:#758AA2;'>Your unique key is </h2> <h1>" + key + "</h1>"
                send_mail(email, fname + " " + lname, msg)
                # mail_camped_student(email, fname, key)
                return jsonify({"result": " ", "ok": "ok"})
            except:
                return jsonify({"result": "Something was Wrong ! please try again !  "})
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/camped_data', methods=['POST', 'GET'])
def camped_data():
    try:
        if request.method == "POST":
            return "home"
        else:
            if 'camp_logged_in' in session:
                camp_id = session['camp_id']
                query = Student_data.query.filter_by(CAMP_ID=camp_id)
                campainer = Campaigner.query.filter_by(CAMP_ID=camp_id).first()
                query1 = Log__deleted__students.query.filter_by(CAMP_ID=camp_id)
                return render_template("backend/camped_data.html", query=query, query1=query1, campainer=campainer)
            return render_template("backend/camp_login.html")
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/camp_change_password/<camp_id>', methods=['POST', 'GET'])
def camp_change_password(camp_id):
    try:
        if request.method == "POST":
            old_password = request.form['old_password']
            new_password = request.form['new_password']

            if old_password == "":
                message = "Not Allowed Empty Field ! "
                danzer = "true"
                return render_template("backend/camp_change_password.html", message=message, danzer=danzer)

            if new_password == "":
                message = "Not Allowed Empty Field ! "
                danzer = "true"
                return render_template("backend/camp_change_password.html", message=message, danzer=danzer)

            query = Campaigner.query.filter_by(CAMP_ID=camp_id).first()
            if query.STATUS != "active":
                message = "You Are Not Active At This Time ! contact Admin ! "
                danzer = "true"
                return render_template("backend/camp_login.html", message=message)

            if query.PASSWORD != old_password:
                message = "Current Password Is Wrong ! "
                danzer = "true"
                return render_template("backend/camp_change_password.html", message=message, danzer=danzer)
            try:
                query.PASSWORD = new_password
                db.session.commit()
                session.clear()
                return '<h2>Password Changed Successfully ! </h2> <a href="/camp">BACK</a>  '
            except:
                message = "Something Was wrong ! "
                danzer = "true"
                return render_template("backend/camp_change_password.html", message=message, danzer=danzer)
        else:
            return render_template("backend/camp_change_password.html")
    except:
        message = ""
        return render_template("backend/404.html", message=message)


# campaigner password forgot

@app.route('/camp_forgot_password', methods=['POST', 'GET'])
def camp_forgot_password():
    try:
        if request.method == "POST":
            email = request.form['email']
            if email == "":
                message = "email is Not Allowded to empty ! "
                danzer = "true"
                return render_template("backend/camp_forgot_password.html", message=message, danzer=danzer)

            query = Campaigner.query.filter_by(EMAIL=email).first()
            if query is None:
                message = "email Not Found ! "
                danzer = "true"
                return render_template("backend/camp_forgot_password.html", message=message, danzer=danzer)
            print(query.EMAIL)
            try:
                msg = "<h2 style='color:#758AA2;'>Your password is </h2> <h1>" + query.PASSWORD + "</h1>"
                send_mail(query.EMAIL, query.FIRSTNAME + " " + query.LASTNAME, msg)
                message = "Password is sent on your Registed Email !  "
                danzer = "false"
                return render_template("backend/camp_forgot_password.html", message=message, danzer=danzer)
            except:
                message = "Please Contact Developer ! "
                danzer = "true"
                return render_template("backend/camp_forgot_password.html", message=message, danzer=danzer)
        else:
            return render_template("backend/camp_forgot_password.html")
    except:
        message = ""
        return render_template("backend/404.html", message=message)

        # Het


@app.route('/dashboard')
def dash():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        if session['admin_credential'] == 'root':
            student = Student_data.query.all()
            myCampaigner = Campaigner.query.all()
            myEvents = Events.query.all()
        else:
            student = Student_data.query.filter_by(BRANCH=session['admin_credential'])
            myCampaigner = Campaigner.query.filter_by(BRANCH=session['admin_credential'])
            myEvents = Events.query.filter_by(DEPARTMENT=session['admin_credential'])
        return render_template('admin/dashboard.html', student=student, myCampaigner=myCampaigner, myEvents=myEvents)
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/campaigner', defaults={'data': home, 'message': None})
@app.route('/campaigner/<data>', defaults={'message': None})
@app.route('/campaigner/<data>/<message>')
def camp1(data, message='none'):
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        if session['admin_credential'] == 'root':
            myCampaigner = Campaigner.query.all()
        else:
            myCampaigner = Campaigner.query.filter_by(BRANCH=session['admin_credential'])
        return render_template('admin/campaigner.html', myCampaigner=myCampaigner, data=data, message=message)
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/admin_logout')
def admin_logout():
    session.clear()
    return redirect(url_for("admin"))


@app.route('/form-register-campaigner', methods=['POST'])
def add_campaigner():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        if request.method == 'POST':
            email = request.form['email']
            fname = request.form['firstname']
            lname = request.form['lastname']
            erno = request.form['er_no']
            branch = request.form['branch']
            mobile_number = request.form['mobile_number']
            sem = request.form['sem']
            print('type : ' + str(mobile_number.isdigit()))

            if mobile_number.isdigit() is False:
                return jsonify({'data': 'Invalid Mobile Number'})
            elif len(str(mobile_number)) is not 10:
                return jsonify({'data': 'Invalid Mobile Number'})
            elif erno.isdigit() is False:
                return jsonify({'data': 'Invalid Enrollment Number'})
            elif len(str(erno)) is not 11:
                return jsonify({'data': 'Invalid Enrollment Number'})
            else:
                try:
                    pas = generate_camp_password(8)
                    campaigner_user = Campaigner(EMAIL=email, PASSWORD=pas, FIRSTNAME=fname, LASTNAME=lname,
                                                 ENROLLMENT_NO=erno,
                                                 BRANCH=branch, SEM=sem, MOBILE=mobile_number, STATUS='active')
                    db.session.add(campaigner_user)
                    db.session.commit()
                    msg = "<h2 style='color:#758AA2;'>Your password is </h2> <h1>" + pas + "</h1>"
                    send_mail(email, fname + " " + lname, msg)
                    # mail_campaigner_password(email, fname + " " + lname, pas)
                    return jsonify({'data': 'success'})
                except:
                    return jsonify({'data': 'User already exists ! '})
    except:
        message = ""
        return render_template("backend/404.html", message=message)


def send_mail(receiver_email, name, msg):
    sender_email = "UvpceConvergence2k19@gmail.com"
    password = "2k19_convergence@Uvpce"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Convergence2k19 Campaigner Password"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    CONVERGENCE"""
    html = """\
    <html>
      <body>
        <p>Hi ,""" + name + """<br>
           This is Convergence 2k19 Admin<br>
           <br><br>
    	   """ + msg + """
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, password)
    s.sendmail(sender_email, receiver_email, message.as_string())
    s.quit()


def generate_camp_password(size):
    exists = 1;
    while exists != 0:
        p = id_generator(size)
        exists = Campaigner.query.filter_by(PASSWORD=p).count()
    return str(p)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/show_camp_password', methods=['POST'])
def show_camp_password():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        campid = request.form['camp_id']
        enteredpassword = request.form['validatepassword']
        if enteredpassword == display_password:
            c = Campaigner.query.filter_by(CAMP_ID=campid).first()
            return jsonify({'status': 'success', 'camppass': str(c.PASSWORD)})
        else:
            return jsonify({'status': 'failed'})
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/change_camp_status', methods=['POST'])
def change_camp_status():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        campid = request.form['camp_id']
        status = request.form['status']
        update_camp = Campaigner.query.filter_by(CAMP_ID=campid).first()

        if status == 'active':
            update_camp.STATUS = 'freeze'
        else:
            update_camp.STATUS = 'active'
        db.session.commit()

        return jsonify({'msg': 'success'})
    except:
        message = ""
        return render_template("backend/404.html", message=message)


# events
@app.route('/events', defaults={'action': None, 'id': None, 'msg': None})
@app.route('/events/<msg>', defaults={'action': None, 'id': None})
@app.route('/events/<action>/<id>', defaults={'msg': None})
def events(msg, action, id):
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')
        try:
            if action == "description" or action == "rules":
                myevent = Events.query.filter_by(ID=id).first()
                return render_template('admin/events.html', myevent=myevent, action=action)
            elif action == "delete":

                d = Events.query.filter_by(ID=id).first()
                db.session.delete(d)
                db.session.commit()
                myevent = Events.query.all()
                return render_template('admin/events.html', myevent=myevent, message='home', msg="deleted")

            else:
                if session['admin_credential'] == 'root':
                    myevent = Events.query.all()
                else:
                    myevent = Events.query.filter_by(DEPARTMENT=session['admin_credential'])

                return render_template('admin/events.html', myevent=myevent, message='home')
        except:
            if session['admin_credential'] == 'root':
                myevent = Events.query.all()
            else:
                myevent = Events.query.filter_by(DEPARTMENT=session['admin_credential'])
            return render_template('admin/events.html', myevent=myevent, message='home', msg="error")
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/add_event')
def add_event():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')
        return render_template('admin/add_event.html')
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/add_event_next', methods=['POST'])
def add_event_next():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        session['event_name'] = request.form['name']
        session['event_date'] = request.form['date']
        session['event_time'] = request.form['time']
        session['event_venue'] = request.form['venue']
        session['event_description'] = request.form['description']
        session['event_rules_count'] = request.form['rules']
        session['department'] = request.form['department']
        if len(session['event_name']) == 0 or len(session['event_date']) == 0 or len(session['event_time']) == 0 or len(
                session['event_venue']) == 0 or len(session['event_description']) == 0 or len(
            session['event_rules_count']) == 0:
            return render_template('admin/add_event.html', msg='empty field')
        else:
            return render_template("admin/add_event.html", status=session['event_rules_count'])
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/add_rules', methods=['POST'])
def add_rules():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        event_name = session['event_name']
        event_date = session['event_date']
        event_time = session['event_time']
        event_venue = session['event_venue']
        event_depatment = session['department']
        event_description = session['event_description']
        rules = '';
        count = request.form['count']
        for i in range(int(count)):
            rules += (str(i + 1) + ". " + request.form[str(i)] + "<br>")

        # DATE
        d = str(event_date).split('-');
        date = d[2] + "/" + d[1] + "/" + d[0]

        myevents = Events(ID=None, NAME=event_name, DATE=date, DEPARTMENT=event_depatment, TIME=event_time,
                          VENUE=event_venue, DESCRIPTION=event_description, RULES=rules)
        db.session.add(myevents)
        db.session.commit()
        if session['admin_credential'] == 'root':
            myevent = Events.query.all()
        else:
            myevent = Events.query.filter_by(DEPARTMENT=session['admin_credential'])
        return render_template('admin/events.html', myevent=myevent, message='home', msg='success')
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/students')
def students():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        std = list_student_date()
        return render_template('admin/student.html', student=std)
    except:
        message = ""
        return render_template("backend/404.html", message=message)


def list_student_date():
    if session['admin_credential'] == 'root':
        student = Student_data.query.all()
        student_length = len(student)
    else:
        student = Student_data.query.filter_by(BRANCH=session['admin_credential'])
        student_length = student.count()

    std = []
    for i in range(student_length):
        std.append({})
    temp_i = 0;
    for s in student:
        std[temp_i].update({'STUDENT_KEY': s.STUDENT_KEY,
                            'FIRSTNAME': s.FIRSTNAME,
                            'LASTNAME': s.LASTNAME,
                            'ENROLLMENT_NO': s.ENROLLMENT_NO,
                            'BRANCH': s.BRANCH,
                            'SEM': s.SEM,
                            'COLLEGE': s.COLLEGE,
                            'EMAIL': s.EMAIL,
                            'MOBILE': s.MOBILE})
        temp_i += 1

    return std


@app.route('/search_student', methods=['POST'])
def search_student():
    try:
        if 'admin_id' not in session:
            return render_template('backend/admin_login.html')

        if request.method == 'POST':
            search_text = request.form['search']
            if search_text == '':
                std = list_student_date()
                return render_template('admin/student.html', student=std)

            if session['admin_credential'] == 'root':
                student = Student_data.query.all()
                student_length = len(student)
            else:
                student = Student_data.query.filter_by(BRANCH=session['admin_credential'])
                student_length = student.count()

            search_result_index = []
            std = []
            for i in range(student_length):
                std.append({})
            temp_i = 0;
            for s in student:
                std[temp_i].update({'STUDENT_KEY': s.STUDENT_KEY,
                                    'FIRSTNAME': s.FIRSTNAME,
                                    'LASTNAME': s.LASTNAME,
                                    'ENROLLMENT_NO': s.ENROLLMENT_NO,
                                    'BRANCH': s.BRANCH,
                                    'SEM': s.SEM,
                                    'COLLEGE': s.COLLEGE,
                                    'EMAIL': s.EMAIL,
                                    'MOBILE': s.MOBILE})
                temp_i += 1

            for i in range(len(std)):
                if std[i]['STUDENT_KEY'] == search_text or std[i]['FIRSTNAME'] == search_text or std[i][
                    'LASTNAME'] == search_text or str(std[i]['ENROLLMENT_NO']) == search_text or std[i][
                    'BRANCH'] == search_text or \
                        str(std[i]['SEM']) == search_text or std[i]['COLLEGE'] == search_text or std[i][
                    'EMAIL'] == search_text or str(std[i]['MOBILE']) == search_text:
                    search_result_index.append(i)

            if len(search_result_index) == 0:
                return render_template('admin/student.html', message="no result")

            search_result = []
            for i in range(len(search_result_index)):
                search_result.append(std[search_result_index[i]])

        return render_template('admin/student.html', student=search_result)
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/index.html')
def index():
    return render_template('main/index.html')


@app.route('/events/index.html')
def event_index():
    return render_template('main/events/index.html')


@app.route('/workshops/index.html')
def workshop_index():
    return render_template('main/workshops/index.html')


# temparary
@app.route('/event_view', defaults={'dept': None})
@app.route('/event_view/<dept>')
def view_events(dept):
    myevent = Events.query.all()
    l = []
    for e in myevent:
        l.append(
            {'id': e.ID, 'name': e.NAME, 'date': e.DATE, 'time': e.TIME, 'venue': e.VENUE,
             'description': e.DESCRIPTION,
             'rules': e.RULES, 'department': e.DEPARTMENT})

    sorted_l = sorted(l, key=lambda i: i['department'])
    m = {}
    previous_event = ''
    for event in sorted_l:
        if previous_event != event['department']:
            m.update({event['department']: []})

    for event in sorted_l:
        m[event['department']].append(
            {'id': event['id'], 'name': event['name'], 'date': event['date'], 'time': event['time'],
             'venue': event['venue'], 'description': event['description'], 'rules': event['rules']})

    selected_department = ''
    if dept == None:
        selected_department = sorted_l[0]['department']
    else:
        selected_department = dept

    print(m[selected_department])
    return render_template("event_view.html", myevent=m, selected_department=selected_department)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    try:
        colleges = Colleges.query.all()
        if request.method == 'POST':
            STUDENT_KEY = request.form['STUDENT_KEY']
            FIRSTNAME = request.form['FIRSTNAME']
            LASTNAME = request.form['LASTNAME']
            ENROLLMENT_NO = request.form['ENROLLMENT_NO']
            BRANCH = request.form['BRANCH']
            SEM = request.form['SEM']
            COLLEGE = request.form['COLLEGE']
            EMAIL = request.form['EMAIL']
            MOBILE = request.form['MOBILE']
            PASSWORD = request.form['PASSWORD']
            danzer = "true"

            if STUDENT_KEY == "" and FIRSTNAME == "" and LASTNAME == "" and ENROLLMENT_NO == "" and BRANCH == "" and SEM == "" and COLLEGE == "" and EMAIL == "" and MOBILE == "":
                danzer = "true"
                message = "Please Fill all Information ! "
                return render_template("registration.html", danzer=danzer, message=message)

            query = Student_data.query.filter_by(STUDENT_KEY=STUDENT_KEY, EMAIL=EMAIL).first()
            if query is None:
                message = "Your Credential Does Not Match ! "
                danzer = "true"
                return render_template("registration.html", danzer=danzer, message=message)

            try:
                update_this = Student_data.query.filter_by(EMAIL=EMAIL).first()
                update_this.FIRSTNAME = FIRSTNAME
                update_this.LASTNAME = LASTNAME
                update_this.ENROLLMENT_NO = ENROLLMENT_NO
                update_this.BRANCH = BRANCH
                update_this.SEM = SEM
                update_this.COLLEGE = COLLEGE
                update_this.MOBILE = MOBILE
                db.session.commit()
                query = Users(EMAIL=EMAIL, PASSWORD=PASSWORD, PRIVILEGE="student")
                db.session.add(query)
                db.session.commit()
                danzer = "false"
                message = "Registration Successfully Done !"
                return render_template("registration.html", danzer=danzer, message=message)
            except:
                danzer = "true"
                message = "Something Was wrong! Please Try Again !"
                return render_template("registration.html", danzer=danzer, message=message, colleges=colleges)
        else:
            return render_template("registration.html", colleges=colleges)
    except:
        message = ""
        return render_template("backend/404.html", message=message)


@app.route('/add_department_admin', methods=['POST', 'GET'])
def add_department_admin():
    try:
        if request.method == 'GET':
            user = Users.query.all()
            return render_template("admin/add_department_admin.html", users=user)

        if request.method == 'POST':
            email = request.form['email']
            department = request.form['department']
            if len(email) == 0:
                return jsonify({'data': 'empty'})
            match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I)
            if match == None:
                return jsonify({'data': 'invalid'})
            else:
                try:
                    pas = generate_admin_password(8)
                    new_admin = Users(EMAIL=email, PASSWORD=pas, PRIVILEGE=department)
                    db.session.add(new_admin)
                    db.session.commit()
                    msg = "<h2 style='color:#758AA2;'>Your password is </h2> <h1>" + pas + "</h1>"
                    send_mail(email, "Admin - " + department, msg)
                    return jsonify({'data': 'success'})
                except sqlalchemy.exc.IntegrityError:
                    return jsonify({'data': 'exists'})
                except:
                    return jsonify({'data': 'unknown'})
    except:
        message = ""
        return render_template("backend/404.html", message=message)


def generate_admin_password(size):
    exists = 1;
    while exists != 0:
        p = id_generator(size)
        exists = Users.query.filter_by(PASSWORD=p).count()
    return str(p)


@app.route('/delete_camped_student/<STUDENT_KEY>', methods=['POST'])
def delete_camped_student(STUDENT_KEY):
    try:
        if 'camp_logged_in' in session:
            try:
                camp_id = session['camp_id']
                query2 = Student_data.query.filter_by(STUDENT_KEY=STUDENT_KEY).first()
                db.session.delete(query2)
                db.session.commit()
                return redirect(url_for("camped_data"))
            except:
                return "Please try again ! something was wrong ! "
        else:
            return redirect(url_for("camp"))
    except:
        message = ""
        return render_template("backend/404.html", message=message)


if __name__ == '__main__':
    manager.run()
