# -*- coding: utf-8 -*-
import MySQLdb
import datetime
from myconfig import DbConfig

class UserPipeline(object):
    def __init__(self):
        localhost = "127.0.0.1"
        self.conn = MySQLdb.Connect (host =localhost,port= 3306,
                                user ='root',
                                passwd ='',
                                db = 'scrapy',charset='utf8')
        self.cur = self.conn.cursor()
        # 清空表
        self.cur.execute('truncate table users;')
        self.conn.commit()

    def process_item(self, item, spider):
        #self.cur.execute("""INSERT INTO users (url, name) VALUES ('11123','333')""")
        self.cur.execute(
                """INSERT IGNORE INTO users (url, name, bio, location, business, gender, avatar, education, major, employment, position, content, ask, answer, agree, thanks)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    item['url'],
                    item['name'],
                    item['bio'],
                    item['location'],
                    item['business'],
                    item['gender'],
                    item['avatar'],
                    item['education'],
                    item['major'],
                    item['employment'],
                    item['position'],
                    item['content'],
                    item['ask'],
                    item['answer'],
                    item['agree'],
                    item['thanks'],
                )
            )
        self.conn.commit()
        # self.cur.close()
        # self.conn.close()

        return item
