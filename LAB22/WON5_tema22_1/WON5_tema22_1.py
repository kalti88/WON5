from flask import Flask, render_template, request

app = Flask('Students')


st = {
    23: {'fname': 'Dana', 'lname': 'Popescu', 'class': '9b'},
    2: {'fname': 'Ion', 'lname': 'Pop', 'class': '10c'},
    31: {'fname': 'Gelu', 'lname': 'Ionescu', 'class': '10c'},
    15: {'fname': 'Geta', 'lname': 'Ionescu', 'class': '9b'},
}


@app.route('/')
@app.route('/students/')
def students():
    return render_template('students.html', students=st)


@app.route('/students/<student_id>/')
def show_student(student_id):
    return render_template("student.html", student=st.get(student_id), sid=student_id)


if __name__ == '__main__':
    app.run(debug=True)
