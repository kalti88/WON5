from flask import Flask, render_template, request
import statistics
import psycopg2

conn = None
try:
    conn = psycopg2.connect(host="localhost", database="school",
                            user="postgres", password="Kaltidata22")
    c = conn.cursor()
    query = f''' select
                    s.id,
                    s.surname,
                    s.first_name,
                    concat (c.class_nr, c.class_letter),
                    c.id
                from 
                    student s
                join 
                    school_class c on s.class_id = c.id
                order by s.surname;
            '''

    c.execute(query)
    school_table = c.fetchall()
    print(school_table)
    query2 = f'''select
                    g.grade,
                    g.student_id
                from
                    grades g;
            '''

    c.execute(query2)
    grades = c.fetchall()
    print(grades)

    query3 = f'''select
                        c.id,
                        concat (c.class_nr, c.class_letter)
                    from
                        school_class c;
                '''

    c.execute(query3)
    classes = c.fetchall()
    print(classes)

    c.close()

except psycopg2.OperationalError as ex:
    print('Database error:', ex)
finally:
    print('Closing DB connection')
if conn:
    conn.close()


app = Flask('Students')


st = {
    23: {'fname': 'Dana', 'lname': 'Popescu', 'class': '9b', 'grades': [7, 8, 9, 10]},
    2: {'fname': 'Ion', 'lname': 'Pop', 'class': '10c', 'grades': [10, 8, 6, 10]},
    31: {'fname': 'Gelu', 'lname': 'Ionescu', 'class': '10c', 'grades': [7, 9, 9, 8]},
    15: {'fname': 'Geta', 'lname': 'Ionescu', 'class': '9b', 'grades': [6, 8, 8, 10]},
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
    media = statistics.mean(st[int(student_id)]['grades'])
    return render_template("student.html", students=st, sid=student_id, med=media)


@app.route('/class/<class_name>/')
def show_class(class_name):
    return render_template("class.html", students=st, cl=class_name, all_cl=classes)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html', search=request.args.get('search').lower().split(), students=st)


if __name__ == '__main__':
    app.run(debug=True)
