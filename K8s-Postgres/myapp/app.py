from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from models import db, EmployeeModel
# import config
import os



app = Flask(__name__)


POSTGRES_URL = os.getenv['postgresUrl']   # config.CONFIG['postgresUrl']
POSTGRES_USER = os.getenv['postgresUser'] # config.CONFIG['postgresUser']
POSTGRES_PASS = os.getenv['postgresPass'] #config.CONFIG['postgresPass']
POSTGRES_DB = os.getenv['postgresDb'] #config.CONFIG['postgresDb']
DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PASS, url=POSTGRES_URL, db=POSTGRES_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)




@app.route('/')
def index():

  return render_template('index.html')   


@app.route('/submit', methods=['POST'])
def submit():
  name= request.form['name']
  surname=request.form['surname']
  age=request.form['age']
  email=request.form['email']
 
  employee=EmployeeModel(name,surname,age,email)
  db.session.add(employee)
  db.session.commit()
 
  #fetch a certain employee
  employeeResult=db.session.query(EmployeeModel).filter(EmployeeModel.id==1)
  for result in employeeResult:
    print(result.name)
 
  return render_template('success.html', data=name)



if __name__ == '__main__':
    app.run(debug=True,port=80)