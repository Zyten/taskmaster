# Task Master : Flask CRUD
:pencil: Simple Todolist built with Flask based on a tutorial by Jake Rieger.
***
### Synopsis

Nothing major. Just a basic CRUD app.

###### Project Page: [zyten-taskmaster.herokuapp.com](https://zyten-taskmaster.herokuapp.com)

### Notes
#### Prep Environment
```bash
sudo apt install python3-pip
sudo pip3 install virtualenv #Installdir for local user was not in path by default (lazy to add :D)
```

#### Prep project folder
```bash
cd ~/dev
mkdir taskmaster && cd taskmaster
```

#### Prep and activate virtual env for our project folder
```bash
virtualenv env
source env/bin/activate
```

#### Install project dependencies
```bash
pip3 install flask flask-sqlalchemy
```

#### Create the DB
```bash
python3
```
```python3
from app import db

db.create_all()
```

#### Run the app
```bash
python3 app.py # Boots up Flask dev-server
```

#### Host in Heroku
```bash
heroku login

pip3 install gunicorn
pip3 freeze > requirements.txt

git init && git add . && git commit -m "Initial commit"

heroku create zyten-taskmaster
echo web: gunicorn app:app > Procfile

git add . && git commit -m "Add Procfile for Heroku"
git push heroku master
```

