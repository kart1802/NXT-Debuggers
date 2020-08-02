import psycopg2
import psycopg2.extras
from flask import Flask, render_template, request, redirect, url_for, session,send_file
import re
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
var = 0
cp = ''
items = list()
ship = list()
edu = list()


@app.route('/', methods=['GET', 'POST'])
def login():
    
    msg1 = ''
    command = 'logged out'
    modal=''
    lusername =''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    
        lusername = request.form['username']
        password = request.form['password']
                
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
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        
        susername = request.form['username']
        password = request.form['password']
        cpassword = request.form['cpassword']
        email = request.form['email']
            
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
    elif request.method == 'POST':
        
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
    global num
    select1 = request.form.get('select1')
    select2 = request.form.get('select2')
    select3 = request.form.get('select3')
    select4 = request.form.get('select4')
    # print(select1)
    # print(select2)
    # print(select3)
    # print(select4)
    if (request.method == 'POST') :
        if (select1 == 'Go to Input Page') :
            num = 1
            return redirect('/inputfortemplate')
        elif (select2 == 'Go to Input Page') :
            num = 2
            return redirect('/inputfortemplate')
        elif (select3 == 'Go to Input Page') :
            num = 3
            return redirect('/inputfortemplate')
        elif (select4 == 'Go to Input Page') :
            num = 4
            return redirect('/inputfortemplate')

    return render_template('template.html')


@app.route('/inputfortemplate',methods = ['GET','POST'])
def input1():
    if (request.method == 'POST') :  
        global var
        global num
        global cp
        global edu
        global items
        global ship
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        contact = request.form.get('contact')
        email = request.form.get('email')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        pincode = request.form.get('pincode')

        edu0 = { 'college' : request.form['college0'],
                  'adyear' : request.form['adyear0'],
                  'gradyear' : request.form['gradyear0'],
                  'cgpa' : request.form['cgpa0'],
                  'percent' : request.form['percent0'],
                  'core' : request.form['core0'],
                  'association' : {
                   'asso0' : request.form['association0'],
                   'asso1' : request.form['association1'],
                   'asso2' : request.form['association2'],
                   'asso3' : request.form['association3']
        }}
        edu.append(edu0)
        edu1 = { 'college' : request.form['college1'],
                 'adyear' : request.form['adyear1'],
                 'gradyear' : request.form['gradyear1'],
                 'cgpa' : request.form['cgpa1'],
                 'percent' : request.form['percent1'],
                 'core' : request.form['core1'],
                 'association' : {
                  'asso0' :  request.form['association4'],
                  'asso1' :  request.form['association5'],
                  'asso2' :  request.form['association6'],
                  'asso3' :  request.form['association7']
        }}
        edu.append(edu1)
        edu2 = { 'college' : request.form['college2'],
                 'adyear' : request.form['adyear2'],
                 'gradyear' : request.form['gradyear2'],
                 'cgpa' : request.form['cgpa2'],
                 'percent' : request.form['percent2'],
                 'core' : request.form['core2'],
                 'association' : {
                   'asso0' : request.form['association8'],
                   'asso1' : request.form['association9'],
                   'asso2' : request.form['association10'],
                   'asso3' : request.form['association11']
        }}
        edu.append(edu2)
        edu3 = { 'college' : request.form['college3'],
                 'adyear' : request.form['adyear3'],
                 'gradyear' : request.form['gradyear3'],
                 'cgpa' : request.form['cgpa3'],
                 'percent' : request.form['percent3'],
                 'core' : request.form['core3'],
                 'association' : {
                   'asso0' : request.form['association12'],
                   'asso1' : request.form['association13'],
                   'asso2' : request.form['association14'],
                   'asso3' : request.form['association15']
        }}
        edu.append(edu3)
        print(edu)



        objective = request.form.get('objective')
        skill = request.form.getlist('skill')
        hobby = request.form.getlist('hobby')
        items0 = { 'proname': request.form['proname0'],
                    'profrom': request.form['profrom0'],
                    'proto': request.form['proto0'],
                    'prodescription': request.form['prodescription0']}
        items.append(items0)
        items1 = { 'proname': request.form['proname1'],
                    'profrom': request.form['profrom1'],
                    'proto': request.form['proto1'],
                    'prodescription': request.form['prodescription1']}
        items.append(items1)
        items2 = { 'proname': request.form['proname2'],
                    'profrom': request.form['profrom2'],
                    'proto': request.form['proto2'],
                    'prodescription': request.form['prodescription2']}
        items.append(items2)
        items3 = { 'proname': request.form['proname3'],
                    'profrom': request.form['profrom3'],
                    'proto': request.form['proto3'],
                    'prodescription': request.form['prodescription3']}
        items.append(items3)
        # print(items)

        ship0 = { 'intitle': request.form['intitle0'],
                    'infrom': request.form['infrom0'],
                    'into': request.form['into0'],
                    'indescription': request.form['indescription0']}
        ship.append(ship0)
        ship1 = { 'intitle': request.form['intitle1'],
                    'infrom': request.form['infrom1'],
                    'into': request.form['into1'],
                    'indescription': request.form['indescription1']}
        ship.append(ship1)
        ship2 = { 'intitle': request.form['intitle2'],
                    'infrom': request.form['infrom2'],
                    'into': request.form['into2'],
                    'indescription': request.form['indescription2']}
        ship.append(ship2)
        ship3 = { 'intitle': request.form['intitle3'],
                    'infrom': request.form['infrom3'],
                    'into': request.form['into3'],
                    'indescription': request.form['indescription3']}
        ship.append(ship3)
        # print(ship)
        print(num)
        achievement = request.form.getlist('achievement')
        github = request.form.get('github')
        linkedin = request.form.get('linkedin')
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
        
        subprocess.call(['pdflatex', 'test', str(var),'.tex'])
        for fname in os.listdir(SOURCE_DIR):
            if fname.lower().endswith('.pdf'):
                shutil.move(os.path.join(SOURCE_DIR, fname), DEST_DIR)
        var = var + 1
        items.clear()
        edu.clear()
        ship.clear()
        num = 0
        return redirect('/pdf')
    return render_template("input.html")

@app.route('/pdf')
def pdf():
    global var
    global cp
    cp = 'test' + str(var-1) + '.pdf'
    
    return render_template('SignOut.html', value = cp)


@app.route('/logout')
def logout():
     return redirect(url_for('login'))  


if __name__ == "__main__":
    app.run(debug=True)