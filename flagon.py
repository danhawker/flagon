# import './lib/bottle.py'
# This is to run on a *really* old embedded box, which runs Pythin 2.5.something.
# Rather than attemptiong to grab and install bottle using pip, setup_tools, etc
# am saving locally and importing from there.

from lib.bottle import route, run, template, request, get, post
from lib.shortuuid import uuid

# OK, so python2.5 doesn't come with json OOTB, so add simplejson
import lib.simplejson

import socket

# Seems the FoxBoard doesn't like this.
# socket.gaierror: (7, 'no address associated with hostname.')
# Guess CrisOS (very old OpenWRT fork) doesn't assign an address in the same way.
# Until I work out a fix, set manually
local_ip = "10.200.1.46"
#local_ip = socket.gethostbyname(socket.gethostname())

# I'm using SMSD to send/receive SMS alerts.
# It uses a series of directories as static queues to send and store messages.
# Where the SMS queues are located.
outbound_queue_path = "/var/spool/sms/outgoing/"
inbound_queue_path = "/var/spool/sms/incoming/"


def rand_fname(suffix):
    # Generate a random filename using the shortuuid lib
    fname = 'sms-' + ''.join(uuid() + '-' + suffix + '.smsmsg')
    return fname

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

# Grabs the data in the inbound JSON message,
# extracts the number and body and dumps to disk
# in correct format for SMSD to hoover up.
@route('/sendsms', method='PUT')
def send_sms():
    recipient = request.json['recipient']
    body = request.json['body']
    file_name = rand_fname("alert")
    outbound_path = outbound_queue_path + file_name
    print "Outbound Path: " + outbound_path

    if not recipient:
        abort(400, 'No Recipient Defined')

    if not body:
        abort(400, 'No Message Body Defined')

    try:
        #return {"recipient": recipient, "body": body}
        sms_message = open(outbound_path, 'w')
        print recipient
        print body
        sms_message.write("To: " + str(recipient) + '\n\n')
        sms_message.write(body + '\n')
        sms_message.close()

    except:
        print ("epic fail")


run(host=local_ip, port=8080)
