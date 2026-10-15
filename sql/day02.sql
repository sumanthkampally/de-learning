select order_id,price,freight_value
from order_items
where price < 20 and freight_value > 15
limit 15;

select customer_id,customer_city,customer_state
from customers 
where customer_state = 'MG' and (customer_city ='belo horizonte' or customer_city = 'uberlandia')
limit 15;

select order_id, order_status 
from orders 
where order_status in ('shipped','canceled','unavailable')
limit 15;

select order_id,price
from order_items 
where price between 100 and 200
order by price asc 
limit 15;

select customer_id,customer_state
from customers
where customer_state in ('SP','RJ','MG')
order by customer_state 
limit 20;

select distinct product_category_name
from products
where product_category_name like '%beleza%';

select distinct customer_city 
from customers
where customer_city ilike 'sao%';

select distinct product_category_name
from products 
where product_category_name like '%acessorios';

select order_id,order_purchase_timestamp 
from orders
where order_purchase_timestamp >='2018-03-01' and order_purchase_timestamp <'2018-04-01'
limit 20;



