import statistics as st

#grupo = [90,94,53,68,79,84,87,72,70,69,65,89,85,83,72]
grupo = [283.6,269.4,262.2,261.1,246.7,245.5,239.2,233.7,230.3,227.9,226.4,225.5,224.1,223.6,222.3,221.4,217.8,217.2,216.9,211.6,211.4,208.5,204.9,202.7,202,200.5,198.5,182.4,111]
paises = [0.16,0.20,0.06,0.06,0.07,0.17,0.06,0.22]

def encontrar_numero_cercano(numero, lista):
    numero_cercano = lista[0]
    indice_cercano = 0
    diferencia_minima = abs(numero - numero_cercano) 

    for i in range(1,len(lista)):
        diferencia_actual = abs(numero - lista[i])
        if diferencia_actual < diferencia_minima:
            numero_cercano = lista[i]
            indice_cercano = i
            diferencia_minima = diferencia_actual
    return numero_cercano, indice_cercano

def caja_bigotes(grupo):
    grupo = sorted(grupo)
    tamanio = len(grupo)
    print("El grupo es: ", grupo ,"y su tamaño es: ", tamanio)

    Q2 = st.median(grupo)
    indice = 0
    for i in grupo:
        indice = indice + 1
        if i == Q2:
            #print(f"El índice es {indice}")
            break
    #numero_cercano_media, indice_datos_centralizado = encontrar_numero_cercano(Q2, grupo)
    #print(f"numero_cercano_media {numero_cercano_media}, indice_datos_centralizado {indice_datos_centralizado}")
    indice = indice
    print(f"La mediana del grupo es {Q2} y su indice es {indice}")
    #media: 
    media = sum(grupo)/tamanio
    print(f"Esta es la media {media}")
    moda = st.mode(grupo)
    print(f"Esta es la media {moda}")


    grupo2  = []
    for i in grupo:
        if i < Q2:
            grupo2.append(i) 

    print(grupo2)
    Q1 = st.median(grupo2)
    print(f"La mediana del grupo2 es {Q1}")

    grupo3  = []
    for i in grupo:
            if i > Q2:
                grupo3.append(i) 

    print(grupo3)
    Q3 = st.median(grupo3)
    print(f"La mediana del grupo3 es {Q3}")

    valor_minimo = min(grupo)
    valor_maximo = max(grupo)

    print(f"El valor minimo del grupo completo es: {valor_minimo} y el valor maximo es {valor_maximo}")

    #Verificando si hay valores atípicos: 
    RI = Q3 - Q1 #Rango Intercuartilico
    BS = Q3 + 1.5 * RI #Barrera superior
    BI = Q1 - 1.5 * RI #Barrera inferior

    print(f"Se consideran valores atípicos los numeros que sea menor o igual a {BI} o mayor o igual a {BS}")

    Valores_BS = []
    Valores_BI = []
    for i in grupo:
         if i >= BS:
              Valores_BS.append(i)

    for i in grupo:
         if i <= BI:
              Valores_BI.append(i)

    print(f"Los valores atípicos de la que son menores o iguales a la barrera inferior son {Valores_BI} y los atípicos mayores o iguales a la barrera superior son: {Valores_BS}")

    #Asimetria
    As = round((Q1 + Q3 - ( 2 * Q2))/Q3-Q1,2)

    if As < 0:
         print(f"El valor de la asimetría es: {As}, y es una asimetría es negativa")
    elif As > 0:
        print(f"El valor de la asimetría es: {As}, y es una asimetría es positiva")
    else:
         print(f"Es simétrico {As}")



#caja_bigotes(grupo)
caja_bigotes(paises)