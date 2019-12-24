import mysql.connector
import dbconfig as cfg

class UserRecordsDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database="taskRecords"
        )

    def create(self, values):
        cursor = self.db.cursor()
        sql="INSERT INTO users (user, start_date, role) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from users"
        cursor.execute(sql)
        results = cursor.fetchall()

        returnArray = []

        for result in results:
            returnArray.append(self.convertToDictionary(result))

        return returnArray
        
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from users where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames = ['id','user', 'start_date', 'role']

        item = {}

        for i, colName in enumerate(colnames):
            value = result[i]
            item[colName] = value
        return item



userRecordsDAO = UserRecordsDAO()

