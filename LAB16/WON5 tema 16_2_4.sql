CREATE SCHEMA school AUTHORIZATION postgres;

create table if not exists school_class (
	id serial primary key,
	class_nr smallint not null,
	class_letter varchar(1) not null
);


create table if not exists student (
	id serial primary key,
	surname varchar(20),
	first_name varchar(20),
	birth_date date,
	class_id int,
	foreign key (class_id) references school_class(id)
);


create table if not exists grades (
	id serial primary key,
	subject varchar(20),
	grade smallint,
	student_id int,
	foreign key (student_id) references student(id)
);
