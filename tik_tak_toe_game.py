"""
Konstante Variablen für das Tic-Tac-Toe-Spiel.
"""
BOARD_SIZE = 3
PLAYER_X = 'X'
PLAYER_O = 'O'

def starte_spiel():
    """
    Startet das Tic-Tac-Toe-Spiel und verwaltet den Spielablauf.
    """
    spielfeld = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    aktueller_spieler = PLAYER_X

    while True:
        zeichne_spielfeld(spielfeld)
        print(f"{aktueller_spieler} ist an der Reihe")
        
        zeile, spalte = get_player_input()

        if spielfeld[zeile][spalte] != ' ':
            print("Feld bereits besetzt! Bitte wähle ein anderes Feld.")
            continue

        spielfeld[zeile][spalte] = aktueller_spieler

        if gewonnen(spielfeld, aktueller_spieler):
            zeichne_spielfeld(spielfeld)
            print(f"Spieler {aktueller_spieler} hat gewonnen!")
            break
        
        if draw(spielfeld):
            zeichne_spielfeld(spielfeld)
            print("Unentschieden!")
            break

        aktueller_spieler = PLAYER_O if aktueller_spieler == PLAYER_X else PLAYER_X

def get_player_input():
    """
    Fordert den Spieler auf, eine gültige Zeile und Spalte einzugeben.
    """
    while True:
        try:
            zeile = int(input("Gib eine Reihe ein (1-3): ")) - 1
            spalte = int(input("Gib eine Spalte ein (1-3): ")) - 1
            if 0 <= zeile < BOARD_SIZE and 0 <= spalte < BOARD_SIZE:
                return zeile, spalte
            else:
                print("Falsche Eingabe! Bitte wähle eine Reihe und Spalte zwischen 1 und 3.")
        except ValueError:
            print("Ungültige Eingabe! Bitte gib eine Zahl ein.")

def zeichne_spielfeld(spielfeld):
    """
    Zeichnet das aktuelle Spielfeld.
    """
    print("    1   2   3")
    print(" --------------")
    for i, reihe in enumerate(spielfeld):
        print(f"{i+1} | {' | '.join(reihe)} |")
        print(" --------------")

def gewonnen(spielfeld, spieler):
    """
    Überprüft, ob der angegebene Spieler gewonnen hat.
    """
    for reihe in spielfeld:
        if all(zelle == spieler for zelle in reihe):
            return True

    for spalte in range(BOARD_SIZE):
        if all(spielfeld[reihe][spalte] == spieler for reihe in range(BOARD_SIZE)):
            return True

    if all(spielfeld[i][i] == spieler for i in range(BOARD_SIZE)):
        return True

    if all(spielfeld[i][BOARD_SIZE-1-i] == spieler for i in range(BOARD_SIZE)):
        return True

    return False

def draw(spielfeld):
    """
    Überprüft, ob das Spiel unentschieden ist.
    """
    for reihe in spielfeld:
        for zelle in reihe:
            if zelle == ' ':
                return False
    return True

starte_spiel()