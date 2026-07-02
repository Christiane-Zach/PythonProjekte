import streamlit as st

def draw_board(prefix: str, spieler: str) -> None:
    for row in range(len(st.session_state.board)):
        cols = st.columns(len(st.session_state.board[row]), gap="small")
        for col in range(len(st.session_state.board[row])):
            with cols[col]:
                if st.button(st.session_state.board[row][col], key=f"{prefix}_{row}_{col}", use_container_width=True):
                    st.session_state.board[row][col] = spieler
                    st.rerun()
                        

def check_win_condition(spieler: str) -> int:
    board = st.session_state.board
    ### Zeilen-Check und Spalten-Check ###
    for i in range(3):
        if spieler == board[0][i] == board[1][i] == board[2][i] or spieler == board[i][0] == board[i][1] == board[i][2]:
            return 1
        
    ### Diagonalen-Check ###
    if spieler == board[0][0] == board[1][1] == board [2][2] or spieler == board[2][0] == board[1][1] == board[0][2]:
        return 1
    
    ### Unentschieden-Check ###
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return 0
    return 2

def clear_board() -> list[list]:
    return [["", "", ""],
            ["", "", ""],
            ["", "", ""]]