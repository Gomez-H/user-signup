from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)

app.config['DEBUG'] = True
app.secret_key = 'abcdefghijklmnopqrstuvwyz'      

# it contains a space character or it consists of less than 3 characters or more than 20 characters


@app.route("/signup", methods=['GET','POST'])
def sign_up():
    new_user = request.form['username']
    new_pass = request.form['password']
    verify_password = request.form['verify']
    new_email = request.form['email']
    error = False
      
    if len(new_user) < 3 or len(new_user) > 20 or " " in new_user or new_user == "":
        flash('Username not valid','us')
        error = True
        
    if new_pass == "" or len(new_pass) < 3 or len(new_pass) >20 or " " in new_pass:
        flash('Password not valid','pw')
        error = True
        
        
    if verify_password != new_pass or verify_password == "":
        flash('Passwords do not match','verify')
        error = True
    
    if len(new_email) > 0:
        if " " in new_email or "@" not in new_email or "." not in new_email or len(new_email)> 3:
            flash('Email not valid','email')
            error = True
    if error:
        return render_template('forms.html', new_user=new_user, new_email=new_email)
            
    else: 
        return render_template('welcome.html', new_user=new_user)         

@app.route("/", methods=['GET', 'POST'])
def index():
     
     return render_template('forms.html')
     

app.run()


