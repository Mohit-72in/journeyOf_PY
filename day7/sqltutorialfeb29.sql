select @@autocommit;
-- disable auto commit for start a transaction
set autocommit = 0; 
create database Prime;
use Prime;
create table accounts(
	id int primary key auto_increment,
    name  varchar(50) not null,
    balance decimal(10,2)
);
select * from accounts;
insert into accounts(name,balance) values
	('Adam',500.00),
    ('Charlie',300.00),
    ("Bob",1000.00);
-- Adam send 50rs to Charlie
START transaction;
	UPDATE accounts set balance = balance-50 where id = 1;
	UPDATE accounts set balance = balance+50 where id = 2; 
COMMIT;
select * from accounts;

-- SQL JOINS
create table customer(
	customer_id int primary key,
    name varchar(50) not null,
    city varchar(50) not null
);
rename table customer to customers;
select * from customers;
-- insert data into customer
insert into customers (customer_id,name,city) values
	(1,"Alice",'Mumbai'),
    (2,'Bob','Delhi'),
    (3,"Charlie",'Bangalore'),
    (4,'David','Mumbai');
-- create table orders
create table orders (
	order_id int primary key,
    customer_id int,
    amount int
);
insert into orders (order_id,customer_id,amount) values
	(101,1,500),
    (102,1,900),
    (103,2,300),
    (104,5,700);
select * from orders;

-- do inner join
select * from 
	customers c inner join orders o
    on c.customer_id = o.customer_id;
select c.customer_id,o.order_id,c.name from 
	customers c inner join orders o
    on c.customer_id = o.customer_id;
-- left join
select * from 
	customers c left join orders o
    on c.customer_id = o.customer_id; 
-- right join
select * from 
	customers c right join orders o
    on c.customer_id = o.customer_id; 
-- outer join is directly not present in mysql
-- we take union of left and right join
select * from customers as c
left join orders as o
on c.customer_id = o.customer_id
UNION
select * from customers as c
right join orders as o
on c.customer_id = o.customer_id;

-- cross join
select * from
customers
cross join orders;
-- Exclusive join 2 types left/right exclusive join 
select * from customers as c
left join orders o
on c.customer_id = o.customer_id
where o.customer_id is null;
-- exclusive right join
select * from customers c
right join orders o
on c.customer_id = o.customer_id
where c.customer_id IS NULL;