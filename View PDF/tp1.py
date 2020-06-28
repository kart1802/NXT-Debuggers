from flask import Flask, render_template,request,redirect,send_file
import jinja2
import os
import shutil
import pdfkit
from jinja2 import Template
from jinja2.loaders import FileSystemLoader
from pdflatex import PDFLaTeX,pdflatex
import subprocess
import webbrowser
SOURCE_DIR = '/Users/Swami/Desktop/Flask/'
DEST_DIR = '/Users/Swami/Desktop/Flask/static/'

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

app=Flask(__name__,template_folder='template')
var = 0
cp = ''
items = list()
ship = list()
edu = list()
@app.route("/", methods = ['GET','POST'])
def home():
    
    if (request.method == 'POST') :  
        global var
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
                  'asso0' :  request.form['association0'],
                  'asso1' :  request.form['association1'],
                  'asso2' :  request.form['association2'],
                  'asso3' :  request.form['association3']
        }}
        edu.append(edu1)
        edu2 = { 'college' : request.form['college2'],
                 'adyear' : request.form['adyear2'],
                 'gradyear' : request.form['gradyear2'],
                 'cgpa' : request.form['cgpa2'],
                 'percent' : request.form['percent2'],
                 'core' : request.form['core2'],
                 'association' : {
                   'asso0' : request.form['association0'],
                   'asso1' : request.form['association1'],
                   'asso2' : request.form['association2'],
                   'asso3' : request.form['association3']
        }}
        edu.append(edu2)
        edu3 = { 'college' : request.form['college3'],
                 'adyear' : request.form['adyear3'],
                 'gradyear' : request.form['gradyear3'],
                 'cgpa' : request.form['cgpa3'],
                 'percent' : request.form['percent3'],
                 'core' : request.form['core3'],
                 'association' : {
                   'asso0' : request.form['association0'],
                   'asso1' : request.form['association1'],
                   'asso2' : request.form['association2'],
                   'asso3' : request.form['association3']
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
        print(ship)
    
        achievement = request.form.getlist('achievement')
        github = request.form.get('github')
        linkedin = request.form.get('linkedin')
        template = latex_jinja_env.get_template('template/Template-3.tex')
        right = template.render(fname = fname, lname = lname, contact = contact ,email = email, address = address, city = city, state = state, country = country, pincode = pincode,  edu = edu, objective = objective, skill = skill, hobby = hobby, items = items,  ship = ship, achievement = achievement, github = github, linkedin = linkedin )
        with open('test'+ str(var) +'.tex','w') as f :
            f.write(right)
        f.close()
        
        subprocess.call('pdflatex test'+ str(var) +'.tex')
        for fname in os.listdir(SOURCE_DIR):
            if fname.lower().endswith('.pdf'):
                shutil.move(os.path.join(SOURCE_DIR, fname), DEST_DIR)
        var = var + 1
        return redirect('/pdf')
    return render_template('index.html')

@app.route('/pdf')
def pdf():
    global var
    global cp
    cp = 'test' + str(var-1) + '.pdf'
    
    return render_template('home.html', value = cp)
if __name__=='__main__':
    app.run(debug=True)
