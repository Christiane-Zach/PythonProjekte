from random import randint
import streamlit as st
import warnings
import sys

zuweisung = {1: "Schere", 2: "Stein", 3: "Papier", 4: "Brunnen"}

def computer_eingabe():
    """Der Computer wählt eine zufällige Zahl von 1 bis 4"""
    return randint(1,4)

def spieler_gewinnt():
    """Der Spieler bekommt einen Gewinn gutgeschrieben"""
    st.write("Hurra! Du hast gewonnen!")
    return 1,0

def computer_gewinnt():
    """Dem Computer wird ein Gewinn gutgeschrieben """
    st.write("Oh nein! Der Computer hat gewonnen :-(")
    return 0,1

def fehler_aufgetreten():
    """Fehlermeldung"""
    st.write("Ein Fehler ist aufgetreten.")
    return 0,0

def find_the_winner(spieler_num: int, computer_num: int):
    """Gewinnt der Spieler oder der Computer nach den Schere-Stein-Papier-Regeln"""
    if spieler_num == computer_num:
        st.write("Es ist unentschieden!")
        return 0,0
    elif spieler_num == 1:
        if computer_num in [2,4]:
            return computer_gewinnt()
        elif computer_num == 3:
            return spieler_gewinnt()
        else:
            return fehler_aufgetreten()
    elif spieler_num == 2:
        if computer_num == 1:
            return spieler_gewinnt()
        elif computer_num in [3,4]:
            return computer_gewinnt()
        else:
            fehler_aufgetreten()
    elif spieler_num == 3:
        if computer_num == 1:
            return computer_gewinnt()
        elif computer_num in [2,4]:
            return spieler_gewinnt()
        else:
            return fehler_aufgetreten()
    elif spieler_num == 4:
        if computer_num in [1,2]:
            return spieler_gewinnt()
        elif computer_num == 3:
            return computer_gewinnt()
        else:
            return fehler_aufgetreten()
    else:
        return fehler_aufgetreten()
    