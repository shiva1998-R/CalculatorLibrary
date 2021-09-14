"""
Unit tests for the calculator library
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passw0rd',
                             database='test_db',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM test_db.Persons"
        cursor.execute(sql)
        result = cursor.fetchall()

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
        
    def test_sql(self):
        assert len(result) == 1



