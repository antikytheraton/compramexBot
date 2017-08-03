#from apiSalinas import salinasApi
#from maquina.nombres import NombresDiv
#from maquina.fecha import diaDi
from replies_bot import RepliesBot

class User:
    sender_id = ''
    name_facebook = ''
    last_name_facebook_ = ''
    state = 10
        
class MaquinaEstados(object):
    baseUrl = "http://localhost:8080"
    
    def __init__(self, bot, user):
        self.replies_bot = RepliesBot(bot)
        self.user = user
        self.functions = {
            10: self.estado10,
            20: self.estado20,
            30: self.estado30,
            40: self.estado40,
            50: self.estado50,
            60: self.estado60,
            70: self.estado70,
            80: self.estado80,
            90: self.estado90,
            100: self.estado100,
            110: self.estado110,
            120: self.estado120,
            121: self.estado121,
            130: self.estado130,
            140: self.estado140,
            150: self.estado150,
            160: self.estado160,
            170: self.estado170,
            180: self.estado180,
            190: self.estado190,
            200: self.estado200,
            210: self.estado210,
            220: self.estado220,
            230: self.estado230,
            231: self.estado231,
            232: self.estado232,
            233: self.estado233,
            240: self.estado240,
            250: self.estado250,
            260: self.estado260,
        }

    def find_state(self, estado, payload):
        self.functions[estado](payload)
    
    # Presentacion
    def estado10(self, payload):
        print("Estado Inicial")
        if payload['message'].get('text'):
            if payload['message']['text'] == 'Hola':
                self.replies_bot.state_10(self.user.sender_id, self.user.name_facebook)
                #guardar estado 20 en base de dato


    # Seleccion de operacion
    def estado20(self, payload):
        print("Estado 20")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(50,payload)
        elif estado == 2:
            self.findStep(30, payload)
        elif estado == 3:
            self.findStep(40, payload)
        else:
            self.findStep(20, 1)

    # Terminos y condiciones
    def estado30(self, payload):
        print("Estado 30")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(20, payload)
        else:
            self.findStep(30, payload)

    # Poiticas de privacidad
    def estado40(self, payload):
        print("Estado 40")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(20, payload)
        else:
            self.findStep(40, 1)

    # Enviar dinero
    def estado50(self, payload):
         """
        -Conexion al servicio de validacion de usuario
        -Verificar en la base de datos si el usuario
        ya se encuentra registrado
            Si es True, ir a estado 70
            Si es False, ir a estado 60
        """
        print("Estado 50")
        # respuesta = salinasApi.peticiones.")ClientValida(baseUrl)
        # print(respuesta)
        # respuesta = str(respuesta)
        respuesta = "True"

        if respuesta.find("True"):
            self.findStep(70, payload)
        elif respuesta.find("False"):
            self.findStep(60, payload)
        else:
            self.findStep(50, 1)

    # Datos del beneficiario
    def estado60(self, payload):
    """
    Algoritmo de reconocimiento de nombres
    """
        print("Estado 60")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(90, payload)
        else:
            self.findStep(60, 1)

    # Elegir beneficiario
    def estado70(self, payload):
    """
    Preguntar al usuario si quiere elegir de entre sus beneficiarios
    guardados
        Si es "Si", ir a estado 80
        Si es "No", ir a estado 60
    """
        print("Estado 70")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(60, payload)
        elif estado == 2:
            self.findStep(80, payload)
        else:
            self.findStep(70, payload)

    # Seleccionar beneficiarios frecuentes
    def estado80(self, payload):
        """
        Carrusel de beneficiarios guardados
        """
        print("Estado 80")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(90, payload)
        else:
            self.findStep(80, payload)

    #Monto
    def estado90(self, payload):
        print("Estado 90")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(100, payload)
        else:
            self.findStep(90, payload)

    #Leer monto    
    def estado100(self, payload):
        print("Estado 100")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(110, payload)
        else:
            self.findStep(100, payload)

    #Datos del usuario
    def estado110(self, payload):
        """
        Algoritmo de reconocimiento de nombres
        """        
        print("Estado 110")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(120, payload)
        else:
            self.findStep(110, payload)

    # Fecha de nacimiento del usuario
    def estado120(self, payload):
        """
        Algoritmo para reconocimiento de fecha de nacimiento
        """
        print("Estado 120")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(121, payload)
        elif estado == 2:
            self.findStep(130, payload)
        else:
            self.findStep(120, 1)

    # Corregir fecha de nacimiento
    def estado121(self, payload):
        """
        Reconocer fecha en formato dd/mm/aaaa
        """
        print("Estado 121")
        estado = int(input())
        payload = input()
        if estado == 2:
            self.findStep(130, payload)
        else:
            self.findStep(121, payload)

    # Domicilio del usuario
    def estado130(self, payload):
        """
        Algoritmo de reconocimiento de direccion
        """
        print("Estado 130")
        estado = 1
        nombre = input()
        apPaterno = input()
        apMaterno = input()
        fechaNacimientoCte = input()

        nombre_full = self.filters.SplitNombres(payload.nombre)
        fecha_fix = self.filters.Splitdia(payload.fecha)

        if estado == 1:
            domicilio = {"calle 7 num 9 col mexico"}
            #self.estado140(estado, nombre, apPaterno, apMaterno, fechaNacimientoCte)
            if payload['message'].get('text'):
                if payload['message']['text'] == domicilio:
                    self.replies_bot.state_130(self.user.sender_id, self.user.name_facebook)
                    #guardar estado 140 en base de dato
        else:
            self.findStep(130, 1)

    # Leer Codigo Postal del usuario
    def estado140(self, payload):
        """
        -Preguntar al servicio si el usuario se encuentra
        en la lista negra:
            Si es True, pasar al estado 160
            Si es False, pasar al 150
        """
        print("Estado 140")
        codigo_postal = {93939}
        if payload['message'].get('text'):
                if payload['message']['text'] == codigo_postal:
                    self.replies_bot.state_140(self.user.sender_id, self.user.name_facebook)
                    # respuesta = salinasApi.peticiones.ClientValida(baseUrl, nombre, apPaterno, apMaterno, fechaNacimientoCte)
                    # TODO ADD MOCKING
                    #guardar estado 150 en base de dato

            
        respuesta = "(True,Respuesta Exitosa)"
        print(respuesta)
        respuesta = str(respuesta)

        if respuesta.find("True"):
            self.findStep(150, payload)
        elif respuesta.find("False"):
            self.findStep(160, payload)
        else:
            self.findStep(140, 1)

    #Confirmar datos
    def estado150(self, payload):
        """
        Preguntar al usuario si quiere confirmar los datos que ingreso

            Si el usuario esta "de acuerdo", Guardar datos en la
            base de datos y conectar con el servicio de activacion
            de codigo. Pasar al estado 170.

            Si el usuario no esta deacuerdo, ir a estado 240
        """        
        print("Estado 150")

        # respuesta = salinasApi.peticiones.generaEnvio(baseUrl)
        # TODO ADD MOCKING
        payload = input()
        respuesta = "(True,Respuesta Exitosa)"
        print(respuesta)
        respuesta = str(respuesta)

        if respuesta.find("True"):
            self.findStep(170, payload)
        elif respuesta.find("False"):
            self.findStep(140, payload)
        else:
            self.findStep(150, 1)

    # Lista Negra
    def estado160(self, payload):
        """
        Este es un estado final
        """
        print("Estado 160")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(10, payload)
        else:
            self.findStep(160, 1)

    # Notificacion activacion de codigo
    def estado170(self, payload):
        print("Estado 170")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(180, payload)
        else:
            self.findStep(170, 1)

    # Generar ticket
    def estado180(self, payload):
        """
        Generar imagen del ticket
        """
        print("Estado 180")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(190, payload)
        else:
            self.findStep(180, payload)

    # Encontrar sucursales cercanas
    def estado190(self, payload):
        """
        -Opcion compartir ubicacion del usuario
            Si "compartir ubicacion", ir a estado 200
            Si "no compartir", ir a estado 210
        """
        print("Estado 190")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(210, payload)
        elif estado == 2:
            self.findStep(200, payload)
        else:
            self.findStep(190, 1)

    # Enviar ubicacion
    def estado200(self, payload):
        """
        -Conectar con el servicio de ubicacion de sucursales
        """
        print("Estado 200")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(220, payload)
        else:
            self.findStep(200, 1)

    # Informacion sucursales
    def estado210(self, payload):
        print("Estado 210")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(230, payload)
        else:
            self.findStep(210, 1)

    # Mapa sucursales cercanas
    def estado220(self, payload):
        print("Estado 220")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(230, payload)
        else:
            self.findStep(220, 1)

    # Notificacion estado de operacion
    def estado230(self, payload):
        """
        Este  estado se dispara cuando el servicio de "Confirmacion
        de retiro" envia el estado de la operacion
        """
        print("Estado 230")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(231, payload)
        elif estado == 2:
            self.findStep(221, payload)
        elif estado == 3:
            self.findStep(233, payload)
        else:
            self.findStep(230, 1)

    # Operacion exitosa
    def estado231(self, payload):
        print("Estado 231")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(10, payload)
        else:
            self.findStep(231, 1)
    
    # Operacion cancelada
    def estado232(self, payload):
        print("Estado 232")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(10, payload)
        else:
            self.findStep(232, 1)

    # Codigo expirado
    def estado233(self, payload):
        print("Estado 233")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(10, payload)
        else:
            self.findStep(233, 1)

    # Modificar datos
    def estado240(self, payload):
        """
        Mostrar al usuario un menu con tres opciones
            -confirmar
            -cancelar
            -reiniciar bot

            Si "confirmar", ir a estado 150
            Si "cancelar", ir a estado 260
            Si "reiniciar bot", ir a estado 250
        """
        print("Estado 240")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(150, payload)
        elif estado == 2:
            self.findStep(260, payload)
        elif estado == 3:
            self.findStep(250, payload)
        else:
            self.findStep(240, 1)

    # Reiniciar bot
    def estado250(self, payload):
        """
        Borrar datos almacenados en la base de datos del la sesion
        """
        print("Estado 250")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(10, payload)
        else:
            self.findStep(250, 1)

    # Cancelar envio
    def estado260(self, payload):
        print("Estado 260")
        estado = int(input())
        payload = input()
        if estado == 1:
            self.findStep(10, payload)
        else:
            self.findStep(260, 1)