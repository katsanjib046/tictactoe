"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    count = 9
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count -= 1
    return O if count % 2 == 0 else X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(newBoard)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        if board[i][0] == board[i][1] == board[i][2] == O:
            return O
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for i in range(3):
            if EMPTY in board[i]:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    The input board is assumed to be terminal.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # If the current player is maximizing player, here X
    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            if (new :=min_value(result(board, action))) > value:
                value = new
                optimal_action = action
        return optimal_action

    # If the current player is minimizing player, here O
    else:
        value = math.inf
        for action in actions(board):
            if (new :=max_value(result(board, action))) < value:
                value = new
                optimal_action = action
        return optimal_action

    

def min_value(board):
    """Returns the minimum possible value of a particular board"""
    if terminal(board):
        return utility(board)
    value= math.inf
    for action in actions(board):
        value = min(value,max_value(result(board, action)))
    return value

def max_value(board):
    """Returns the minimum possible value of a particular board"""
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value
