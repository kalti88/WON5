select count(*) as "Total number of students"
from student s;

select count(*) as "Total number of students"
from student s
where surname = 'Popescu';

select count(*) as "Total number of students" 
from 
	student s
inner join 
	school_class c on s.class_id = c.id
where 
	c.class_nr = '5' and c.class_letter = 'c';
