import psycopg2
import psycopg2.extras
from flask import Flask, render_template, redirect, url_for, session,send_file
from flask import request as r
import re
import random
import jinja2
import os
import shutil
import pdfkit
from jinja2 import Template
from jinja2.loaders import FileSystemLoader
from pdflatex import PDFLaTeX,pdflatex
import subprocess
import webbrowser
SOURCE_DIR = "/app"
DEST_DIR = "/app/static"

latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

app = Flask(__name__,template_folder='templates')
app.secret_key = 'your secret key'
conn = psycopg2.connect(database="d993pimcmhkbu", user = "kakgaivnavppjb", password = "9431d918ce26ad100a6f097fe09f3c484f1071d04bfafbb6fcb255d25f331a16", host = "ec2-3-215-83-17.compute-1.amazonaws.com", port = "5432")

num = 0
var = random.random()
cp = ''
items = list()
ship = list()
edu = list()
if os.path.exists("/app/static/test" +str(var)+".tex"): 
            os.remove("/app/static/test" +str(var)+".tex")
if os.path.exists("/app/static/test" +str(var)+".pdf"):
            os.remove("/app/static/test" +str(var)+".pdf")

@app.route('/', methods=['GET', 'POST'])
def login():
    
    msg1 = ''
    command = 'logged out'
    modal=''
    lusername =''
    if r.method == 'POST' and 'username' in r.form and 'password' in r.form:
    
        lusername = r.form['username']
        password = r.form['password']
                
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SELECT * FROM userinfo WHERE username = %s AND password = %s', (lusername, password,))
        
        account = cur.fetchone()
        conn.commit()
        
                
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
    if r.method == 'POST' and 'username' in r.form and 'password' in r.form and 'email' in r.form:
        
        susername = r.form['username']
        password = r.form['password']
        cpassword = r.form['cpassword']
        email = r.form['email']
            
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SELECT username FROM userinfo WHERE username = %s', (susername,))
        account = cur.fetchone()
        conn.commit()
        
        
        if account:
            msg2 = 'Account already exists!'
            modal = 'signup'
            command = 'logging'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg2 = 'Invalid email address!'
            modal = 'signup'
            command = 'logging'
        elif not re.match(r'[A-Za-z0-9]+', susername):
            msg2 = 'Username must contain only characters and numbers!'
            modal = 'signup'
            command = 'logging'
        elif password != cpassword:
            msg2 = 'confirm your password again'
            modal = 'signup'   
            command = 'logging' 
        elif not susername or not password or not email:
            msg2 = 'Please fill out the form!'
            modal = 'signup'
            command = 'logging'
        else:
            
            cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            cur.execute('INSERT INTO userinfo VALUES ( 2, %s, %s, %s)', (susername, password, email,))
            conn.commit()
            conn.close()
            signupsuccess = 'You have successfully registered. Now you can log in!'
            command = 'logging'
    elif r.method == 'POST':
        
        msg2 = 'Please fill out the form'
        modal = 'signup'
        command = 'logging'
    return render_template('homepage.html',msg2=msg2,command=command,modal=modal,signupsuccess=signupsuccess,susername=susername,email=email)

    
@app.route('/home')
def home():
    
    if 'loggedin' in session:
    
        return render_template('homepage.html', username=session['username'],command='logged in')
    
    return redirect(url_for('login'))    


@app.route('/choose-template',methods = ['GET','POST'])
def template():
    select1 = r.form.get('select1')
    select2 = r.form.get('select2')
    select3 = r.form.get('select3')
    select4 = r.form.get('select4')
    # print(select1)
    # print(select2)
    # print(select3)
    # print(select4)
    if (r.method == 'POST') :
        if (select1 == 'Go to Input Page') :
            session['num'] = 1
            return redirect('/inputfortemplate')
        elif (select2 == 'Go to Input Page') :
            session['num'] = 2
            return redirect('/inputfortemplate')
        elif (select3 == 'Go to Input Page') :
            session['num'] = 3
            return redirect('/inputfortemplate')
        elif (select4 == 'Go to Input Page') :
            session['num'] = 4
            return redirect('/inputfortemplate')

    return render_template('template.html')


