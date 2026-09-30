select product_id,product_category_name from products limit 15;

select * from orders where order_status = 'canceled'

select order_id,price from order_items order by price desc limit 10

select customer_id,customer_city,customer_state from customers where customer_state = 'RJ' order by customer_city 

select order_id, order_purchase_timestamp from orders order by order_purchase_timestamp asc limit 5

select order_id,price
from order_items
where PRICE > 0 
order by price asc limit 10

select customer_id,customer_state 
from customers 
where customer_state = 'SP' or customer_state = 'RJ' 

select order_id,order_status
from orders
where order_status <> 'delivered'