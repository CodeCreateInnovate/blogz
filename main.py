from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

tasks = []


@app.route("/blog", methods=['POST', 'GET'])
def blog():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('todos.html', title="Blog Posts", tasks=tasks)


app.run()