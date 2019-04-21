import smtplib
from flask import Flask, request, render_template, jsonify, redirect, session, url_for
import random
import string
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
import xml.etree.ElementTree as et

app = Flask(__name__)
app.secret_key = "jhsldfsakdfh23kjnk23h1j23g12kj3b12"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/convergence2k19-mitul'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# password from admin to check campaigner password
display_password = "123@abc"


class Users(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    EMAIL = db.Column(db.String(80), unique=True, nullable=False)
    PASSWORD = db.Column(db.String(120), unique=True, nullable=False)
    PRIVILEGE = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, EMAIL, PASSWORD, PRIVILEGE):
        self.EMAIL = EMAIL
        self.PASSWORD = PASSWORD
        self.PRIVILEGE = PRIVILEGE

    def __repr__(self):
        return '<User %r>' % self.EMAIL


class Campaigner(db.Model):
    CAMP_ID = db.Column(db.Integer, primary_key=True)
    EMAIL = db.Column(db.String(80), unique=True)
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
    STUDENT_KEY = db.Column(db.String(16), primary_key=True)
    FIRSTNAME = db.Column(db.String(50))
    LASTNAME = db.Column(db.String(50))
    ENROLLMENT_NO = db.Column(db.String(15))
    BRANCH = db.Column(db.String(50))
    SEM = db.Column(db.Integer, nullable=True)
    COLLEGE = db.Column(db.String(200))
    EMAIL = db.Column(db.String(80), unique=True)
    MOBILE = db.Column(db.BigInteger)
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
    if request.method == "POST":
        return "home"
    else:
        return "<h1>Home</h1>"


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if 'admin_temp_var' not in session and request.method != 'POST':
        return render_template('backend/admin_login.html');

    if request.method == "POST":
        session['admin_temp_var'] = 1
        student = Student_data.query.all()
        std = []
        for i in range(len(student)):
            std.append({})
        temp_i = 0;
        for s in student:
            std[temp_i].update({'STUDENT_KEY': s.STUDENT_KEY,
                                'NAME': s.LASTNAME + ',' + s.FIRSTNAME,
                                'ENROLLMENT_NO': s.ENROLLMENT_NO,
                                'BRANCH': s.BRANCH,
                                'SEM': s.SEM,
                                'COLLEGE': s.COLLEGE,
                                'EMAIL': s.EMAIL,
                                'MOBILE': s.MOBILE})
            temp_i += 1
        myCampaigner = Campaigner.query.all()
        myEvents = Events.query.all()
        return render_template('admin/dashboard.html', student=student, myCampaigner=myCampaigner, myEvents=myEvents)
    else:
        myUsers = Users.query.all()
        myCampaigner = Campaigner.query.all()
        return render_template('backend/admin_login.html', myUsers=myUsers, myCampaigner=myCampaigner)
        # return render_template("backend/admin_login.html")


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


@app.route('/camp', methods=['POST', 'GET'])
def camp():
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
            query = Student_data(STUDENT_KEY=key, FIRSTNAME=fname, LASTNAME=lname, ENROLLMENT_NO='', BRANCH='', SEM=0,
                                 COLLEGE='', EMAIL=email, MOBILE=mobile, EVENT_1='', EVENT_2='', CAMP_ID=camp_id,
                                 LAST_LOGIN='')
            db.session.add(query)
            db.session.commit()
            return jsonify({"result": "Register Successfully ! ", "ok": "ok"})
        except:
            return jsonify({"result": "Something was Wrong ! please try again !  "})


@app.route('/camp_change_password/<camp_id>', methods=['POST', 'GET'])
def camp_change_password(camp_id):
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
            return "<h2>Password Changed Successfully ! </h2>"
        except:
            message = "Something Was wrong ! "
            danzer = "true"
            return render_template("backend/camp_change_password.html", message=message, danzer=danzer)
    else:
        return render_template("backend/camp_change_password.html")


# campaigner password forgot

