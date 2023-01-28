import psycopg2
conn = None
try:
    conn = psycopg2.connect(host="localhost", database="mydb",
                            user="postgres", password="Kaltidata22", options="-c search_path=school")
    c = conn.cursor()
    nume = 'Nume'
    prenume = 'Prenume'
    clasa = "Clasa"
    separator = '-'
    query = f''' select
                    s.surname as "{nume}",
                    s.first_name as "{prenume}",
                    concat (c.class_nr, c.class_letter) as "{clasa}"
                from 
                    student s
                join 
                    school_class c on s.class_id = c.id
                order by s.surname;
            '''
    c.execute(query)
    school_table = c.fetchall()
    with open('school_table.txt', 'w') as school:
        print(f'{separator * 45}\n{nume:<20}{prenume:<20}{clasa:>5}\n{separator * 45}', file=school)
        for e in school_table:
            print(f'{e[0]:<20}{e[1]:<20}{(e[2]):>5}', file=school)
        print(f'{separator * 45}', file=school)
    c.close()
except psycopg2.OperationalError as ex:
    print('Database error:', ex)
finally:
    print('Closing DB connection')
if conn:
    conn.close()
