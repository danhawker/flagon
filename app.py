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

run(host='localhost', port=8080)