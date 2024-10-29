# Aufgabe 3
# 3.1 Baue eine Hauptfunktion mit dem Namen starte_spiel(), kopiere deine List Comprehension mit deinem
#     Spielfeld in die Funktion, so das dein Spielfeld bei dem Aufruf der Funktion erstellt wird
# 3.2 Definiere eine Variable mit dem Namen aktueller_spieler => 'X' in deiner Funkion
# 3.3 Baue eine While Schleife, in deiner starte_spiel() Funktion, die bei dem Start der Schleife
#     deine Funktion zeichne_spielfeld aufruft. (TIPP: Vergiss nicht die Parameterübergabe)
# 3.4 Fordere innerhalb deiner While Schleife eine Eingabe an, welche die Zeile mit einer Zahl empfängt und speichere den Wert der
#     Eingabe in der Variable zeile. Dieser Wert wird später auf den Index deines Feldes zugreifen
# 3.5 Fordere innerhalb deiner While Schleife eine weitere Eingabe an, welche die Spalte mit einem Zahlenwert empfängt, die später dem Index der
#     Spalte zugewiesen wird und speichere den Wert der Eingabe in einer Variablen mit dem Namen spalte
#      (TIPP: Aus der Kombination deiner Eingabe ergeben sich später die Indizes und somit die Stelle an der deine Wahl platziert wird)

from aufgabe_1 import spielfeld
from aufgabe_2 import zeichne_spielfeld

def starte_spiel():
    Spielfeld = [[ ' ' for _ in range(3)] for _ in range(3)]
    aktueller_spieler = 'X'
    while True:
        zeichne_spielfeld(Spielfeld)
        zeile = int(input("Gib eine Reihe ein (1-3): ")) - 1
        spalte = int(input("Gib eine Spalte ein (1-3): ")) - 1
        Spielfeld[zeile][spalte] = aktueller_spieler
        ...
        
starte_spiel()