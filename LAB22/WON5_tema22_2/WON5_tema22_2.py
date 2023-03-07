from flask import Flask, render_template, request

app = Flask('Students')


st = {
    23: {'fname': 'Dana', 'lname': 'Popescu', 'class': '9b'},
    2: {'fname': 'Ion', 'lname': 'Pop', 'class': '10c'},
    31: {'fname': 'Gelu', 'lname': 'Ionescu', 'class': '10c'},
    15: {'fname': 'Geta', 'lname': 'Ionescu', 'class': '9b'},
}

classes = []
for i in st:
    if st[i]['class'] not in classes:
        classes.append(st[i]['class'])


@app.route('/')
@app.route('/students/')
def students():
    return render_template('students.html', students=st)


@app.route('/students/<student_id>/')
def show_student(student_id):
    return render_template("student.html", students=st, sid=student_id)


@app.route('/class/<class_name>/')
def show_class(class_name):
    class_list = []
    for i, k in st.items():
        if k['class'] == class_name:
            class_list.append(k)
    return render_template("class.html", cl=class_list, cl_name=class_name)


if __name__ == '__main__':
    app.run(debug=True)
