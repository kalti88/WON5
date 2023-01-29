import psycopg2
import statistics
conn = None

try:
    conn = psycopg2.connect(host="localhost", database="mydb",
                            user="postgres", password="Kaltidata22", options="-c search_path=school")
    c = conn.cursor()

    query1 = f'''select (id)
                from student s;
            '''
    c.execute(query1)
    all_students_id = c.fetchall()
    all_students_id = [i[0] for i in all_students_id]
    # print(all_students_id)

    query2 = f'''select distinct subject
                from grades g;
                '''
    c.execute(query2)
    all_subjects = c.fetchall()
    all_subjects = [i[0] for i in all_subjects]
    # print(all_subjects)

    for i in all_students_id:
        for j in all_subjects:
            query3 = f'''select
                              g.grade
                            from
                                grades g
                            where
                                student_id = {i} and subject = '{j}';
                        '''
            c.execute(query3)
            all_grades = c.fetchall()
            if all_grades:
                all_grades = [i[0] for i in all_grades]
                val = (j, statistics.mean(all_grades), i)
                c.execute("""insert into student_average (subject, average, student_id)
                                values (%s, %s, %s)""", val)
                conn.commit()
            else:
                val = (j, '0', i)
                c.execute("""insert into student_average (subject, average, student_id)
                                values (%s, %s, %s)""", val)
                conn.commit()

    query4 = f'''select
                      s.surname,
                      s.first_name,
                      a.subject,
                      a.average
                    from
                        student_average a
                    join
                        student s on a.student_id = s.id
                    order by subject asc, average desc;
                '''
    c.execute(query4)
    table_average = c.fetchall()
    print(table_average)
    c.close()
except psycopg2.OperationalError as ex:
    print('Database error:', ex)
finally:
    print('Closing DB connection')
if conn:
    conn.close()
