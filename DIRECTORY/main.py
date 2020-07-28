from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)


app.secret_key = 'your secret key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'apte@mysql!'
app.config['MYSQL_DB'] = 'pythonlogin'


mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    
    msg1 = ''
    command = 'logged out'
    modal=''
    lusername =''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    
        lusername = request.form['username']
        password = request.form['password']
                
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (lusername, password,))
        
        account = cursor.fetchone()
                
        if account:
        
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            
            return redirect(url_for('home'))
        else:
            
            msg1 = 'Incorrect username/password!'
            modal = 'login'
            command = 'logging'
    return render_template('homepage.html', msg1=msg1,command=command,modal=modal,lusername=lusername)



@app.route('/register', methods=['GET', 'POST'])
def register():

    msg2 = ''
    modal = ''
    command = 'logging'
    signupsuccess = ''
    susername =''
    email =''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        
        susername = request.form['username']
        password = request.form['password']
        cpassword = request.form['cpassword']
        email = request.form['email']
            
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (susername,))
        account = cursor.fetchone()
        
        if account:
            msg2 = 'Account already exists!'
            modal = 'signup'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg2 = 'Invalid email address!'
            modal = 'signup'
        elif not re.match(r'[A-Za-z0-9]+', susername):
            msg2 = 'Username must contain only characters and numbers!'
            modal = 'signup'
        elif password != cpassword:
            msg2 = 'confirm your password again'
            modal = 'signup'    
        elif not susername or not password or not email:
            msg2 = 'Please fill out the form!'
            modal = 'signup'
        else:
    
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (susername, password, email,))
            mysql.connection.commit()
            signupsuccess = 'You have successfully registered. Now you can log in!'
    elif request.method == 'POST':
        
        msg2 = 'Please fill out the form'
        modal = 'signup'
    return render_template('homepage.html',msg2=msg2,command=command,modal=modal,signupsuccess=signupsuccess,susername=susername,email=email)


    
@app.route('/home')
def home():
    
    if 'loggedin' in session:
    
        return render_template('homepage.html', username=session['username'],command='logged in')
    
    return redirect(url_for('login'))    



@app.route('/choose-template')
def template():
    return render_template('template.html')



@app.route('/input')
def input():
    return render_template("input.html")



@app.route('/logout')
def logout():
     return redirect(url_for('login'))  



if __name__ == "__main__":
    app.run(debug=True)