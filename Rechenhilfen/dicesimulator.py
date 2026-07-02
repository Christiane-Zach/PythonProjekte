from random import randint

def wurf_simulator(anzahl: int) -> list:
    würfe = []
    for _ in range(0, anzahl):
        würfe.append(randint(1,6))
    return würfe

def mittelwert(liste: list) -> float:
    return sum(liste) / len(liste)

