from replies_bot import RepliesBot
import states
from customModules.clasificador.ner.intent_trainer import create_pkl_intent, obtener_respuesta

class User:
    sender_id = ''
    name_facebook = ''
    last_name_facebook_ = ''

class MaquinaEstados(object):
    def __init__(self, bot, user):
        self.replies_bot = RepliesBot(bot)
        self.user = user
        self.functions = {
            10: self.estado10,
            20: self.estado20,
            30: self.estado30,
            40: self.estado40,
        }

    def find_state(self, estado, payload=None):
        if payload == None:
            self.functions[estado]()
        else:
            self.functions[estado](payload)

    def estado10(self, payload):
        if payload['message'].get('text'):
            if payload['message']['text'].upper() == 'HOLA':
                self.replies_bot.state_10(self.user.sender_id, self.user.name_facebook)
                states.overwriteState("states.txt",20)
            else:
                self.replies_bot.send_alert(self.user.sender_id,"Intenta con un hola.")
        else:
            self.replies_bot.send_alert(self.user.sender_id,"Intenta con un hola ;)")

    def estado20(self, payload):
        # print(payload['message'].get('text'))
        if payload.get('postback'):
            print(payload.get('postback'))
            if payload['postback']['payload'] == '30':
                self.find_state(30)
            elif payload['postback']['payload'] == '40':
                self.find_state(40)

        elif payload['message'].get('text'):
            frase = payload['message'].get('text')
            create_pkl_intent(frase) # Se genera el clasificador pkl
            clasif = obtener_respuesta(frase) # Se utiliza el clasificador para clasificar (duh!)
            if clasif == '0':
                self.replies_bot.send_alert(self.user.sender_id, "Comprar producto")
            elif clasif == '1':
                self.replies_bot.send_alert(self.user.sender_id, "Ubicar tienda")
            elif clasif == '2':
                self.replies_bot.send_alert(self.user.sender_id, "Ayuda")

        else:
            self.replies_bot.send_alert(self.user.sender_id, "Presiona una opción del recuadro anterior")

    def estado30(self):
        self.replies_bot.state_30(self.user.sender_id)
        states.overwriteState("states.txt",10)

    def estado40(self):
        self.replies_bot.state_40(self.user.sender_id)
