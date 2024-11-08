from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)
# tasks = []
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="senacrs",
    database="tasks_db",
    use_pure=True
    )

@app.route('/')
def index():
    sql = "SELECT * FROM tasks;"
    c = cnx.cursor()
    row = c.execute(sql)
    task = c.fetchall()

    
    return render_template('index.html', tasks=task)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        sql = f"INSERT INTO tasks (task) VALUES ('{task}');"
        c = cnx.cursor()
        c.execute(sql)
        cnx.commit()
        
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    
    if 0 <= task_id:
        sql = f"DELETE from tasks WHERE id={task_id};"
        c = cnx.cursor()
        c.execute(sql)
        cnx.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':

    app.run(debug=True)
