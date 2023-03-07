from flask import Flask, render_template, request

app = Flask('Students')


st = {
    23: {'fname': 'Dana', 'lname': 'Popescu', 'class': '9b'},
    2: {'fname': 'Ion', 'lname': 'Pop', 'class': '10c'},
    31: {'fname': 'Gelu', 'lname': 'Ionescu', 'class': '10c'},
    15: {'fname': 'Geta', 'lname': 'Ionescu', 'class': '9b'},
}

classes = set()
for i in st:
    classes.add(st[i]['class'])


@app.route('/')
@app.route('/students/')
def students():
    return render_template('students.html', students=st)


@app.route('/student/<student_id>/')
def show_student(student_id):
    return render_template("student.html", students=st, sid=student_id)


@app.route('/class/<class_name>/')
def show_class(class_name):
    return render_template("class.html", students=st, cl=class_name, all_cl=classes)


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_value = request.args.get('search').lower()
    search_result = {}
    for k, v in st.items():
        if search_value in v['fname'].lower() or search_value in v['lname'].lower():
            search_result[k] = v
    return render_template('students.html', students=search_result)


if __name__ == '__main__':
    app.run(debug=True)
