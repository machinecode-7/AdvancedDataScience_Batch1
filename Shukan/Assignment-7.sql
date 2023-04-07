select * from shukan.data;
select progress from shukan.data;
select * from shukan.data limit 2;
insert into shukan.data values ('jigar', '99','male','5','yellow','12/12/1992','1');
insert into shukan.data (name) values ("shukan");
select * from shukan.data where Driver is null;
select distinct Progress, Gender from shukan.data;



select * from shukan.contact;
select distinct city from shukan.contact;
select distinct city, state from shukan.contact;
select * from shukan.contact where city = "Hamilton";
select distinct first_name ,city ,zip from shukan.contact order by first_name;
select distinct first_name ,city ,zip from shukan.contact order by first_name desc;
select count(distinct first_name) from shukan.contact;
select count(*) from shukan.contact;