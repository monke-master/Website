-- Получение заказов на сумму более 100 тыс. рублей 
SELECT user_id, item_id, amount, discount, date FROM order_history WHERE amount * (SELECT price from items WHERE id = user_id) > 0