select * from unicorn_companies;

select sum(valuation) from unicorn_companies;
select max(valuation) from unicorn_companies;

alter table unicorn_companies modify column valuation float;

select max(valuation) from unicorn_companies;


select country, sum(valuation)
from unicorn_companies
group by country;
# split, agg, combine


select country, max(valuation)
from unicorn_companies
group by country;


select country, max(valuation)
from unicorn_companies
group by country
having max(valuation) > 90;

-- Hvaing is similar to where command but only limitation of where is that it 
-- does not work with aggregate function like sum, max, count etc..
select country, max(valuation)
from unicorn_companies
where max(valuation > 100)
group by country;


select country, sum(valuation)
from unicorn_companies
where sum(valuation > 100)
group by country;

-- initial data filter before applying aggregation
select country, sum(valuation)
from unicorn_companies
where valuation > 10
group by country
order by sum(valuation) desc;

-- filter after aggregation
select country, sum(valuation)
from unicorn_companies
group by country
having sum(valuation) > 100;


select country, sum(valuation)
from unicorn_companies
where valuation > 10
group by country
having sum(valuation) > 100;


select count(*) from unicorn_companies;

select count(*) from unicorn_companies
where valuation > 10;