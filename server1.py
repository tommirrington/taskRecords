from flask import Flask, jsonify, request, abort
from taskRecordsDAO import taskRecordsDAO
from userRecordsDAO import userRecordsDAO
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)


@app.route('/tasks')
def getAll():
	tasks = taskRecordsDAO.getAll()
	return jsonify(tasks)

#curl http://127.0.0.1:5000/tasks

@app.route('/tasks/<int:id>')
def findByID(id):
	foundTask = taskRecordsDAO.findByID(id)
	return jsonify(foundTask)

#curl http://127.0.0.1:5000/tasks/1

@app.route('/tasks', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'reports_submitted' in reqJson and type(reqJson['reports_submitted']) is not int:
        abort(400)
    if 'tests_completed' in reqJson and type(reqJson['tests_completed']) is not int:
        abort(400)
    # other checking 
    task = {
        "user": reqJson['user'],
        "task_date": reqJson['task_date'],
        "task_type": reqJson['task_type'],
        "reports_submitted": reqJson['reports_submitted'],
        "tests_completed": reqJson['tests_completed'],
        "daily_report": reqJson['daily_report'],
        "notes": reqJson['notes'],
    }
    values = (task['user'],task['task_date'],task['task_type'],task['reports_submitted'],task['tests_completed'],task['daily_report'],task['notes'])
    newId = taskRecordsDAO.create(values)
    task['id'] = newId
    return jsonify(task)

#curl -i  -H "Content-Type:application/json" -X POST -d '{"user":"stan","task_date":"2019-01-02","task_type":"line","reports_submitted":4,"tests_completed":3,"daily_report":"complete","notes":"nftr"}'  http://127.0.0.1:5000/tasks

@app.route('/tasks/<int:id>', methods=['PUT'])
def update(id):
    foundTask = taskRecordsDAO.findByID(id)
    if not foundTask:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'reports_submitted' in reqJson and type(reqJson['reports_submitted']) is not int:
        abort(400)
    if 'tests_completed' in reqJson and type(reqJson['tests_completed']) is not int:
        abort(400)

    if 'user' in reqJson:
        foundTask['user'] = reqJson['user']
    if 'task_date' in reqJson:
        foundTask['task_date'] = reqJson['task_date']
    if 'task_type' in reqJson:
        foundTask['task_type'] = reqJson['task_type']
    if 'reports_submitted' in reqJson:
        foundTask['reports_submitted'] = reqJson['reports_submitted']
    if 'tests_completed' in reqJson:
        foundTask['tests_completed'] = reqJson['tests_completed']
    if 'daily_report' in reqJson:
        foundTask['daily_report'] = reqJson['daily_report']
    if 'notes' in reqJson:
        foundTask['notes'] = reqJson['notes']

    values =(foundTask['user'],foundTask['task_date'],foundTask['task_type'],foundTask['reports_submitted'],foundTask['tests_completed'],foundTask['daily_report'],foundTask['notes'],foundTask['id'])
    taskRecordsDAO.update(values)
    return jsonify(foundTask)

### IMPORTANT : CHECK DATE IS FORMATTED YY-MM-DD
#curl -i  -H "Content-Type:application/json" -X PUT -d '{"user":"bob","task_date":"2019-01-01","task_type":"line","reports_submitted":2,"tests_completed":3,"daily_report":"complete","notes":"nftr"}'  http://127.0.0.1:5000/tasks/1


@app.route('/tasks/<int:id>' , methods=['DELETE'])
def delete(id):
    taskRecordsDAO.delete(id)
    return jsonify({"done":True})

#curl -X DELETE "http://127.0.0.1:5000/tasks/4"

@app.route('/tasks/<user>')
def findByUser(user):
	foundTask = taskRecordsDAO.findByUser(user)
	return jsonify(foundTask)

#curl http://127.0.0.1:5000/tasks/Edmond

# user records server calls

@app.route('/users', methods=['POST'])
def createUser():
    if not request.json:
        abort(400)
    reqJson = request.json

    user = {
        "user": reqJson['user'],
        "start_date": reqJson['start_date'],
        "role": reqJson['role'],
    }
    values = (user['user'],user['start_date'],user['role'])
    newId = userRecordsDAO.create(values)
    user['id'] = newId
    return jsonify(user)

#curl -i  -H "Content-Type:application/json" -X POST -d '{"user":"stan","start_date":"2019-01-02","role":"auditor"}'  http://127.0.0.1:5000/users

@app.route('/users')
def getAllUsers():
	users = userRecordsDAO.getAll()
	return jsonify(users)

#curl http://127.0.0.1:5000/users

@app.route('/users/<int:id>' , methods=['DELETE'])
def deleteUser(id):
    userRecordsDAO.delete(id)
    return jsonify({"done":True})

#curl -X DELETE "http://127.0.0.1:5000/users/4"


if __name__=='__main__':
	app.debug = True
	app.run()



