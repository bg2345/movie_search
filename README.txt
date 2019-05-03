Readme


1. Create your project folder and cd to the directory in terminal/command prompt.
2. Create your virtual environment and install dependencies. (You could also download project file from GitHub and use the requirements.txt file to install everything that is needed.) For mac:
   1. virtualenv venv
   2. source venv/bin/activate
   3. pip install flask
   4. pip install flask-bootstrap4
   5. pip install flask_sqlalchemy
   6. pip install flask_migrate
   7. pip install requests
   8. export FLASK_APP=main.py
   9. export FLASK_DEBUG=1
   10. flask run
3. Now that Flask is running, you should be able to go to http://localhost:5000/ in a browser to access the application. When it loads it will show you the current movies that are being shown in theaters in Greece, as well as the directors. It will also save this information to a SQLite database (work in progress).
