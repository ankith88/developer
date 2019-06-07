from flask import Flask, request, make_response
import json
app = Flask(__name__)

# trigger id 0
@app.route('/taskstart', methods=['GET','POST'])
def taskstart():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task start')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 1
@app.route('/taskETA', methods=['GET','POST'])
def tasketa():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task ETA')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 2
@app.route('/taskarrival', methods=['GET','POST'])
def taskarrival():
  # validate only
  if request.method == 'GET':
    print(request.args.get('check',''))
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task arrival')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 3
@app.route('/taskcomplete', methods=['GET','POST'])
def taskcomplete():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task complete')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 4
@app.route('/taskfailed', methods=['GET','POST'])
def taskfailed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task failed')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 5
@app.route('/workerduty', methods=['GET','POST'])
def workerduty():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('worker duty')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 6
@app.route('/taskcreated', methods=['GET','POST'])
def taskcreated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task created')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 7
@app.route('/taskupdated', methods=['GET','POST'])
def taskupdated():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task updated')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 8
@app.route('/taskdeleted', methods=['GET','POST'])
def taskdeleted():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task deleted')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 9
@app.route('/taskassigned', methods=['GET','POST'])
def taskassigned():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task assigned')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 10
@app.route('/taskunassigned', methods=['GET','POST'])
def taskunassigned():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task unassigned')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 12
@app.route('/taskdelayed', methods=['GET','POST'])
def taskdelayed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task delayed')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 13
@app.route('/taskcloned', methods=['GET','POST'])
def taskcloned():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('task cloned')
    print(json.dumps(request.get_json()))
    return ('',200)

# trigger id 14
@app.route('/smsrecipientresponsemissed', methods=['GET','POST'])
def smsrecipientresponsemissed():
  # validate only
  if request.method == 'GET':
    return request.args.get('check','')
  elif request.method == 'POST':
    print('SMS recipient response missed')
    print(json.dumps(request.get_json()))
    return ('',200)