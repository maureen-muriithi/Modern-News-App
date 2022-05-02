from app import app
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('notFound.html'),404
