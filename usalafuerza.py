mochila = ["casco","cuchillo","linterna","sable de luz","comida","mapa"]

def usar_la_fuerza(mochila):# si encontro el sable de luz y la posicion
    if(len(mochila) == 0): #no encontro el sable de luz
        return False, 0
    elif(mochila[0] == "sable de luz"):
        return True, 0
    else:
        recursiva = usar_la_fuerza(mochila[1:])
        return recursiva[0], recursiva[1] +1

devolucion = usar_la_fuerza(mochila)
if(devolucion[0]):
    print("Se encontró el sable de luz dentro de la mochila y fue necesario sacar",devolucion[1],"objetos")
else:
    print("No se encontro el sable de luz en la mochila")
   
    


