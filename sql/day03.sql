select count(*) from orders;
SELECT SUM(price) FROM order_items;
SELECT AVG(price) FROM order_items;
SELECT MIN(price) FROM order_items;
SELECT MAX(price) FROM order_items;
SELECT
  COUNT(*)            AS total_items,
  SUM(price)          AS total_revenue,
  ROUND(AVG(price), 2) AS avg_price,
  MIN(price)          AS cheapest,
  MAX(price)          AS most_expensive
FROM order_items;

SELECT COUNT(*) AS all_orders,
       COUNT(order_delivered_customer_date) AS orders_with_delivery_date
FROM orders;

select count(*) 
from order_items;
select SUM(price) as total_revenue 
from order_items;
select Round(AVG(price),2) as avg_price
from order_items;
select MIN(price) as cheapest_product,
		MAX(price) as expensive_product
from order_items;
select count(*)
from orders 
where order_status = 'canceled';
select ROUND(AVG(freight_value),2) as freight_over_100
from order_items 
where price > 100;
select count(*) as all_orders,
		count(order_delivered_customer_date) AS orders_with_delivery_date
	from orders;