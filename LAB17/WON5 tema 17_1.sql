select
	s.surname as "Nume",
	s.first_name as "Prenume",
	concat (c.class_nr, c.class_letter) as "Clasa"
from 
	student s
join 
	school_class c on s.class_id = c.id
order by s.surname
