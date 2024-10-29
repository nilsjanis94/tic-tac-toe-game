# Aufgabe 2
# 2.1 Suche im Internet nach der Methode .join() und erkläre im Detail was diese macht
# 2.2 Schreibe eine Funktion mit dem Namen zeichne Spielfeld mit einer for Schleife, die jede Liste deiner List Comprehension untereinander ausgibt
# 2.3 Benutze die join Methode, um die Listen mit einem " | " Zeichen miteinander zu verbinden und gebe sie in der Console aus.
# 2.4 füge jeder Liste in einer Reihe einen Boden mit "-" hinzu und gebe dein Spielfeld in der Console aus. (Tipp: 9 Trennstriche sehen gut und symmetrisch aus)
# Dein Ergebnis sollte etwa wie folgt aussehen:
#
#  |   |
#---------
#  |   |
#---------
#  |   |
#---------

from aufgabe_1 import spielfeld

def zeichne_spielfeld(spielfeld):

    for row in spielfeld:
        print(" | ".join(row))
        print("---------")
