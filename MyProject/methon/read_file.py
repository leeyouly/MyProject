# -*- coding: utf-8 -*-
import cx_Oracle

class ReadFileAndImportDB(object):

    def __init__(self, tns='10.6.0.94:1521/db',user='stg',password='stg123'):
        self.TNS = tns
        self.User = user
        self.Password = password

    def read_file(self):
        try:
            f = open('D:\JeBrainsProject\MyProject\MyProject\methon\win_toto14.txt', 'r')
            sortArray = []
            for line in f.readlines():
                # print line
                sortArray.append(list(line.replace('\n','')))
        except:
            print 'file read error!!!!'
        finally:
            if f:
                f.close()

        table_name = 'test_ly_01'
        insertSQL = "insert into %s(C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14) " \
                    "values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)" % (table_name)

        try:
            db = cx_Oracle.connect(self.User, self.Password, self.TNS)

            c = db.cursor()

            c.prepare(insertSQL)
            c.executemany(None, sortArray)
        finally:
            db.commit()
            db.close()



if __name__=="__main__":
    print("main")
    test = ReadFileAndImportDB()
    test.read_file()