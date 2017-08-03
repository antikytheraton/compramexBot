Estado 10 "Presentación":
Mensaje: "Hola NOMBRE, buenos días"
Botón generico: texto: "Envía dinero a tus amigos de forma rápida y segura"("Enviar dinero", "Términos y condiciones", "Políticas de privacidad") 

#Estado 20 "Selección de operación"

#Estado 30 "Términos y condiciones"

#Estado 40 "Políticas de privacidad"

#Estado 50 "Enviar dinero":

Estado 60 "Datos del beneficiario":
Mensaje: "NOMBRE, para darte mayor seguridad, necesitamos validar algunos datos"
Mensaje: "¿Cuál es el nombre completo de la persona a la que enviaras?"

Estado 80 "Seleccionar beneficiarios frecuentes":
Mensaje: "¿Deseas seleccionar a un beneficiario de tu lista de envíos?"
Botón generico carrusel: texto: "CONTACT" ("Seleccionar", "Borrar")

Estado 90 "Monto":	
Respuesta rápida: texto: "¿Cuánto quieres enviarle? a NOMBRE_RECEPTOR" ("$200", "$500", "$1000")

#Estado 100 "Leer monto":

Estado 110 "Datos del usuario"
Mensaje: "Hola NOMBRE, para brindarte mayor seguridad en tu envío, ¿me podrías confirmar tu nombre completo?"

Estado 120 "Leer datos del usuario": 
Respuesta rápida: texto: "NOMBRE, me ayudas a confirmar que tu fecha de nacimiento es FECHA" ("Si", "No")

Estado 121 "Corregir fecha de nacimiento"
Mensaje: "NOMBRE, me ayudas a ingresar tu fecha de nacimiento con el siguiente formato dd/mm/aaaa"

#Estado 122 "Leer fecha de nacimiento"

Estado 130 "Domicilio usuario":
Mensaje: "Para darte mayor seguridad, ¿podrías por favor proporcionarme los datos de tu domicilio?"

Estado 140 "Leer domicilio usuario":
Mensaje: "Ahora tu código postal por favor"

Estado 150 "Confirmar datos beneficiario, monto, usuario":
Mensaje: "Gracias NOMBRE, elegiste enviar CANTIDAD a NOMBRE_RECEPTOR"
Mensaje: "El costo total de tu envío, incluyendo comisión e IVA es de CANTIDAD_FINAL"
Respuesta rápida: texto: "NOMBRE, ¿estás de acuerdo?" ("Si", "No")

Estado 160 "Lista negra":
Mensaje: "Lo siento, no puedo procesar su envío, por favor acuda a una sucursal"

Estado 170 "Notificación activación de código":
Mensaje: "NOMBRE, tu código de envío ha sido activado con éxito"

Estado 180 "Generar ticket":
Mensaje: "NOMBRE, este es tu código de envío"
Imagen: código generado

Estado 190 "Econtrar sucursales cercanas":
Respuesta rápida: texto: "¿Quieres que te muestre las sucursales más cercanas" ("Enviar ubicación", "No enviar")

#Estado 200: "Leer ubicación":

Estado 210 "Mapa sucursales cercanas":
Mensaje: "Actívalo en la sucursal Elecktra o Banco Azteca más cerca de ti"
Mensaje: "También puedes activarlo con alguno de nuestros socios.\nFarmacias del ahorro, Tiendas Neto, Presta Prenda"
Mensaje: "¿Tienes alguna duda?"
Butón generico llamada: texto: "LLámanos o escríbenos un correo electrónico" ("Llamar", "Escribir correo")

Estado 220 "Mapa sucursales cercanas":
Mensaje: "Actívalo en la sucursal Elecktra o Banco Azteca más cercana a ti"
Botón generico ruta: Mapa, Nombre sucursal, Dirección
Mensaje: "También puedes activarlo con alguno de nuestros socios.\nFarmacias del ahorro, Tiendas Neto, Presta Prenda"
Mensaje: "¿Tienes alguna duda?"
Botón generico llamada: texto: "LLámanos o escríbenos un correo electrónico" ("Llamar", "Escribir correo")

#Estado 230 "Notificación estado de operación"

Estado 231 "Operación exitosa":
Mensaje: "Hola NOMBRE, te informo que NOMBRE acaba de cobrar el envío"

Estado 232 "Operación cancelada":
Mensaje: "Hola NOMBRE, te informo que tu envío fue cancelado"

Estado 233 "Código expirado":
Mensaje: "Hola NOMBRE, te informo que tu código de envío expiro"

Estado 240 "Modificar datos":
Botón generico datos: texto: "NOMBRE, ¿deseas realizar alguna modificación en los datos que ingresaste?" ("Confirmar datos", "Cancelar envío", "Reiniciar bot")

Estado 250 "Reiniciar bot":
Mensaje: "Se ha reiniciado tu usuario"

Estado 260 "Cancelar envío":
Mensaje: "Se ha cancelado el envío"

