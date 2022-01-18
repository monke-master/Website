-- Получение сегодняшних заказов
SELECT user_id, item_id, amount, discount FROM order_history WHERE date = DATE('now')