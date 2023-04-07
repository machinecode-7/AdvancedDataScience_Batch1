select * from data.call_detail;

-- Logical Operators
select * from data.call_detail where mr_id = "MR0002" and HCO_ID = "HCO0001";

-- to select rows based on condition within one column 
select * from data.call_detail where mr_id = "MR0002" or mr_id = "MR0003";

-- efficiency of a query
select * from data.call_detail where mr_id = "MR0002"  and (hco_id = "HCO0001" or hco_id = "HCO0002");
select * from data.call_detail where mr_id = "MR0002";

-- Not condition
select * from data.call_detail where mr_id = 'MR0001' or mr_id = "MR0003" or mr_id = "MR0004"; -- logically correct but not easy to read and bit inneficient
select * from call_detail where mr_id in ("MR0001","MR0003","MR0004"); -- more readable but still inneficient
select * from call_detail where not mr_id = "MR0002"; -- readable and efficient

-- delete  any row based on condition
delete from data.call_detail where HCP_ID = "HCP0020";

-- update any row based on condition
update data.call_detail set product_id = 'PR0003' where hcp_id = 'HCP0019';

select * from leaders.prime_minister_terms;

select max(pm_start) from leaders.prime_minister_terms;
select min(pm_start) from leaders.prime_minister_terms;
select avg(pm_start) as average from leaders.prime_minister_terms;
select sum(pm_start) from leaders.prime_minister_terms;

select * from leaders.prime_minister_terms where prime_minister like 'H%';
select * from leaders.prime_minister_terms where prime_minister like 'Has%';
select * from leaders.prime_minister_terms where prime_minister like '%Modi';
select * from leaders.prime_minister_terms where prime_minister like '_a%';

-- Alter operations
select * from data.call_detail;

-- add column
alter table data.call_detail add Product_Name text;
-- delete column
alter table data.call_detail drop column Product_Name;
-- rename a column
Alter table data.call_detail rename column call_date to reach_date;

-- Joins ----------------------------------------------------------------------------
-- when you join two tables, and if you select * columns you will get all the columns from both the tables
-- Inner Joins
select prime_minister_terms.prime_minister, prime_minister_terms.pm_start, prime_ministers.country,
prime_ministers.continent
 from 
prime_minister_terms 
inner join prime_ministers
on prime_minister_terms.prime_minister = prime_ministers.prime_minister;

alter table prime_minister_terms rename column prime_minister to pm;

select prime_minister_terms.pm, prime_minister_terms.pm_start, prime_ministers.country,
prime_ministers.continent
from 
prime_minister_terms 
inner join prime_ministers
on prime_minister_terms.pm = prime_ministers.prime_minister;

select pm1.pm, pm1.pm_start, pm2.country, pm2.continent
from 
prime_minister_terms pm1
inner join prime_ministers pm2
on pm1.pm = pm2.prime_minister;






