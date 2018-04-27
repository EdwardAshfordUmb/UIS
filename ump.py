# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, send_from_directory, make_response
from flask_basicauth import BasicAuth
from nocache import nocache
from functools import wraps

##### create the application object
app = Flask(__name__)

##### use decorators to link the function to a url

###########################################################################
@app.route('/4534623452132d532home')
@nocache
def home():
    return render_template('home.html')  # render a template

#########################################
################################################### 
# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['pass'] == 'admin' and request.form['user'] == 'admin':
            return redirect(url_for('home'))
        else:
            return render_template('invalid.html', error=error)
    return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
