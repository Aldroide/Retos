Sec0 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
Sec1 = ["P1", "P1", "P2", "P2", "P1", "P2", "P2", "P2"]
sec2 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P2", "P1"]
sec3 = ["P1", "P1"]


def juego(secuencia):
    game = ["Love", "15", "30", "40"]
    fin = False
    error = False
    P1 = 0
    P2 = 0

    lon = len(secuencia)
    for i in range(0, (lon)):
        error = fin
        P1 += 1 if secuencia[i] == "P1" else 0
        P2 += 1 if secuencia[i] == "P2" else 0

        if P1 >= 3 and P2 >= 3:
            if not fin and abs(P1-P2) <= 1:
                print("Deuce" if P1 == P2 else
                      "Ventaja P1"if P1 > P2 else "Ventaja P2")
            else:
                fin = True
        else:
            if P1 < 4 or P2 < 4:
                print(f"{game[P1]}-{game[P2]}")
            else:
                fin = True

    print("Puntos no validos"if error else
          "Ha ganado P1" if P1 > P2 else "Ha ganado P2")


juego(Sec0)
juego(Sec1)
juego(sec2)
juego(sec3)
