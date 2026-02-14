-- Total ventas por mes
SELECT
  substr(o.order_date, 1, 7) AS month,
  ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_sales
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY month
ORDER BY month;

-- Top clientes por ventas
SELECT
  c.customer_name,
  ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_sales
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY c.customer_name
ORDER BY total_sales DESC;
