# import './lib/bottle.py'
# This is to run on a *really* old embedded box, which runs Pythin 2.5.something.
# Rather than attemptiong to grab and install bottle using pip, setup_tools, etc
# am saving locally and importing from there.

from lib.bottle import route, run, template, request, get, post

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@get('/messages/<id:int>')
def index(id):
    return template('Message ID: {{id}}', id=id)

@get('/message/<id:int>')
def json(id):
    id=id
    return { "id": id, "name": "Test Item " + str(id) }

@route('/documents', method='PUT')
def put_document():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
#    entity = json.loads(data)
#    if not entity.has_key('id'):
#        abort(400, 'No id specified')
    try:
        return { data }

#        db['documents'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))

@route('/jsontest', method='PUT')
def put_json():
    data = request.json()
    if not data:
        abort(400, 'No data received')
    try:
        #return { data }
        return { data.id }
    except ValidationError as ve:
        abort(400, str(ve))

@route('/sendsms', method='PUT')
def send_sms():
    recipient = request.json['recipient']
    body = request.json['body']
    
    if not recipient:
        abort(400, 'No Recipient Defined')
        
    if not body:
        abort(400, 'No Message Body Defined')
    
    try:
        return {"recipient": recipient, "body": body}
        
    except ValidationError as ve:
        abort(400, str(ve))
            

run(host='localhost', port=8080)