from django.test import TestCase

# Create your tests here.
import requests, pymysql
#
# headers = {"Content-Type": "application/json;charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"}
# response = requests.post("https://www.zengjie.top/public/company/search", json={"companyName": ""}, headers=headers)
# response = response.json()
# # print(response)
# print(len(response.get('data')))
# print(response.get('data')[0])
# new_list = list()
# for i in response.get('data'):
#     new = (j for j in i.values())
#     i = tuple(new)
#     print(i)
#     new_list.append(i)
#
# print(new_list)
#
#
# sql = "insert into tablename(id,company_name,type,status) value(%s,%s)"
# results = [(1,'python'),(2,'java'),(3,'c'),(4,'golang')]
# cursor = db.cursor()
# try:
#     cursor.executemany(sql,results)
# except:
#     db.rollback()
#     traceback.print_exc()
# finally:
#     cursor.close()