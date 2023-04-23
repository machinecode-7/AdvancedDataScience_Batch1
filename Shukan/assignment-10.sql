SELECT * FROM shukan.order_itemsss;

select order_items_id , product_id , quantity , pname , price ,
row_number() over (order by order_id) as sequence_no
from shukan.order_items;

select order_items_id , product_id , quantity , pname , price ,
row_number() over (order by pname) as sequence_no
from shukan.order_items;

select order_items_id , product_id , quantity , pname , price ,
row_number() over (order by pname) as row_number_name,
rank() over (order by pname) as rank_name
from shukan.order_items;

#rank rows in partitions with no gaps in ranking values
select order_items_id , product_id , quantity , pname , price ,
row_number() over (order by pname) as row_number_name,
rank() over (order by pname) as rank_name ,
dense_rank() over (order by pname) as dense_rank_name
from shukan.order_items;

#partation by
select  order_items_id , product_id , quantity , pname , price ,
dense_rank() over ( partition by quantity order by order_items_id) as dense_rank_name
from shukan.order_items;


create table shukan.order_wala as
select order_items_id , product_id , quantity , pname , price ,
dense_rank() over ( partition by quantity order by order_items_id desc) as dense_rank_name
from shukan.order_items;

select * from shukan.order_wala;

create table shukan.timepass (id int , nam int , roll_no varchar(50) );

drop table shukan.timepass;

#sub Query 
SELECT * FROM shukan.cart;
SELECT * FROM shukan.order_items;

select product_id from shukan.cart where product_id
 not in (select product_id from shukan.order_items);