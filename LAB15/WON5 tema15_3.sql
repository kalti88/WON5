select surname, first_name, average_grade 
from student;
select surname, first_name, average_grade, class_nr, class_letter
from student
	where class_nr = 10;
select surname, first_name, average_grade
from student
	where class_nr = 10 and class_letter = 'c';
select surname, first_name, average_grade 
from student
order by surname asc;
select surname, first_name, average_grade 
from student
order by average_grade desc;
select surname, first_name, average_grade 
from student
order by average_grade desc
limit 3;
select birth_date, surname, first_name 
from student
where 
	birth_date
		between '2005-01-01' and '2005-12-31';


