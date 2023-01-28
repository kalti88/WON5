import psycopg2
conn = None
try:
    conn = psycopg2.connect(host="localhost", database="mydb",
                            user="postgres", password="Kaltidata22", options="-c search_path=school")
    c = conn.cursor()
    query = ''' select
                    s.surname as "Nume",
                    s.first_name as "Prenume",
                    concat (c.class_nr, c.class_letter) as "Clasa"
                from 
                    student s
                join 
                    school_class c on s.class_id = c.id
                order by s.surname;
            '''
    c.execute(query)
    school_table = c.fetchall()
    print(school_table)
    c.close()
except psycopg2.OperationalError as ex:
    print('Database error:', ex)
finally:
    print('Closing DB connection')
if conn:
    conn.close()
