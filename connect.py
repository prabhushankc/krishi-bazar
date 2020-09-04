import mysql.connector


class Connector:
    def __init__(self):
        self.khi = mysql.connector.connect(host="localhost", user="root", password="Password@123SQL", database='mydb')
        self.my_cursor = self.khi.cursor()

    def traffic(self, query, values):
        try:
            self.my_cursor.execute(query, values)
            self.khi.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def show(self, query):
        self.my_cursor.execute(query)
        data = self.my_cursor.fetchall()
        return data

    def search(self, query, value):
        self.my_cursor.execute(query, value)
        info = self.my_cursor.fetchall()
        return info


class Dbase(Connector):
    def __init__(self):
        super().__init__()

    def savenew(self, name, psw, user_name, dob, gender, address, phone, mail):
        query = "insert into registration(name,password,user_name,dob,gender,address,phone,mail) values (%s, %s, %s," \
                " %s, %s, %s, %s, %s)"
        values = (name, psw, user_name, dob, gender, address, phone, mail)
        self.traffic(query, values)
        print('asas')

    def forlogin(self, user_name, psw):
        query1 = 'select * from registration where user_name = %s and password = %s'
        values1=(user_name, psw)
        data = self.search(query1, values1)
        return data


class Storage:
    def __init__(self):
        self.two = mysql.connector.connect(host="localhost", user="root", password="Password@123SQL", database='storage')
        self.my_cursor = self.two.cursor()

    def traffic(self, query, values):
        self.my_cursor.execute(query, values)
        self.two.commit()
        return True

    def show(self, query):
        self.my_cursor.execute(query)
        data = self.my_cursor.fetchall()
        return data

    def search(self, query, value):
        self.my_cursor.execute(query, value)
        info = self.my_cursor.fetchall()
        return info

    def traffic_id(self,query, value):
        self.my_cursor.execute(query, value)
        self.two.commit()
        return self.my_cursor.lastrowid


class Gg(Storage):
    def __init__(self):
        super().__init__()

    def saveitem(self, items, price, available_quantity):
        query = "insert into unit(vegetable, price, quantity) values(%s, %s, %s)"
        values = (items, price, available_quantity)
        self.traffic(query, values)
        print('asas')

    def show_veg(self):
        query = 'select * from unit'
        return self.show(query)

    def new_cus(self,a):
        query = 'insert into customer(username) values(%s)'
        values = (a,)
        return self.traffic_id(query, values)

    def bill(self,a,b,c,d):
        query = 'insert into bill(item, price, quntity, cus_id) values(%s, %s, %s,%s)'
        values = (a, b, c, d,)
        return self.traffic_id(query, values)

    def com(self):
        query = 'select cus_id from customer'
        return self.show(query)

    def generate(self,a ):
        query= 'select sum(price*quntity) from bill where cus_id = %s'
        values = (int(a),)
        return self.search(query, values)