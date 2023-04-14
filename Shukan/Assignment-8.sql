select * from shukan.contact;

select * from shukan.contact where state = "MI" and zip  = "70116";

select * from shukan.contact where state = "MI" or zip  = "70116";

select * from shukan.contact where county = "New York"  and (zip = "10011" or zip = "10025");
select * from shukan.contact where county = "New York";

select * from shukan.contact where county = 'Cook' or county = "Orleans" or county = "Livingston";
select * from shukan.contact where county in ('Cook' , "Orleans" , "Livingston");
-- Not condition
select * from shukan.contact where not county = 'Orleans' ;

-- delete  any row based on condition
delete from shukan.contact where city = 'Brighton' ;

-- update any row based on condition
update shukan.contact set first_name = 'shukan' where last_name = 'Butt';

select max(zip) from shukan.contact;
select min(zip) from shukan.contact;
select avg(zip) as average from shukan.contact;
select sum(zip) from shukan.contact;

select * from shukan.contact where last_name like 'M%';
select * from shukan.contact where last_name like 'Mar%';
select * from shukan.contact where last_name like '%ca';
select * from shukan.contact where last_name like '_ar%';


select * from shukan.contact;

-- add column
alter table shukan.contact add address text;

-- add column
alter table shukan.contact drop column address;

-- rename
Alter table shukan.contact rename column phone to mobile;


-- Joins --
select * from shukan.cart;
select * from shukan.order_items;



select cart.cart_id, cart.product_id, cart.pname, cart.price,
cart.qty
 from 
shukan.cart 
inner join shukan.order_items
on cart.product_id = order_items.product_id;


