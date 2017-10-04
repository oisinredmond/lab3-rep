
from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Otto3838'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.93.167'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/newrec")
def addstudent():
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO students (studentName, email) values ("third student","thirdstudent@mydit.ie")''')
    return "added a third student"

@app.route("/update")
def update():
    cur = mysql.connection.cursor()
    cur.execute('''UPDATE students SET studentName = "John Doe" WHERE studentName = "first student"''')
    return "changed third student's name"

@app.route("/delete")
def delete():
    cur = mysql.connection.cursor()
    cur.execute('''DELETE FROM students WHERE studentName = "third student"''')
    return "deleted the third student"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')
