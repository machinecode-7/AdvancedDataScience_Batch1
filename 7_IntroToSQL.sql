select * from data.product_master;
-- schema.table => data.product_master

select product_id from data.product_master;
-- select column_nmae from schema.table

select * from data.product_master limit 2;
-- you can limit the number of rows in output

select * from data.call_detail;

-- unique values in any column
select distinct MR_ID from data.call_detail;

-- unique values within multiple columns
-- unique pairs of data within multiple columns
select distinct MR_ID, Product_ID from data.call_detail;

-- select specific rows with a given condition (relatable to filter)
select * from call_detail where MR_ID = "MR0002";

-- Insert data into table
insert into data.product_master values ('PR0004', 'Chrome');

select * from data.product_master;

-- Insert data into few columns only
insert into data.product_master (Product_ID) values ("PR0005");

select * from data.product_master;

select * from data.product_master where product_name is null;

select distinct product_id, product_name from data.product_master;

-- sort a table by a column name in ascending order
select distinct product_id, product_name from data.product_master order by product_name;

-- sort a table by a column name in descending order
select distinct product_id, product_name from data.product_master order by product_name desc;

-- count number of distinct values (it won't consider null values)
select count(distinct product_id) from data.product_master;

-- count (all)number of rows in a table
select count(*) from data.product_master;

-- delete rows based on condition
delete from data.product_master where product_name is null;