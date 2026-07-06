def clear_board() -> list[list]:
    """Ein leeres Spielfeld wird zurückgegeben"""
    return [["", "", ""],
            ["", "", ""],
            ["", "", ""]]

def check_win_condition(spieler: str, board: list[list]) -> int:
    """Gibt 0 zurück, wenn das Spiel noch läuft, 1, wenn jemand gewonnen hat, und 2, wenn es unentschieden ist"""
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