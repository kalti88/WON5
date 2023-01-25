insert into school_class (id, class_nr, class_letter) 
	values (default, '5', 'c');
insert into school_class (id, class_nr, class_letter) 
	values (default, '7', 'a');

insert into student (id, surname, first_name, birth_date, class_id) 
	values (default, 'Popescu', 'Maria', '2010-10-06', '1');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default, 'Ionescu', 'Gelu', '2011-09-02', '2');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default,'Radulescu', 'Ana-Maria', '2005-05-11', '2');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default,'Muresan', 'Ionel', '2006-12-03', '1');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default,'Lopez', 'Jennifer', '1985-10-02', '1');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default,'Todoran', 'Temistocle', '1999-06-07', '2');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default,'Popa', 'Ioana', '2009-10-06', '2');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default,'Rebengiuc', 'Victor', '1977-09-02', '2');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default,'Tanase', 'Ceorgeta', '2005-05-11', '1');    
insert into student (id, surname, first_name, birth_date, class_id) 
    values (default,'Moldovan', 'Stefan', '2005-12-03', '1');

   
insert into grades (id, subject, grade, student_id)
	values (default, 'English', '8', '1');
insert into grades (id, subject, grade, student_id)
	values (default, 'Math', '6', '2');
insert into grades (id, subject, grade, student_id)
	values (default, 'History', '9', '4');
insert into grades (id, subject, grade, student_id)
	values (default, 'Anathomy', '5', '5');
insert into grades (id, subject, grade, student_id)
	values (default, 'Chemistry', '10', '7');
insert into grades (id, subject, grade, student_id)
	values (default, 'English', '7', '2');
insert into grades (id, subject, grade, student_id)
	values (default, 'Math', '6', '3');
insert into grades (id, subject, grade, student_id)
	values (default, 'History', '9', '5');
insert into grades (id, subject, grade, student_id)
	values (default, 'Anathomy', '9.4', '6');
insert into grades (id, subject, grade, student_id)
	values (default, 'Chemistry', '5', '8');
insert into grades (id, subject, grade, student_id)
	values (default, 'English', '6', '3');
insert into grades (id, subject, grade, student_id)
	values (default, 'Math', '7', '8');
insert into grades (id, subject, grade, student_id)
	values (default, 'History', '7', '9');
insert into grades (id, subject, grade, student_id)
	values (default, 'Anathomy', '8', '8');
insert into grades (id, subject, grade, student_id)
	values (default, 'Chemistry', '6', '10');
