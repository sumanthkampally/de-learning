select order_status, count(order_status) as orders_per_status
from orders
group by order_status order by orders_per_status desc;


select distinct customer_state, customer_city
from customers
where customer_state in ('SP','RJ','MG') and customer_city like 'santa%'
order by customer_state,customer_city;

select count(order_id) as mid_price_high_shipping_cost
from order_items
where price between 50 and 150 and freight_value >20;

select count(order_id) as mid_price_high_shipping_cost
from order_items
where price >= 50 AND price <= 150 and freight_value >20;

select count(order_id) as total_orders_in_2017
from orders
where order_purchase_timestamp >= '2017-01-01' and order_purchase_timestamp < '2018-01-01';

select count(order_id) as delayed_deliveries 
from orders 
where order_status = 'delivered' and order_delivered_customer_date > order_estimated_delivery_date ;

select customer_state, count(distinct customer_city) as different_cities
from customers
group by customer_state order by different_cities desc limit 5;


select order_status, count(order_status) as orders_per_status
from orders 
where order_purchase_timestamp >= '2017-10-01'
  and order_purchase_timestamp <  '2018-01-01'
group by order_status order by orders_per_status desc;

select order_id,price,freight_value 
from order_items 
where freight_value > price limit 10;


select distinct customer_city,customer_state
from customers
where customer_city ilike 'sao%' and customer_state <> 'SP';

select payment_type, count(payment_value) as payments_over_500
from order_payments
where payment_value > 500
group by payment_type order by payments_over_500 desc;

