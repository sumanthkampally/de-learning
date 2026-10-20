select order_id,order_status,order_purchase_timestamp as purchase_date 
from orders
order by purchase_date desc limit 10;

select order_status,count(order_status) as total_orders_per_status
from orders group by order_status order by total_orders_per_status desc;

select distinct customer_city, customer_state
from customers where customer_city like 'santa%' 
and customer_state in ('SP','RJ','MG') order by customer_state, customer_city;

select count(*) as no_of_order_items
from order_items
where price between 50 and 150 and freight_value >20;

select sum(price) as total_price, sum(freight_value) as total_shipping
from order_items;

select round(avg(price),2) as average_price_above_200 
from order_items
where price > 200;

SELECT count(*) AS orders_2017
FROM orders
WHERE order_purchase_timestamp >= '2017-01-01'
  AND order_purchase_timestamp <  '2018-01-01';

SELECT count(*) AS late_orders
FROM orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date > order_estimated_delivery_date; 

select count(distinct product_id) as products_sold
from order_items;

select count(distinct product_category_name) as categories 
from products
where product_category_name is not null;

select customer_state,count(customer_id) as total_customers
from customers
group by customer_state order by total_customers desc limit 5;

select order_id, order_delivered_carrier_date, order_status
from orders
where order_delivered_carrier_date is null and order_status not in ('canceled','unavailable') limit 10;