@app.route('/inputfortemplate',methods = ['GET','POST'])
def input1():
    num = session.get('num')
    if (r.method == 'POST') :  
        global var
        global edu
        global items
        global ship
        fname = r.form.get('fname')
        lname = r.form.get('lname')
        contact = r.form.get('contact')
        email = r.form.get('email')
        address = r.form.get('address')
        city = r.form.get('city')
        state = r.form.get('state')
        country = r.form.get('country')
        pincode = r.form.get('pincode')

        edu0 = { 'college' : r.form['college0'],
                  'adyear' : r.form['adyear0'],
                  'gradyear' : r.form['gradyear0'],
                  'cgpa' : r.form['cgpa0'],
                  'percent' : r.form['percent0'],
                  'core' : r.form['core0'],
                  'association' : {
                   'asso0' : r.form['association0'],
                   'asso1' : r.form['association1'],
                   'asso2' : r.form['association2'],
                   'asso3' : r.form['association3']
        }}
        edu.append(edu0)
        edu1 = { 'college' : r.form['college1'],
                 'adyear' : r.form['adyear1'],
                 'gradyear' : r.form['gradyear1'],
                 'cgpa' : r.form['cgpa1'],
                 'percent' : r.form['percent1'],
                 'core' : r.form['core1'],
                 'association' : {
                  'asso0' :  r.form['association4'],
                  'asso1' :  r.form['association5'],
                  'asso2' :  r.form['association6'],
                  'asso3' :  r.form['association7']
        }}
        edu.append(edu1)
        edu2 = { 'college' : r.form['college2'],
                 'adyear' : r.form['adyear2'],
                 'gradyear' : r.form['gradyear2'],
                 'cgpa' : r.form['cgpa2'],
                 'percent' : r.form['percent2'],
                 'core' : r.form['core2'],
                 'association' : {
                   'asso0' : r.form['association8'],
                   'asso1' : r.form['association9'],
                   'asso2' : r.form['association10'],
                   'asso3' : r.form['association11']
        }}
        edu.append(edu2)
        edu3 = { 'college' : r.form['college3'],
                 'adyear' : r.form['adyear3'],
                 'gradyear' : r.form['gradyear3'],
                 'cgpa' : r.form['cgpa3'],
                 'percent' : r.form['percent3'],
                 'core' : r.form['core3'],
                 'association' : {
                   'asso0' : r.form['association12'],
                   'asso1' : r.form['association13'],
                   'asso2' : r.form['association14'],
                   'asso3' : r.form['association15']
        }}
        edu.append(edu3)
        print(edu)



        objective = r.form.get('objective')
        skill = r.form.getlist('skill')
        hobby = r.form.getlist('hobby')
        items0 = { 'proname': r.form['proname0'],
                    'profrom': r.form['profrom0'],
                    'proto': r.form['proto0'],
                    'prodescription': r.form['prodescription0']}
        items.append(items0)
        items1 = { 'proname': r.form['proname1'],
                    'profrom': r.form['profrom1'],
                    'proto': r.form['proto1'],
                    'prodescription': r.form['prodescription1']}
        items.append(items1)
        items2 = { 'proname': r.form['proname2'],
                    'profrom': r.form['profrom2'],
                    'proto': r.form['proto2'],
                    'prodescription': r.form['prodescription2']}
        items.append(items2)
        items3 = { 'proname': r.form['proname3'],
                    'profrom': r.form['profrom3'],
                    'proto': r.form['proto3'],
                    'prodescription': r.form['prodescription3']}
        items.append(items3)
        # print(items)

        ship0 = { 'intitle': r.form['intitle0'],
                    'infrom': r.form['infrom0'],
                    'into': r.form['into0'],
                    'indescription': r.form['indescription0']}
        ship.append(ship0)
        ship1 = { 'intitle': r.form['intitle1'],
                    'infrom': r.form['infrom1'],
                    'into': r.form['into1'],
                    'indescription': r.form['indescription1']}
        ship.append(ship1)
        ship2 = { 'intitle': r.form['intitle2'],
                    'infrom': r.form['infrom2'],
                    'into': r.form['into2'],
                    'indescription': r.form['indescription2']}
        ship.append(ship2)
        ship3 = { 'intitle': r.form['intitle3'],
                    'infrom': r.form['infrom3'],
                    'into': r.form['into3'],
                    'indescription': r.form['indescription3']}
        ship.append(ship3)
        # print(ship)
        print(num)
        achievement = r.form.getlist('achievement')
        github = r.form.get('github')
        linkedin = r.form.get('linkedin')
        if (num == 1) :
            template = latex_jinja_env.get_template('templates/Template-1.tex')
        elif (num == 2) :
            template = latex_jinja_env.get_template('templates/Template-2.tex')
        elif (num == 3) :
            template = latex_jinja_env.get_template('templates/Template-3.tex')
        elif (num == 4) :
            template = latex_jinja_env.get_template('templates/Template-4.tex')

        right = template.render(fname = fname, lname = lname, contact = contact ,email = email, address = address, city = city, state = state, country = country, pincode = pincode,  edu = edu, objective = objective, skill = skill, hobby = hobby, items = items,  ship = ship, achievement = achievement, github = github, linkedin = linkedin )

        with open('test'+ str(var) +'.tex','w') as f :
            f.write(right)
        f.close()
        subprocess.call(['pdflatex', 'test'+str(var)+'.tex'])
        for fname in os.listdir(SOURCE_DIR):
            if fname.lower().endswith('.pdf'):
                shutil.move(os.path.join(SOURCE_DIR, fname), DEST_DIR)
        items.clear()
        edu.clear()
        ship.clear()
        return redirect('/pdf')
    return render_template("input.html")

@app.route('/pdf')
def pdf():
    global cp
    global var
    cp = 'test'+str(var)+'.pdf'
    return render_template('SignOut.html', value = cp)

@app.route('/logout')
def logout():
     return redirect(url_for('login'))  

if __name__ == "__main__":
    app.run(debug=True)    