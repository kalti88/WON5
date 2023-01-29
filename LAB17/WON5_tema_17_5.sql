create table if not exists student_average (
	id serial primary key,
	subject varchar(20),
	average decimal,
	student_id int,
	foreign key (student_id) references student(id)
);