import mysql.connector
import dbconfig as cfg

class TaskRecordsDAO:
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
        sql="INSERT INTO tasks (user, task_date, task_type, reports_submitted, tests_completed, daily_report, notes) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from tasks"
        cursor.execute(sql)
        results = cursor.fetchall()

        returnArray = []

        for result in results:
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from tasks where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update tasks set user= %s, task_date=%s,  task_type=%s, reports_submitted=%s, tests_completed=%s, daily_report=%s, notes=%s where id= %s"
        cursor.execute(sql, values)
        self.db.commit()
        
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from tasks where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames = ['id','user','task_date','task_type','reports_submitted','tests_completed','daily_report','notes']

        item = {}

        for i, colName in enumerate(colnames):
            value = result[i]
            item[colName] = value
        return item

    def findByUser(self, user):
        cursor = self.db.cursor()
        sql="select * from tasks where user = %s"
        values = (user,)
        cursor.execute(sql, values)
        results = cursor.fetchall()

        returnArray = []

        for result in results:
            returnArray.append(self.convertToDictionary(result))

        return returnArray


taskRecordsDAO = TaskRecordsDAO()

