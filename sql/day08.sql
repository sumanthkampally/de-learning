SELECT
  payment_type,
  COUNT(*)                       AS payments,
  ROUND(SUM(payment_value), 2)   AS total_value,
  ROUND(AVG(payment_value), 2)   AS avg_value,
  MAX(payment_value)             AS largest
FROM order_payments
GROUP BY payment_type
ORDER BY total_value DESC;

SELECT customer_state, customer_city, COUNT(*) AS customers
FROM customers
GROUP BY customer_state, customer_city
ORDER BY customers DESC
LIMIT 10;

SELECT payment_type, COUNT(*) AS big_payments
FROM order_payments
WHERE payment_value > 100
GROUP BY payment_type
ORDER BY big_payments DESC;

SELECT
  EXTRACT(YEAR FROM order_purchase_timestamp) AS order_year,
  COUNT(*) AS orders
FROM orders
GROUP BY EXTRACT(YEAR FROM order_purchase_timestamp)
ORDER BY order_year;


SELECT product_category_name, COUNT(*) AS products
FROM products
GROUP BY product_category_name
ORDER BY products DESC
LIMIT 5;


select seller_id, count(order_id) as items_sold, sum(price) as total
from order_items
group by seller_id 
order by total desc limit 5;


select order_status, count(order_id) as orders_per_status
from orders 
where order_purchase_timestamp >= '2018-01-01' and order_purchase_timestamp < '2019-01-01'
group by order_status
order by orders_per_status desc;

select extract(month from order_purchase_timestamp) as order_month,count(*) as orders
from orders
where order_purchase_timestamp >= '2017-01-01' 
	and order_purchase_timestamp < '2018-01-01'
group by extract(month from order_purchase_timestamp)
order by order_month;

select payment_installments, count(*) as payments
from order_payments
group by payment_installments 
order by payment_installments asc;

select order_id, count(order_item_id) as items 
from order_items
group by order_id
order by items desc,order_id limit 10;

select customer_state, count(customer_id) as customers_per_state
from customers
where  customer_state in ('SP','RJ','MG')
group by customer_state;


select customer_state,customer_city, count(*) 
from customers
group by customer_state;

select customer_state, count(*) 
from customers
group by customer_state;

select customer_state,customer_city, count(*) 
from customers
group by customer_state,customer_city;