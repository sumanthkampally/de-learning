SELECT COUNT(*) as not_delivered_yet FROM orders WHERE order_delivered_customer_date IS NULL;

SELECT product_id, product_category_name
FROM products
WHERE product_category_name IS NULL
LIMIT 10;

SELECT DISTINCT order_status FROM orders;

SELECT DISTINCT customer_state, customer_city
FROM customers
ORDER BY customer_state, customer_city
LIMIT 20;

SELECT COUNT(*) AS rows_in_table,
       COUNT(DISTINCT customer_unique_id) AS unique_people
FROM customers;
SELECT customer_state AS state
FROM customers
WHERE state = 'SP'
LIMIT 5;
SELECT count(*) as no_of_customers,c.customer_state
FROM customers AS c
group by c.customer_state order by no_of_customers desc;

select count(*) as not_approved
from orders where order_approved_at is null;

select order_id,order_delivered_customer_date,order_status as status
from orders 
where order_status = 'delivered' and order_delivered_customer_date is null;

SELECT COUNT(*) AS no_category
FROM products
WHERE product_category_name IS null;

select distinct payment_type 
from order_payments;

select count(distinct(customer_city)) as unique_cities
from customers;

select count(distinct(customer_state)) as unique_states
from customers;

SELECT count(*) as total_customers,c.customer_state as state
FROM customers AS c
group by c.customer_state order by total_customers  desc;



