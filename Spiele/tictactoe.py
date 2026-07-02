import streamlit as st
import Spiele.board as b
import Spiele.KI as KI

st.header("Tic Tac Toe")

## alles bereit fürs Spiel ##
zeichen = ["X", "O"]
st.write(f"Du spielst als 2. und hast das Zeichen {zeichen[1]}")
grad = st.pills("Schwierigkeitsstufe", ["leicht", "schwer"], default="leicht")

if "board" not in st.session_state:
    st.session_state.board = b.clear_board()
if "first_move" not in st.session_state:
    st.session_state.first_move = True
if "spieler" not in st.session_state:
    st.session_state.spieler = 0
if "computer" not in st.session_state:
    st.session_state.computer = 0

## dann lass es beginnen ##
# KI spielt zuerst
x_count = sum(row.count("X") for row in st.session_state.board)
o_count = sum(row.count("O") for row in st.session_state.board)
if x_count <= o_count:
    st.session_state.board = KI.make_move(zeichen[0], grad, st.session_state.board, st.session_state.first_move)
    st.session_state.first_move = False          
            
# dann kommt der Spieler
b.draw_board("tic_tac_toe", zeichen[1])

# Auswertung
_, mitte, _ = st.columns(3)

with mitte:
    st.write("")
    st.write("")
    
    spieler = b.check_win_condition(zeichen[1])
    computer = b.check_win_condition(zeichen[0])
    if spieler + computer > 0:
        if spieler == 1:
            st.write("Du hast gewonnen!!")
        if computer == 1:
            st.write("Schade! Der Computer hat gewonnen")
        st.session_state.spieler += spieler
        st.session_state.computer += computer
        st.session_state.board = b.clear_board()

    st.write(f"Spieler {st.session_state.spieler} : {st.session_state.computer} Computer")
    
    if mitte.button("Nochmal neu ..."):
        st.session_state.board = b.clear_board()
        st.session_state.spieler = 0
        st.session_state.computer = 0
        st.rerun()