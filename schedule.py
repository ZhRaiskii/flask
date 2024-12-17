from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql8752605:63YTNVES7g@sql8.freemysqlhosting.net:3306/sql8752605'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Para(db.Model):
    __tablename__ = 'Para'
    ID = db.Column(db.Integer, primary_key=True)
    TeacherID = db.Column(db.Integer, nullable=True)
    GroupID = db.Column(db.Integer, nullable=True)
    RoomID = db.Column(db.Integer, nullable=True)
    SubjectID = db.Column(db.Integer, nullable=True)
    DayID = db.Column(db.Integer, nullable=True)
    ClassNumber = db.Column(db.Integer, nullable=True)
    PairNumber = db.Column(db.Integer, nullable=True)

class Room(db.Model):
    __tablename__ = 'Rooms'
    ID = db.Column(db.Integer, primary_key=True)
    RoomNumber = db.Column(db.String(50), nullable=True)
    RoomTypeID = db.Column(db.Integer, nullable=True)

class RoomType(db.Model):
    __tablename__ = 'RoomTypes'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=True)

class Subject(db.Model):
    __tablename__ = 'Subjects'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=True)
    SubjectCode = db.Column(db.String(50), nullable=True)
    LectureHours = db.Column(db.Integer, nullable=True)
    LabHours = db.Column(db.Integer, nullable=True)
    PracticalHours = db.Column(db.Integer, nullable=True)

class Teacher(db.Model):
    __tablename__ = 'Teachers'
    ID = db.Column(db.Integer, primary_key=True)
    LastName = db.Column(db.String(255), nullable=True)
    FirstName = db.Column(db.String(255), nullable=True)
    MiddleName = db.Column(db.String(255), nullable=True)

class Day(db.Model):
    __tablename__ = 'Days'
    ID = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.String(50), nullable=True)

class Group(db.Model):
    __tablename__ = 'Groups'
    ID = db.Column(db.Integer, primary_key=True)
    Direction = db.Column(db.String(255), nullable=True)
    GroupCode = db.Column(db.String(50), nullable=True)
    Name = db.Column(db.String(255), nullable=True)

@app.route('/schedule', methods=['GET'])
def get_schedule():
    paras = db.session.query(Para).all()

    teachers = {teacher.ID: teacher for teacher in db.session.query(Teacher).all()}
    groups = {group.ID: group for group in db.session.query(Group).all()}
    rooms = {room.ID: room for room in db.session.query(Room).all()}
    subjects = {subject.ID: subject for subject in db.session.query(Subject).all()}
    days = {day.ID: day for day in db.session.query(Day).all()}

    schedule = []
    for para in paras:
        teacher = teachers.get(para.TeacherID)
        group = groups.get(para.GroupID)
        room = rooms.get(para.RoomID)
        subject = subjects.get(para.SubjectID)
        day = days.get(para.DayID)

        schedule.append({
            'ID': para.ID,
            'Teacher': f"{teacher.LastName} {teacher.FirstName} {teacher.MiddleName}" if teacher else None,
            'Group': group.Name if group else None,
            'Room': room.RoomNumber if room else None,
            'Subject': subject.Name if subject else None,
            'Day': day.Date if day else None,
            'ClassNumber': para.ClassNumber,
            'PairNumber': para.PairNumber
        })

    return jsonify(schedule)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5321)
