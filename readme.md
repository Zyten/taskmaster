# Task Master: Simple Todolist with Flask
> https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=0s

## Notes
### Prep Environment
```bash
sudo apt install python3-pip
sudo pip3 install virtualenv #Installdir for local user was not in path by default (lazy to add :D)
```

### Prep project folder
```bash
cd ~/dev
mkdir taskmaster && cd taskmaster
```

### Prep and activate virtual env for our project folder
```bash
virtualenv env
source env/bin/activate
```

### Install project dependencies
```bash
pip3 install flask flask-sqlalchemy
```

### Create the DB
```bash
python3
```
```python3
from app import db

db.create_all()
```

### Run the app
```bash
python3 app.py # Boots up Flask dev-server
```

### Host in Heroku
```bash
heroku login

pip3 install gunicorn
pip3 freeze > requirements.txt

git init
```

