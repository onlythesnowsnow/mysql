#encoding: utf-8
import json
import MySQLdb
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def test():
    db = MySQLdb.connect("localhost", "", "", "test_database", charset='utf8')
    cursor = db.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()
    print "Database version : %s " % data
    db.close()

def insert():
    db = MySQLdb.connect("localhost", "root", "", "car_db", charset='utf8')
    cursor = db.cursor()
    car_name = '宝马'
    car_stock = 25
    sql = "INSERT INTO ck_table(car_name,car_stock) VALUES ('%s','%d')" % (car_name , car_stock)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print 'error'
        db.rollback()
    db.close()

def find_all():
    db = MySQLdb.connect("localhost", "", "", "test_database", charset='utf8')
    cursor = db.cursor()
    sql = "select * from test_table"
    cursor.execute(sql)
    results = cursor.fetchall()
    print results
    db.close()

def find_part():
    db = MySQLdb.connect("localhost", "", "", "test_database", charset='utf8')
    cursor = db.cursor()
    sql = "select * from test_table where age > '%d'" % (19)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        name = row[0]
        age = row[1]
        sex = row[2]
    print "name = %s,age = %d,sex = %s" % (name ,age ,sex)
    db.close()

def db_update():
    db = MySQLdb.connect("localhost", "", "", "test_database", charset='utf8')
    cursor = db.cursor()
    sql = "update test_table set age = age + 1 where sex = '%s' " % ("男")
    cursor.execute(sql)
    db.commit()
    db.close()

def db_delete():
    db = MySQLdb.connect("localhost", "", "", "test_database", charset='utf8')
    cursor = db.cursor()
    sql = "delete from test_table where age > '%d'" % (20)
    cursor.execute(sql)
    db.commit()
    db.close()

if __name__ == "__main__":
    insert()