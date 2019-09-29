# this is an official Python runtime, used as the parent image
FROM python:3.7.2-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Flask app to run on
EXPOSE 80

# We need to run this to run in Windows
RUN chmod 644 app.py

# execute the Flask app
CMD ["python", "app.py"]

## Bash commands:
# docker build -t survey-codification:latest .
# docker run -p 5000:80 survey-codification
