from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Signup Page</title>
    </head>
    <body>
        <h1>Signup</h1>
"""

page_footer = """
    </body>
</html>
"""

# it contains a space character or it consists of less than 3 characters or more than 20 characters
@app.route("/signup", methods=['POST'])
def add_user():
    new_user = request.form['username']
    new_pass = request.form['password']
    error_username = "Not valid username"
    error_password = "Not valid password"
    if new_user == "" or len(new_user) < 3 or len(new_user) >20 or " " in new_user:
        return redirect("/?error=" + error_username)
    if new_pass == "" or len(new_pass) < 3 or len(new_pass) >20 or " " in new_pass:   
        return redirect("/?error=" + error_password)
    else: 
        return render_template('welcome.html', new_user=new_user)
      

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('forms.html', error=encoded_error)


app.run()