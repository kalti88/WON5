create table if not exists supplier (
	id serial primary key,
	supplier varchar(30),
	address varchar(30),
	email_address varchar(10),
	phone varchar(10)
);