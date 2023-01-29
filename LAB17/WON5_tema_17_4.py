import psycopg2
conn = None

nume = input('Introdu numele elevului penrtu cautare:').lower()
prenume = input('Introdu prenumele elevului penrtu cautare:').lower()
separator = '-'

try:
    conn = psycopg2.connect(host="localhost", database="mydb",
                            user="postgres", password="Kaltidata22", options="-c search_path=school")
    c = conn.cursor()

    query1 = f'''select count(*) as "Total number of students"
            from student s
            where surname = '{nume.capitalize()}' and first_name = '{prenume.capitalize()}';
            '''
    c.execute(query1)
    all_students_same_name = c.fetchone()[0]

    query3 = f'''select
                          s.id,
                          s.surname,
                          s.first_name,
                          concat (c.class_nr, c.class_letter),
                          g.subject,
                          g.grade,
                          g.date
                        from
                            student s
                        join
                            school_class c on s.class_id = c.id
                        join 
                            grades g on s.id = g.student_id 
                        where
                            surname = '{nume.capitalize()}' and first_name = '{prenume.capitalize()}';
                    '''

    if all_students_same_name == 0:
        print('Nu exista nici un elev cu acest nume!')
    elif all_students_same_name == 1:
        c.execute(query3)
        school_table = c.fetchall()
        print(f'Numar total de elevi cu acest nume:{all_students_same_name}')
        print(f'Elevul/a cu numele {nume.capitalize()} {prenume.capitalize()} din clasa {school_table[0][3]} are urmatoarele note:')
        for i in school_table:
            print(f'Materia {i[4]} din data de {i[6]} nota {i[5]}')
    else:
        query2 = f'''select s.id                    
                            from student s
                            where surname = '{nume.capitalize()}' and first_name = '{prenume.capitalize()}';
                            '''
        c.execute(query2)
        student_id = c.fetchall()
        c.execute(query3)
        school_table = c.fetchall()
        print(f'Numar total de elevi cu acest nume:{all_students_same_name}\n {separator * 30}')
        for j in student_id:
            class_student = (i[3] for i in school_table if i[1] == j[0])
            print(f'Elevul/a cu numele {nume.capitalize()} {prenume.capitalize()} si ID-ul {j[0]} din clasa {class_student} are urmatoarele note:')
            for i in school_table:
                if i[0] == j[0]:
                    print(f'Materia {i[4]} din data de {i[6]} nota {i[5]}')
            print(f'{separator * 30}')

    c.close()
except psycopg2.OperationalError as ex:
    print('Database error:', ex)
finally:
    print('Closing DB connection')
if conn:
    conn.close()
