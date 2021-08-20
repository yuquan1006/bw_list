# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: York Yu
# CreatDate: 2021/8/16 0016 11:24
# Description: 数据初始化或者同步更新
import requests, pymysql

def get_data():
    headers = {"Content-Type": "application/json;charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"}
    response = requests.post("https://www.zengjie.top/public/company/search", json={"companyName": ""}, headers=headers)
    response = response.json()
    # print(response)
    new_list = list()
    for i in response.get('data'):
        new = (j for j in i.values())
        i = tuple(new)
        new_list.append(i)
    print(new_list)
    return sorted(new_list, key= lambda x: x[0])

def init_data(results=get_data()):
    """  初始化或更新数据"""
    sql = "REPLACE into bw_list_search_bw_list(id,company_name,type,status,detail,update_time) value(%s,%s,%s,%s,'',%s)"
    db = pymysql.connect(host='localhost',user='root',password='12345678',db='bw_list')
    cursor = db.cursor()
    try:
        cursor.executemany(sql,results)
    except BaseException as e:
        print(e)
        db.rollback()
    finally:
        db.commit()
        db.close()

if __name__ == '__main__':
    init_data()