def send_data(reciver, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("testuvpce@gmail.com", "4591814515")
    s.sendmail("testuvpce@gmail.com", reciver, message)
    s.quit()


@app.route('/camp_forgot_password', methods=['POST', 'GET'])
def camp_forgot_password():
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
            reciver = query.EMAIL
            message = "Hello Campaginer : your Password is :  {} ".format(query.PASSWORD)
            send_data(reciver, message)
            message = "Password is sent on your Registed Email !  "
            danzer = "false"
            return render_template("backend/camp_forgot_password.html", message=message, danzer=danzer)
        except:
            message = "Please Contact Developer ! "
            danzer = "true"
            return render_template("backend/camp_forgot_password.html", message=message, danzer=danzer)
    else:
        return render_template("backend/camp_forgot_password.html")

        # Het


@app.route('/dashboard')
def dash():
    if 'admin_temp_var' not in session:
        return render_template('backend/admin_login.html')

    myUsers = Student_data.query.all()
    myCampaigner = Campaigner.query.all()
    myEvents = Events.query.all()
    return render_template('admin/dashboard.html', myUsers=myUsers, myCampaigner=myCampaigner, myEvents=myEvents)


@app.route('/campaigner', defaults={'data': home})
@app.route('/campaigner/<data>')
def camp1(data, message='none'):
    if 'admin_temp_var' not in session:
        return render_template('backend/admin_login.html')

    myCampaigner = Campaigner.query.all()
    return render_template('admin/campaigner.html', myCampaigner=myCampaigner, data=data, message=message)


@app.route('/admin_logout')
def admin_logout():
    session.clear()
    return redirect(url_for("admin"))


@app.route('/form-register-campaigner', methods=['POST'])
def add_campaigner():
    if 'admin_temp_var' not in session:
        return render_template('backend/admin_login.html')
    if request.method == 'POST':
        email = request.form['email']
        fname = request.form['firstname']
        lname = request.form['lastname']
        erno = request.form['er_no']
        branch = request.form['branch']
        mobile_number = request.form['mobile_number']
        sem = request.form['sem']
        pas = generate_camp_password(8)
        campaigner_user = Campaigner(EMAIL=email, PASSWORD=pas, FIRSTNAME=fname, LASTNAME=lname, ENROLLMENT_NO=erno,
                                     BRANCH=branch, SEM=sem, MOBILE=mobile_number, STATUS='active')
        db.session.add(campaigner_user)
        db.session.commit()
        myCampaigner = Campaigner.query.all()
    return redirect(url_for('camp1', data='home', message='success'))


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
    campid = request.form['camp_id']
    enteredpassword = request.form['validatepassword']
    if enteredpassword == display_password:
        c = Campaigner.query.filter_by(CAMP_ID=campid).first()
        return jsonify({'status': 'success', 'camppass': str(c.PASSWORD)})
    else:
        return jsonify({'status': 'failed'})


@app.route('/change_camp_status', methods=['POST'])
def change_camp_status():
    campid = request.form['camp_id']
    status = request.form['status']
    update_camp = Campaigner.query.filter_by(CAMP_ID=campid).first()

    if status == 'active':
        update_camp.STATUS = 'freeze'
    else:
        update_camp.STATUS = 'active'
    db.session.commit();

    return jsonify({'msg': 'success'})


# events
@app.route('/events', defaults={'action': None, 'id': None, 'msg': None})
@app.route('/events/<msg>', defaults={'action': None, 'id': None})
@app.route('/events/<action>/<id>', defaults={'msg': None})
def events(msg, action, id):
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
            myevent = Events.query.all()
            return render_template('admin/events.html', myevent=myevent, message='home')
    except:
        myevent = Events.query.all()
        return render_template('admin/events.html', myevent=myevent, message='home', msg="error")


# @app.route('/edit_desc/<id>',methods=['POST'])
# def edit_desc(id):
#     updated_desc = request.form['description']
#     base_path = os.path.dirname(os.path.realpath(__file__))
#     xml_file = os.path.join(base_path, "data\\events.xml")
#     tree = et.parse(xml_file)
#     root = tree.getroot()
#     for r in root:
#         for event in r:
#             if (event.attrib["id"] == id):
#                 for sub_tag in event:
#                     if sub_tag.tag == "description":
#                         sub_tag.text = updated_desc
#                         tree.write(xml_file)
#     return redirect(url_for('events',msg='success'))


@app.route('/add_event')
def add_event():
    return render_template('admin/add_event.html')


@app.route('/add_event_next', methods=['POST'])
def add_event_next():
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


@app.route('/add_rules', methods=['POST'])
def add_rules():
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
    myevent = Events.query.all()
    return render_template('admin/events.html', myevent=myevent, message='home', msg='success')


@app.route('/students')
def students():
    student = Student_data.query.all()

    std = []
    for i in range(len(student)):
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

    print(std)

    return render_template('admin/student.html', student=std)


@app.route('/search_student', methods=['POST'])
def search_student():
    if request.method == 'POST':
        search_text = request.form['search'];
        student = Student_data.query.all()

        search_result_index = []
        std = []
        for i in range(len(student)):
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

        search_result = []
        for i in range(len(search_result_index)):
            search_result.append(std[search_result_index[i]])

        print(search_result)
    return render_template('admin/student.html', student=search_result)


# temparary
# @app.route('/view_events')
# def view_events():
#     myevent = Events.query.all()
#     return render_template("/view_events.html",myevent=myevent)


if __name__ == '__main__':
    manager.run()
