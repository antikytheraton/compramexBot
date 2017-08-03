"""Clase que te ayuda a 'inflar' tu dataset"""
import unicodedata
import pandas as pd
# from preparacion_dataset.aumenta_datos import aumentar_data_set
# from preparacion_dataset.aumentar_datos_tags import aumentar_data_set_tags
from aumenta_datos import aumentar_data_set
from aumentar_datos_tags import aumentar_data_set_tags

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

#Declaración de los parámetros para inflar nuestro dataset
#Frase: Es la frase base donde los campos que queremos sustituir están en mayúsculas
#Hueco: Es el campo que queremos sustituir, recuerda que debe de ir en mayúscula
#Valores: Son los valores con los que quieres sustituir los huecos
#IMPORTANTE: el orden de arreglo de valores, y de huecos deben de coincidir.
#IMPORTANTE: el tamaño de tags, de huecos y de la primera dimensión de valores debe de ser igual

deseos = ['quiero', 'deseo', 'anhelo', 'ocupo', 'busco', 'necesito', 'debo']
comprares = ['comprar', 'adquirir', 'conseguir', 'ubicar', 'obtener'] #si agregas aquí, deberías agregar en la variable compro
unos = ['un', 'unos', 'una', 'unas']
productos = ['auto', 'autos', 'lavadora','lavadoras', 'mueble','muebles', 'computadora','computadoras', 'laptop', 'laptops']
dondes = ['donde', 'en donde']
ayudas = ['ayuda', 'asistencia', 'atención', 'apoyo']
compro = ['compro', 'adquiero', 'consigo', 'ubico', 'obtengo']

valores = [deseos, comprares, unos, productos, dondes, ayudas, compro]

huecos = ['DESEO', 'COMPRAR', 'UNO', 'PRODUCTO', 'DONDE', 'AYUDA', 'COMPRO']

title_tags = ['dseo', 'cmpr', 'uno', 'pdcto', 'dnde', 'ayda', 'cmpo']

frases = []
numeros_intencion = []

res_frases = []
res_tags = []
#En este caso las frases a inflar las sacamos de un archivo txt
#Las frases infladas se guardan en 'frases' y sus número de intencion en 'numeros_intencion'
file = open("../trainingFAQs.txt", 'r')
for linea in file.readlines():
    frase = linea
    frase = frase.replace('?', '').replace('¿', '').replace('\n', '')
    frase = elimina_tildes(frase)
    numero_intencion = frase[0]#Se extrae el número de intención
    frase_sin_numero = frase[2:]#Se quita el número de intención
    frases.append(list(aumentar_data_set(frase_sin_numero, huecos, valores)))
    numeros_intencion.append(numero_intencion*len(aumentar_data_set(frase_sin_numero, huecos, valores)))

    frasesTags, tags = aumentar_data_set_tags(frase_sin_numero, huecos, valores, title_tags)
    res_frases.append(frasesTags)
    res_tags.append(tags)
file.close()

##########----INTENCIONES----##########
#Se ingresa el numero de intencion con la frase inflada correspondiente, y se escribe a otro txt
numeros_intencion = ''.join(numeros_intencion)
file = open("./data_final_inflado_intencion.txt", 'w')
index_numeros_intencion=0
for oraciones in frases:
    for palabra in oraciones:
        oracion = " ".join(str(x) for x in palabra)
        file.write(numeros_intencion[index_numeros_intencion]+' '+oracion)
        file.write('\n')
        index_numeros_intencion+=1
file.close()

#########----TAGS----###########
#Se ponen los tags y las frases dentro de sus listas correspondientes, para bajarlas a una sola dimensión
lista_frases_unida = []
lista_tags_unida = []

for frase_base in res_frases:
    for oraciones in frase_base:
        lista_frases_unida.extend(['-', '-', '-']+oraciones+['-', '-', '-'])

for frase_base in res_tags:
    for oraciones in frase_base:
        lista_tags_unida.extend(['-', '-', '-']+oraciones+['-', '-', '-'])

labels=["tags","words"]
df=pd.DataFrame.from_records(zip(lista_tags_unida,lista_frases_unida),columns=labels)
df.to_csv("data_final_inflado_tag.csv", sep=',')
