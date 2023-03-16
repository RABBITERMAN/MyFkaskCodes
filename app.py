import os
from flask import send_from_directory #, add_url_rule
from flask import Flask
#import flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
	return "<b>Hello From RabbiterMan To World</b></br>hiiiii  "    
    
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

 #@app.add_url_rule('/favicon.ico',redirect_to=url_for('static', filename='favicon.ico'))
 
 
@app.route('/test')
def index2():
    """ Displays the index page accessible at '/'
    """
    return render_template('index.html')