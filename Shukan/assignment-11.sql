select * from shukan.order_items;

select sum(price) from shukan.order_items;
select max(price) from shukan.order_items;
select min(price) from shukan.order_items;
select avg(price) from shukan.order_items;

alter table shukan.order_items modify column price float;
select * from shukan.order_items;

#group by
select order_id, sum(price)
from shukan.order_items
group by order_id;

select order_id, max(price)
from shukan.order_items
group by order_id;

#having
select order_id, max(price)
from shukan.order_items
group by order_id
having max(price) > 500;


select order_id, sum(price)
from shukan.order_items
where price > 100
group by order_id
order by sum(price) desc;


select order_id, sum(price)
from shukan.order_items
group by order_id
having sum(price) > 500;


select order_id, sum(price)
from shukan.order_items
where price > 100
group by order_id
having sum(price) > 500;

select count(*) from shukan.order_items;

select count(*) from shukan.order_items
where price > 200;