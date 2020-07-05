# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class ProxyspiderPipeline:
#     def process_item(self, item, spider):
#         return item

# import csv
# import json
# import pymysql
# from .settings import *
import pandas as pd
import pymysql

class ProxyspiderPipeline:
    def __init__(self):
        self.db=pymysql.connect(
            host='localhost',
            user='root',
            passwd='root',
            db='maoyan',
            charset='utf8',
            port=3306)
        self.cursor=self.db.cursor()
        print('connection mysql success.......')
    def process_item(self, item, spider):
        # return item
        title = item['title']
        link = item['link']
        time = item['time']
        category = item['category']
        # output = f'{title} category: {category} online_time: {time} link: {link}']
        # with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as movie:
        #     movie.write(output)
        # return item

        output = [f'{title} category: {category} online_time: {time} link: {link}']
        movie = pd.DataFrame(data=output)
        movie.to_csv('./moviefile2.csv', mode='a', encoding='utf8',index=False, header=False)

        # sql="INSERT INTO maoyan(title,link,time,category) VALUES(%s,%s,%s,%s)"
        sql='''INSERT INTO maoyan(title,link,time,category) VALUES(%s,%s,%s,%s);'''
        values=(title,link,time,category)
        print(sql)
        # values = (item['title'],item['link'],item['time'],item['category'])
        self.cursor.execute(sql,values)
        # self.cursor.execute(sql,(item['title'],item['link'],item['time'],item['category']))
        # self.cursor.execute(sql,({item},{link},{time},{category}))
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
    


# class ConnDB(object):
#     def __init__(self):
#         self.db=pymysql.connect(
#             host='localhost',
#             user='root',
#             passwd='root',
#             db='maoyan',
#             charset='utf8',
#             port=3306)
#         self.cursor=self.db.cursor()
#         print('connection mysql success.......')
#     def process_item(self, item, spider):
#         sql="INSERT INTO maoyan('title','link','time','category') VALUES(%s,%s,%s,%s)"
#         print(sql)
#         values = (item['title'],item['link'],item['time'],item['category'])
#         self.cursor.execute(sql,(item['title'],item['link'],item['time'],item['category']))
#         # self.cursor.execute(sql,({item},{link},{time},{category}))
#         self.db.commit()
#         return item

#     def close_spider(self, spider):
#         self.cursor.close()
#         self.db.close()

# 建表语句
# CREATE TABLE IF NOT EXISTS `maoyan`(
#    `id` bigint NOT NULL AUTO_INCREMENT,
#    `title` varchar(255) CHARACTER SET utf8,
#    `link` varchar(255) CHARACTER SET utf8,
#    `time` datetime DEFAULT NULL,
#    `category` varchar(255) CHARACTER SET utf8,
#    PRIMARY KEY (`id`)
# )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

# if __name__ == "__main__":
#     db = ConnDB()
#     db.process_item()
#     print(item)


# class ProxyspiderPipeline:
#     def process_item(self, item, spider):
#         # dic_info['name']=[item['Name']]
#         # dic_info['type']=[item['Type']]
#         # dic_info['atime']=[item['Time']]
#         # pd.DataFrame(dic_info).to_csv(path, mode='a',index=False,encoding='utf8')
#         conn = pymysql.connect(host = 'localhost',
#                                 port = 3306,
#                                 user = 'root',
#                                 password = 'root',
#                                 database = 'maoyan',
#                                 charset = 'utf8'
#                                 )

#         cur=conn.cursor()

#         result=[]
#         # values=(item['Id'],item['Name'],item['Type'],item['Time'])
#         values=(item['title'],item['link'],item['time'])

#         try:
#             # cur.execute('insert into '+'film.film_name '+' values(%s,%s,%s,%s)',values)
#             cur.execute('insert into '+'maoyan(title,link,time) '+' values(%s,%s,%s)',values)
#             # cur.execute('select * from film.film_name')
#             result.append(cur.fetchall())
#             cur.close()
#             conn.commit()

#             print(result)

#         except Exception as a:
#             print(a)

#         conn.close()
#         return item
