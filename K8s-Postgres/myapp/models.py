from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class EmployeeModel(db.Model):
    __tablename__ = "employees"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    surname = db.Column(db.String())
    age= db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self,name,surname,age,email):
        
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        
 
    def __repr__(self):
        return f"{self.name}:{self.surname}"


        
     # def __repr__(self):
       # return '<User %r>' % self.username
