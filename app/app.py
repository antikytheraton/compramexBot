from flask import Flask, request, send_from_directory
from pymessenger.bot import Bot
import requests
import json
import traceback
import random
import sys
import os
import states
from replies_bot import RepliesBot
from maquina_estados import User, MaquinaEstados

app = Flask(__name__)

ACCESS_TOKEN = ""
VERIFY_TOKEN = ""

bot = Bot(ACCESS_TOKEN)
user = User()
state_machine = MaquinaEstados(bot, user)

@app.route('/')
def home():
	return 'Incio del server del servidor'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	print("Llego solicitud")
	if request.method == 'POST':
		try:
			print ("POST executed")
			print (" ")
			output = request.get_json()
			print ("Entrada POST: " + str(output))
			print (" ")
			for event in output['entry']:
				messaging = event['messaging']

				for evtMessage in messaging:
					recipient_id = evtMessage['sender']['id']
					print ("USER_ID: " + recipient_id)

					load_client(recipient_id)
					state = get_state(user.sender_id)
					print(state)
					state_machine.find_state(state, evtMessage)

		except Exception:
			traceback.print_exc(file=sys.stdout)

	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		return "Verificar el token"

	return "Chatbot Grupo Salinas"

def get_public_data(idSender):
	try:
		# Obtiene datos publicos de usuario
		userResponse = requests.get('https://graph.facebook.com/v2.6/' + idSender + '?fields=first_name,last_name,profile_pic,locale,timezone,gender,is_payment_enabled&access_token=' + ACCESS_TOKEN)
		return json.loads(userResponse.text)
	except Exception:
		traceback.print_exc(file=sys.stdout)

def get_data_user(recipient_id):
	userTempData = get_public_data(recipient_id)
	data = {'name':'','last_name':''}
	if len(userTempData) > 0: #El usuario puede tener privado sus datos personales {}
		data['name'] = userTempData['first_name']
		data['last_name'] = userTempData['last_name']
	return data

def get_state(id):
	# global flagx
	#consulta el ultimo estado del usuario(id) en la base de datos
	state_user = states.readState("states.txt")

	print("STATE USER : "+str(state_user))
	return int(state_user)

def load_client(recipient_id):
	data = get_data_user(recipient_id)
	user.sender_id = recipient_id
	user.name_facebook = data['name']
	user.last_name_facebook = data['last_name']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
