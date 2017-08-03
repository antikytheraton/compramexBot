class RepliesBot(object):

	def __init__(self,bot):
		self.bot = bot
		self.buttons = {'state10':[{"type":"postback","title":"Quiero comprar!","payload": 30 }, 
						  {"type":"postback","title":"Ayuda","payload": 40 },],
			   'state210':[{"type":"phone_number","title":"Llamar","payload": "+525500000000" }], 
			   'state70':[{"type":"postback","title":"Seleccionar beneficiario","payload": 80 }, 
						  {"type":"postback","title":"Nuevo beneficiario","payload": 60 }],}
		self.replies = {'state90':[{"content_type":"text","title":"$200","payload":"200"}, 
						  {"content_type":"text","title":"$500","payload":"500"}, 
						  {"content_type":"text","title":"$1000","payload":"1000"}],
				'stateS/N':[{"content_type":"text","title":"Si","payload":"Si"}, 
						  {"content_type":"text","title":"No","payload":"No"}],
				'state190':[{"content_type":"location", "title":"Enviar"},
							{"content_type":"text","title":"No enviar","payload":"No"}]}

	def state_location(self,sender_id,coordinates):
		message = "Enviaste localización"
		self.bot.send_text_message(sender_id, message)

	def send_alert(self,sender_id, message):
		'''Alert'''
		self.bot.send_text_message(sender_id, message)

	def show_yes_no(self,sender_id, text):
		'''Verify names'''
		self.bot.send_quick_replies(sender_id,text,self.replies['stateS/N'])

	def state_10(self,sender_id, name):
		'''Presentación bot'''
		text = "Hola "+name+", soy el Bot de Compra-Mex ❤"
		self.bot.send_text_message(sender_id, text)
		message = "¿Qué deseas hacer?"
		self.bot.send_button_message(sender_id, message, self.buttons['state10'])

	def state_30(self,sender_id):
		text = "Dime que producto quieres comprar para mostrate tiendas 100% mexicanas"
		self.bot.send_text_message(sender_id,text)


	def state_40(self,sender_id):
		text = "Estadito 40 bb"
		self.bot.send_text_message(sender_id,text)