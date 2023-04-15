select * from data.call_detail;
-- Locgical operators
select * from call_detail where MR_ID = 'MR0002' and Product_ID = "pr0002";

-- to select rows based on one condition within one column
select * from call_detail where Product_ID = "Pr0002" or Product_ID = "pr0003";

-- efficiency of querry'
select * from call_detail where MR_ID = "MR0002" and (HCO_ID = "HCO0001" or HCO_ID = "HCO0002");
select * from call_detail where MR_ID ="MR0002";

-- in & Not condition
select * from call_detail where MR_ID = "Mr0001" or MR_ID = "mr0003" or MR_ID = "mr0004";
select * from call_detail where MR_ID in ("mr0001", "mr0003", "mr0004");
select * from call_detail where not MR_ID = "mr0002";
select * from call_detail where not HCO_ID = "hco0001";

-- delete any row based on condtion
delete from call_detail where hcp_id = "Hcp0020";

update call_detail set product_id = 'PR0003' where hcp_id = 'hcp0019';
insert into call_detail values ("Call0020", "MR0004", "HCO0003", "HCP0020", "20-04-2024", "PR0004");	
delete from call_detail where Product_ID = "PR0004";

select * from leaders.prime_minister_terms as pm1;

select max(pm_start) from leaders.prime_minister_terms;
select min(pm_start) from leaders.prime_minister_terms;
select avg(pm_start) from leaders.prime_minister_terms;
select sum(pm_start) from leaders.prime_minister_terms;

select * from leaders.prime_minister_terms as pm1;

select * from prime_minister_terms where pm like 'N%';
select * from prime_minister_terms where pm like "h%";
select * from prime_minister_terms where pm_start like '2022';
select * from prime_minister_terms where pm like '_a%';

-- alter operations

select * from call_detail;
alter table call_detail add product_name text;
update call_detail set product_name = "apple" where Hcp_id = "HCP0001";
update call_detail set product_name = "apple" where Hcp_id = "HCP0001";
alter table call_detail drop column product_name;

alter table call_detail rename column reach_date to call_date;

-- Joins
select * from prime_minister_terms;
select * from prime_ministers;
select count(*) from prime_minister_terms;
select count(*) from prime_ministers;


select prime_minister_terms.pm, prime_minister_terms.pm_start, prime_ministers.country,
prime_ministers.continent 
from prime_minister_terms 
inner join prime_ministers
on prime_minister_terms.pm = prime_ministers.prime_minister;

select pm1.pm, pm1.pm_start, pm2.country,
pm2.continent
from 
prime_minister_terms pm1
inner join prime_ministers pm2
on pm1.pm = pm2.prime_minister;





