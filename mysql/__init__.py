#encoding: utf-8

import MySQLdb
import sys
from flask import *
import time
import json
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['DEBUG'] = True

# 返回首页
@app.route('/main', methods=['get'])
def get_main():
        return render_template('main.html')

#仓库函数
@app.route('/ck', methods=['get'])
def get_ck():
        return render_template('ck.html')

@app.route('/add_ck', methods=['get'])
def get_add_ck():
        return render_template('add_ck.html')

@app.route('/add_ck', methods=['post'])
def post_add_ck():
    logo = {}
    db = MySQLdb.connect("localhost", "root", "", "car_db", charset='utf8')
    cursor = db.cursor()
    car_name = request.form['car_name']
    car_stock = request.form['car_stock']
    sql = "INSERT INTO ck_table(car_name,car_stock) VALUES ('%s','%s')" % (car_name, car_stock)
    if car_name != '' and car_stock != '':
        try:
            cursor.execute(sql)
            db.commit()
            logo['logo'] = u'操作成功'
            db.close()
        except:
            logo['logo'] = u'数据重复'
            db.rollback()
            db.close()
        return render_template('result.html', **logo)
    else:
        logo['logo'] = u'操作不能为空'
        db.close()
        return render_template('result.html', **logo)

@app.route('/delete_ck', methods=['get'])
def get_delete_ck():
        return render_template('delete_ck.html')

@app.route('/delete_ck', methods=['post'])
def post_delete_ck():
    logo = {}
    db = MySQLdb.connect("localhost", "root", "", "car_db", charset='utf8')
    cursor = db.cursor()
    car_name = request.form['car_name']
    sql = "delete from ck_table where car_name = '%s'" % (car_name)
    if car_name != '':
        try:
            cursor.execute(sql)
            db.commit()
            logo['logo'] = u'操作成功'
            db.close()
        except:
            logo['logo'] = u'操作失败'
            db.rollback()
            db.close()
        return render_template('result.html', **logo)
    else:
        logo['logo'] = u'操作不能为空'
        db.close()
        return render_template('result.html', **logo)

@app.route('/update_ck', methods=['get'])
def get_update_ck():
        return render_template('update_ck.html')

@app.route('/update_ck', methods=['post'])
def post_update_ck():
    logo = {}
    db = MySQLdb.connect("localhost", "root", "", "car_db", charset='utf8')
    cursor = db.cursor()
    car_name = request.form['car_name']
    car_stock = request.form['car_stock']
    sql = "update ck_table set car_stock = '%s' where car_name = '%s' " % (car_stock,car_name)
    if car_name != '':
        try:
            cursor.execute(sql)
            db.commit()
            logo['logo'] = u'操作成功'
            db.close()
        except:
            logo['logo'] = u'操作失败'
            db.rollback()
            db.close()
        return render_template('result.html', **logo)
    else:
        logo['logo'] = u'操作不能为空'
        db.close()
        return render_template('result.html', **logo)

@app.route('/find_ck', methods=['get'])
def get_find_ck():
    datas = []
    db = MySQLdb.connect("localhost", "root", "", "car_db", charset='utf8')
    cursor = db.cursor()
    sql = "select * from ck_table "
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        data = {}
        data['car_name'] = row[0]
        data['car_stock'] = row[1]
        datas.append(data)
    db.close()
    data = json.dumps(datas)
    return render_template('find_ck.html', data=data)

@app.route('/cl', methods=['get'])
def get_cl():
        return render_template('cl.html')

@app.route('/cr', methods=['get'])
def get_cr():
        return render_template('cr.html')

@app.route('/if', methods=['get'])
def get_if():
        return render_template('if.html')

@app.route('/')
def index():
    context = {
        'username': u'dddd',
        'gender': u'man',
        'age': 18
    }
    return render_template('main.html',**context)

if __name__ == '__main__':
    app.run(host='127.0.0.1')