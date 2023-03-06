from flask import Flask, render_template, request
import statistics
import psycopg2

conn = None
try:
    conn = psycopg2.connect(host="localhost", database="school",
                            user="postgres", password="Kaltidata22")

    def school():
        c1 = conn.cursor()
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

        c1.execute(query)
        school_table = c1.fetchall()
        c1.close()
        return school_table

    def grade():
        c2 = conn.cursor()
        query2 = f'''select
                        g.grade,
                        g.student_id
                    from
                        grades g;
                '''

        c2.execute(query2)
        grades = c2.fetchall()
        c2.close()
        return grades

    def classes():
        c3 = conn.cursor()
        query3 = f'''select
                            c.id,
                            concat (c.class_nr, c.class_letter)
                        from
                            school_class c;
                    '''

        c3.execute(query3)
        school_classes = c3.fetchall()
        c3.close()
        return school_classes

except psycopg2.OperationalError as ex:
    print('Database error:', ex)
# finally:
#     print('Closing DB connection')
# if conn:
#     conn.close()


app = Flask('Students')

#
# st = {
#     23: {'fname': 'Dana', 'lname': 'Popescu', 'class': '9b', 'grades': [7, 8, 9, 10]},
#     2: {'fname': 'Ion', 'lname': 'Pop', 'class': '10c', 'grades': [10, 8, 6, 10]},
#     31: {'fname': 'Gelu', 'lname': 'Ionescu', 'class': '10c', 'grades': [7, 9, 9, 8]},
#     15: {'fname': 'Geta', 'lname': 'Ionescu', 'class': '9b', 'grades': [6, 8, 8, 10]},
# }


@app.route('/')
@app.route('/students/')
def students():
    return render_template('students.html', students=school())


@app.route('/students/<student_id>/')
def show_student(student_id):
    all_stud = [i[0] for i in school()]
    grades = [i[0] for i in grade() if i[1] == int(student_id)]
    media = statistics.mean(grades)
    return render_template("student.html", students=school(), sid=student_id, med=media, all_students=all_stud, stud_grades=grade())


@app.route('/class/<class_name>/')
def show_class(class_name):
    all_classes = [i[1] for i in classes()]
    return render_template("class.html", students=school(), cl=class_name, all_cl=all_classes, class_datas=classes(), stud_grades=grade())


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html', search=request.args.get('search').lower().split(), students=school())


if __name__ == '__main__':
    app.run(debug=True)


