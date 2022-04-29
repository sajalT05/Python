from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
# initialize SQL Alchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database=SQLAlchemy(app)

class FormFields(database.Model):
    serialNumber=database.Column(database.Integer, primary_key=True)
    firstName=database.Column(database.String(200), nullable=False)
    description=database.Column(database.String(1000), nullable=False)
    dateCreation=database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self)-> str:
        return f"{serialNumber}, {firstName}, {description}, {dateCreation}"

@app.route('/')
def welcome():
    addDataInform=FormFields(firstName="John", description="This is a test")
    database.session.add(addDataInform)
    database.session.commit()
    return render_template('index.html')

@app.route('/records')
def showRecords():
    showAllRecords=FormFields.query.all()
    print(showAllRecords)
    return 'this is records page.'

if __name__=='__main__': 
    app.run(debug=True, port=8080)