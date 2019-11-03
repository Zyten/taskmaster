from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # __name__ is a special var in Python that gets its value depending on how we execute the script
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// = relative path, //// = absolute path
db = SQLAlchemy(app)

# Define DB Model (will be used to automatically create table - at least in this tutorial with sqlite)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # __repr__ is Python method that defines what is echoed by interpreter when it evaluates an expression that returns an object
    def __repr__(self):
        return '<Task %>' % self.id # returns <Task 1>, <Task 2> etc. % here is just param binding

# @app.route('/')
@app.route('/', methods=['POST', 'GET']) # Specify methods that this route can handle (default only GET)
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # supports .first() etc like Eloquent (check docs)
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content'] # Are form inputs sanitised automatically?

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)

if __name__ == "__main__": # __name__ only equal to __main__ when it is executed as script (vs loading as module for example)
    app.run(debug=True)