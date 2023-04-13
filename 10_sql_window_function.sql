select * from cars;

-- row number window function
select id, car_name, company, hp,
row_number() over (order by id) as row_number_id
from data.cars;

select id, car_name, company, hp,
row_number() over (order by car_name) as row_number_id
from data.cars;

-- rank
-- if all values in a column are unique, rank will work same as row_number
select id, car_name, company, hp,
row_number() over (order by car_name) as row_number_name,
rank() over (order by car_name) as rank_name
from data.cars;

select id, car_name, company, hp,
row_number() over (order by company) as row_number_name,
rank() over (order by company) as rank_name
from data.cars;

select id, car_name, company, hp,
row_number() over (order by company) as row_number_name,
rank() over (order by company) as rank_name,
dense_rank() over (order by company) as dense_rank_name
from data.cars;

select id, car_name, company, hp,
row_number() over (order by hp) as row_number_name,
rank() over (order by hp) as rank_name,
dense_rank() over (order by hp) as dense_rank_name
from data.cars;

select id, car_name, company, hp,
dense_rank() over (order by hp, company) as dense_rank_name
from data.cars;

select id, car_name, company, hp,
row_number() over (order by hp desc) as row_number_name,
rank() over (order by hp desc) as rank_name,
dense_rank() over (order by hp desc) as dense_rank_name
from data.cars;

-- partition by
select id, car_name, company, hp,
dense_rank() over ( partition by company order by hp) as dense_rank_name
from data.cars;

create table cars_ranked as
select id, car_name, company, hp,
dense_rank() over ( partition by company order by hp desc) as dense_rank_name
from data.cars;

select * from cars_ranked;
-- Create table

create table demo_table 
( roll_number int,
student_name varchar(255),
standard int);

drop table demo_table;

-- 8 bits => 1 byte

-- 1 -> 2 (0,1)
-- 2 -> (00, 01, 10, 11) 4
-- 3 -> (000,001,.....111) 8
-- 4 -> 16, 5-> 32, 6-> 64, 7-> 128, 8-> 256 (0,255)

select * from leaders.prime_minister_terms;
select * from leaders.prime_ministers;

-- sub query example
select pm 
from leaders.prime_minister_terms
where 
pm not in (select prime_minister from leaders.prime_ministers);


