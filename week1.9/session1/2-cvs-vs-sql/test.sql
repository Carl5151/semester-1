select name, postcode from restaurants 
where name = 'Bella Napoli';

select * from customers limit 10;

select distinct(cuisine) from restaurants;

select name from restaurants where cuisine='Italian';

select count(*) from restaurants where cuisine='Italian'