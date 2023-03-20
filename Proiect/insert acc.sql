insert into accessories (id, cod_acc, cod_supp, description, supp_id) 
	values (default, 'PFA357', 'Fermaimposta TOP GRILLO 3037.001', 'Fermaimposta automatico per sol.libro con vite da 140mm', '3'); 
	
alter table accessories alter column description type varchar(300);