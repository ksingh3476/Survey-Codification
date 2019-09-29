# survey-codification
Automation and codification of survey creation/generation and parsing.

Steps to run the project:

No dependencies needed, but a few commands are required to run the project. 

1. Navigate to the survey-codification directory
2. Enter `export FLASK_APP=app.py`
3. Enter `export FLASK_ENV=development` - this will allow you to run the project in debug mode, eliminating the need to run the project every time you make a change (like nodemon).
4. Enter `flask run` to run the project. 
5. Navigate to `'localhost:5000'` to see and interact with the project

#Parser Functionality

1. The parser utilizes the python-docx library in order to take a word document in which the questions are tagged as heading style 
"Heading 1" and the answers are tagged with "Normal". 

2. The results are split and stored into class objects those class objects are read into a dictionary that is returned as a JSON object.