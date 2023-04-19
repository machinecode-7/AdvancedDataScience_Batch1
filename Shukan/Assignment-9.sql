select * from shukan.order_itemsss;
select * from shukan.order_itemsss where order_items_id = 4 and order_id = 2;

select * from shukan.order_itemsss where order_items_id = 4 or order_items_id = 8;


select * from shukan.order_itemsss where quantity = 2  and (order_id = 2 or order_id = 4);

# same output using different methords
select * from shukan.order_itemsss where quantity = 2  or quantity = 3 or quantity = 5;
select * from shukan.order_itemsss where quantity in (3 ,2 ,5);
select * from shukan.order_itemsss where not quantity = 1 ;

#update
update shukan.order_itemsss set pname = "athanu" where pname = "Mango-pickle";

#delete
delete from shukan.order_itemsss where product_id = 12;

select * from shukan.order_itemsss;

select max(product_id) from shukan.order_itemsss;
select min(product_id) from shukan.order_itemsss;
select avg(product_id) from shukan.order_itemsss;
select sum(product_id) from shukan.order_itemsss;

select * from shukan.categories;
select * from shukan.products;
alter table shukan.products drop column product_price;
alter table shukan.products drop column product_image ;
alter table shukan.products drop column product_keywords;

#inner join
select product_id , product_cat , product_title , product_mrp from shukan.products
inner join shukan.categories
on product_cat = categories.cat_id;

select count(*) from shukan.products
inner join shukan.categories
on product_cat = categories.cat_id;

select product_id , product_cat , product_title , product_mrp from shukan.products
right join shukan.categories
on product_cat = categories.cat_id;

select product_id , product_cat , product_title , product_mrp from shukan.products
left join shukan.categories
on product_cat = categories.cat_id;

#case statement
select * from shukan.products;

SELECT product_title, product_mrp,
CASE WHEN product_mrp < 50 THEN 'The price is too low'
WHEN product_mrp = 50 THEN 'The price is average'
ELSE 'The price is too high'
END AS price_category
FROM shukan.products;

#subquery
select count(*) from (select * from shukan.products where product_mrp >= 50) subquery;

