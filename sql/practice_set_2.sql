select payment_type,count(payment_type) as no_of_payments
from order_payments
group by payment_type order by no_of_payments desc;

select payment_type, round(avg(payment_value),2) as average_of_payments
from order_payments
group by payment_type;

select order_id,payment_type,payment_value 
from order_payments
order by payment_value desc limit 10;

select count(*) as no_of_payments
from order_payments 
where payment_installments > 1;

select max(payment_installments) as max_installments
from order_payments;

select count(product_id) as no_of_products_morethan_5000g
from products
where product_weight_g > 5000;

select distinct product_category_name
from products
where product_category_name like 'esporte%';

select count(distinct seller_id) as no_of_different_sellers
from order_items;

select customer_state,count(distinct customer_city) as no_of_different_cities 
from customers
group by customer_state order by no_of_different_cities desc limit 5;

select order_status,count(order_id) as no_of_orders_per_status_2018
from orders 
where order_purchase_timestamp >= '2018-01-01'
and order_purchase_timestamp <  '2019-01-01'
group by order_status order by no_of_orders_per_status_2018 desc;