from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql7751052:3VSnLU8Jzj@sql7.freesqldatabase.com/sql7751052'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the data models
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
    __tablename__ = 'Room'
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), nullable=True)
    room_type_id = db.Column(db.Integer, nullable=True)

class RoomType(db.Model):
    __tablename__ = 'RoomType'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)

class Subject(db.Model):
    __tablename__ = 'Subject'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    subject_code = db.Column(db.String(50), nullable=True)
    lecture_hours = db.Column(db.Integer, nullable=True)
    lab_hours = db.Column(db.Integer, nullable=True)
    practical_hours = db.Column(db.Integer, nullable=True)

class Teacher(db.Model):
    __tablename__ = 'Teacher'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255), nullable=True)
    first_name = db.Column(db.String(255), nullable=True)
    middle_name = db.Column(db.String(255), nullable=True)

class Day(db.Model):
    __tablename__ = 'Day'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=True)

class Group(db.Model):
    __tablename__ = 'Group'
    id = db.Column(db.Integer, primary_key=True)
    direction = db.Column(db.String(255), nullable=True)
    group_code = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(255), nullable=True)

# Create the API endpoint to fetch the schedule
@app.route('/schedule', methods=['GET'])
def get_schedule():
    paras = Para.query.all()
    schedule = []
    for para in paras:
        schedule.append({
            'ID': para.ID,
            'TeacherID': para.TeacherID,
            'GroupID': para.GroupID,
            'RoomID': para.RoomID,
            'SubjectID': para.SubjectID,
            'DayID': para.DayID,
            'ClassNumber': para.ClassNumber,
            'PairNumber': para.PairNumber
        })
    return jsonify(schedule)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5321)
