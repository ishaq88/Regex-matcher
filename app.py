from flask import Flask, render_template, request, jsonify
import re
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')


app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])
def index():
    
    matches = [] 
    formatted_matches = []
    
    if request.method == 'POST':

        regex = request.form.get('regex')
        string = request.form.get('string')
              
        try:
            pattern = re.compile(regex)
            matches = pattern.finditer(string)
           
           
            for i, match in enumerate(matches):
                start, end = match.span()
                formatted_matches.append(f"Match {i+1}   ({start}-{end})  |  {match.group()}")


        except re.error as e:
            formatted_matches = [f"Invalid regular expression: {e}"]
    
        return jsonify(matches=formatted_matches)
    
    return render_template('index.html', matches=formatted_matches) 


@app.route('/emailvalidator', methods=['GET', 'POST'])
def email_validator():
    
    matches = [] 
    formatted_matches = []
    
    if request.method == 'POST':
        
        string = request.form.get('string')
              
        email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        matches = email_pattern.finditer(string)
        
        
        for i, match in enumerate(matches):
            formatted_matches.append(f"Match {i+1}   ==>  {match.group()}")


    return render_template('email_validator.html', matches=formatted_matches)

if __name__ == '__main__':
    app.run(debug=True)