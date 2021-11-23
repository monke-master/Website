from sqlite3 import *


class MyDatabase:

    def __init__(self, address):
        self.connection = connect(address)
        self.cursor = self.connection.cursor()

    def getUserIdsWithLogin(self, login):
        query = "SELECT id from users WHERE login = " + '"' + login +  '"'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()

    def getTodayOrders(self):
        query = "SELECT user_id, item_id, amount, discount FROM order_history WHERE date = DATE('now')"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getDiscountItems(self):
        query = "SELECT name, price, pic_url FROM items WHERE discount > 0"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getOrdersWithSum(self, summ):
        query = "SELECT user_id, item_id, amount, discount, date FROM order_history " \
                "WHERE amount * (SELECT price from items WHERE id = user_id) > " + str(summ)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getItemIdsWithAmount(self, amount):
        query = "SELECT id FROM items where amount = " + str(amount)
        self.cursor.execute(query)
        return self.cursor.fetchall()


db = MyDatabase("database")
db.close()

