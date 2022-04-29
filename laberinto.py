def laberinto(matriz, x, y, rutas=[]):
    """Salida del laberinto."""
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            rutas.append([x, y])
            print("Saliste del laberinto")
            print(rutas)
            rutas.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            rutas.append([x, y])
            # print("mover hacia el  este")
            laberinto(matriz, x, y+1, rutas)
            # print("mover hacia el oeste")
            laberinto(matriz, x, y-1, rutas)
            # print("mover hacia el norte")
            laberinto(matriz, x-1, y, rutas)
            # print("mover hacia el sur")
            laberinto(matriz, x+1, y, rutas)
            rutas.pop()
            matriz[x][y] = 1


lab = [[1, 1, 1, 1, 1, 1, 1],
       [0, 1, 0, 1, 1, 0, 1],
       [0, 1, 0, 0, 1, 0, 1],
       [1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 2]]

lab2 = [[1,1,0,1],
        [0,1,0,0],
        [0,1,1,2]]

laberinto(lab2, 0, 0)