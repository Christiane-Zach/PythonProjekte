import streamlit as st
import Spiele.board as b
import Spiele.KI as KI

st.header("Tic Tac Toe")

## alles bereit fürs Spiel ##
if "board" not in st.session_state:
    st.session_state.board = b.clear_board()
if "board_disabled" not in st.session_state:
    st.session_state.board_disabled = False
if "first_move" not in st.session_state:
    st.session_state.first_move = True
if "spieler" not in st.session_state:
    st.session_state.spieler = 0
if "computer" not in st.session_state:
    st.session_state.computer = 0

zeichen = ["X", "O"]
grad = st.pills("Schwierigkeitsstufe", ["leicht", "schwer"], default="leicht")

st.write(f"Du spielst als 1. und hast das Zeichen {zeichen[1]}")

## Spielfeld ##
### Der Spieler wird von dem Computer herausgefordert, der immer direkt nach ihm am Zug ist
### Der Computer muss wissen, ob es sich um den ersten Zug handelt und welche Schwierigkeitstufe gewählt wurde
### Außerdem müssen die Regeln für Tic Tac Toe eingehalten werden 
for row in range(len(st.session_state.board)):
    cols = st.columns(len(st.session_state.board[row]), gap="small")
    for col in range(len(st.session_state.board[row])):
        with cols[col]:
            if st.button(st.session_state.board[row][col], key=f"tic_tac_toe_{row}_{col}", use_container_width=True):
                if st.session_state.board[row][col] == "" and not st.session_state.board_disabled:
                    st.session_state.board[row][col] = zeichen[1]
                    if b.check_win_condition(zeichen[1], st.session_state.board) == 0:
                        st.session_state.board = KI.make_move(zeichen[0], grad, st.session_state.board, st.session_state.first_move)
                    if st.session_state.first_move:
                        st.session_state.first_move = False 
                    st.rerun() 

# Auswertung des Spiels und Anzeige der Punkte
_, mitte, _ = st.columns(3)

with mitte:
    st.write("")
    st.write("")
    
    spieler = b.check_win_condition(zeichen[1], st.session_state.board)
    computer = b.check_win_condition(zeichen[0], st.session_state.board)
    if spieler + computer > 0 and not st.session_state.board_disabled:
        if spieler == 1:
            st.write("Du hast gewonnen!!")
        if computer == 1:
            st.write("Schade! Der Computer hat gewonnen")
        if spieler == 2:
            st.write("Es ist unentschieden!")
        st.session_state.board_disabled = True
        if spieler + computer == 1:
            st.session_state.spieler += spieler
            st.session_state.computer += computer
    
    if mitte.button("Neues Spiel starten"):
        st.session_state.board = b.clear_board()
        st.session_state.first_move = True
        st.session_state.board_disabled = False
        st.rerun()

    st.write(f"Spieler {st.session_state.spieler} : {st.session_state.computer} Computer")
    
    if mitte.button("Nochmal neu ..."):
        st.session_state.board = b.clear_board()
        st.session_state.first_move = True
        st.session_state.spieler = 0
        st.session_state.computer = 0
        st.session_state.board_disabled = False
        st.rerun()