#Para probar puedes usar estos datos, te tiene que dar un vector de 18

# topicos = ['pollo cocido', 'dinero']
# acciones = ['enviar', 'recibir', 'comprar']
# unes = ['un', 'una', 'unos cuantos']
# valores = [topicos, acciones, unes]
#
# huecos = ['TOPICO', 'ACCION', 'UN']
#
# title_tags = ['tpc', 'acc', 'uns']
#
# frase="Como le hago para ACCION UN TOPICO nuevo"

def aumentar_data_set_tags(frase, huecos, valores, tags):
    list_frase = frase.split(' ')
    resultado = []
    resultado_tags = []

    list_aux = list(list_frase)
    list_aux_tags = list('*'*len(list_aux))

    for i in range(len(huecos)):
        if i == 0:
            try:
                index = list_aux.index(huecos[i])
                for valor in valores[i]:
                    if (' ' in valor) == True:
                        list_aux_original = list(list_aux)
                        del list_aux[index]
                        list_aux = list_aux[:index]+valor.split(' ')+list_aux[index:]
                        resultado.append(list(list_aux))
                        list_aux = list(list_aux_original)

                        list_aux_tags_original = list(list_aux_tags)
                        for index_palabra_oracion in range(len(valor.split(' '))):
                            list_aux_tags = list_aux_tags[:index] + [tags[i]] + list_aux_tags[index:]
                        del list_aux_tags[(index + len(valor.split(' '))):(index + len(valor.split(' ')) * 2-1)]
                        resultado_tags.append(list(list_aux_tags))
                        list_aux_tags = list(list_aux_tags_original)

                    else:
                        list_aux[index] = valor
                        resultado.append(list(list_aux))

                        list_aux_tags[index] = tags[i]
                        resultado_tags.append(list(list_aux_tags))
            except:
                resultado.append(list(list_aux))
                resultado_tags.append(list(list_aux_tags))
                continue
        else:
            list_aux = list(resultado)
            resultado.clear()

            list_aux_tags = list(resultado_tags)
            resultado_tags.clear()

            for j in range(len(list_aux)):
                try:
                    index = list_aux[j].index(huecos[i])
                    for valor in valores[i]:
                        if (' ' in valor) == True:
                            list_aux_original = list(list_aux[j])
                            del list_aux[j][index]
                            list_aux[j] = list_aux[j][:index] + valor.split(' ') + list_aux[j][index:]
                            resultado.append(list(list_aux[j]))
                            list_aux[j] = list_aux_original

                            list_aux_tags_original = list(list_aux_tags[j])
                            for index_palabra_oracion in range(len(valor.split(' '))):
                                list_aux_tags[j] = list_aux_tags[j][:index] + [tags[i]] + list_aux_tags[j][index:]
                            del list_aux_tags[j][(index + len(valor.split(' '))):(index + len(valor.split(' ')) * 2-1)]
                            resultado_tags.append(list(list_aux_tags[j]))
                            list_aux_tags[j] = list(list_aux_tags_original)
                        else:
                            list_aux[j][index] = valor
                            resultado.append(list(list_aux[j]))

                            list_aux_tags[j][index] = tags[i]
                            resultado_tags.append(list(list_aux_tags[j]))
                except:
                    resultado.extend(list(list_aux))
                    resultado_tags.extend(list(list_aux_tags))
                    break
    return resultado, resultado_tags

# print(aumentar_data_set_tags(frase, huecos, valores, title_tags)[0])
# print(len(aumentar_data_set_tags(frase, huecos, valores, title_tags)[0]))
#
# print(aumentar_data_set_tags(frase, huecos, valores, title_tags)[1])
# print(len(aumentar_data_set_tags(frase, huecos, valores, title_tags)[1]))