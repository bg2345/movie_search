Readme


1. Create your project folder and cd to the directory in terminal/command prompt.
2. Create your virtual environment and install dependencies. (You could also download project file from GitHub and use the requirements.txt file to install everything that is needed.) For mac:
   a. virtualenv venv
   b. source venv/bin/activate
   c. pip install flask
   d. pip install flask-bootstrap4
   e. pip install flask_sqlalchemy
   f. pip install flask_migrate
   g. pip install requests
   h. export FLASK_APP=main.py
   i. export FLASK_DEBUG=1
   j. flask run
3. Now that Flask is running, you should be able to go to http://localhost:5000/ in a browser to access the application. When it loads it will show you the current movies that are being shown in theaters in Greece, as well as the directors. It will also save this information to a SQLite database (work in progress).
