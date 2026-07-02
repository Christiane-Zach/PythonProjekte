import random as rd

def make_move(zeichen: str, grad: str, board: list[list], is_first_move: bool):
    #ki_play = True
    #if ki_play:
    #    if grad == "schwer":
    #move = make_good_move(board, is_first_move)
    #    else:
    move = make_random_move()
    board[ord(move[0])-65][int(move[1])-1] = zeichen[0]
    #        ki_play = False
    return board

def make_random_move() -> str:
    return rd.choice('ABC') + rd.choice('123')

def make_good_move(board: list[list], is_first_move: bool) -> str:
    if is_first_move:
        return "B2"
    
    elif ("" != board[1][0] == board[2][0] or "" != board[0][1] == board[0][2] or "" != board[1][1] == board [2][2]) and "" == board[0][0]:
        return "A1"
    elif ("" != board[1][1] == board[2][1] or "" != board[0][0] == board[0][2]) and "" == board[0][1]:
        return "A2"
    elif ("" != board[1][2] == board[2][2] or "" != board[0][0] == board[0][1] or "" != board[2][0] == board[1][1]) and "" == board[0][2]:
        return "A3"
    elif ("" != board[0][0] == board[2][0] or "" != board[1][1] == board[1][2]) and "" == board[1][0]:
        return "B1"
    elif ("" != board[0][1] == board[2][1] or "" != board[1][0] == board[1][2] or "" != board[0][0]== board [2][2] or "" != board[2][0] == board[0][2]) and "" == board[1][1]:
        return "B2"
    elif ("" != board[0][2] == board[2][2] or "" != board[1][0] == board[1][1]) and "" == board[1][2]:
        return "B3"
    elif ("" != board[0][0] == board[1][0] or "" != board[2][1] == board[2][2] or "" != board[1][1] == board[0][2]) and "" == board[2][0]:
        return "C1"
    elif ("" != board[0][1] == board[1][1] or "" != board[2][0] == board[2][2]) and "" == board[2][1]:
        return "C2"
    elif ("" != board[0][2] == board[1][2] or "" != board[2][0] == board[2][1] or "" != board[0][0] == board[1][1]) and "" == board[2][2]:
        return "C3"
    else:
        return make_random_move()