from tictactoe import player, actions, result, winner, terminal, utility, minimax, calculate_utility_sum

EMPTY = None
X = 'X'
O = 'O'

def board(Xs =[], Os =[]):
    var_board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    for action in Xs:
        var_board[action[0]][action[1]] = X
    for action in Os:
        var_board[action[0]][action[1]] = O
    return var_board



def test_player():
    assert player(board()) == X
    assert player(board(Xs = [(0,0)])) == O
    assert player(board(Xs = [(0,0)], Os = [(0,1)])) == X


def test_actions():
    assert actions(board()) == {(0,0), (0,1), (0,2),
                                (1,0), (1,1), (1,2),
                                (2,0), (2,1), (2,2)}

    assert actions(board(Xs = [(0,0)], Os = [(0,1)])) == {(0,2),
                                                            (1,0), (1,1), (1,2),
                                                            (2,0), (2,1), (2,2)}

    assert actions(board(Xs = [(0,0)], Os = [(0,1), (1,1)])) == {(0,2),
                                                            (1,0), (1,2),
                                                            (2,0), (2,1), (2,2)}
    
def test_result():
    assert result(board(), (0,0)) == board(Xs = [(0,0)], Os = [])
    assert result(board(Xs = [(0,0)], Os = []), (0,1)) == board(Xs = [(0,0)], Os = [(0,1)])

def test_winner():
    assert winner(board()) == None
    assert winner(board(Xs = [(0,0)], Os = [])) == None
    assert winner(board(Xs = [(0,0), (1,0),(2,0) ], Os = [(0,1), (0,2)])) == X
    assert winner(board(Xs = [(0,0), (1,1),(2,2) ], Os = [(0,1), (0,2)])) == X

def test_terminal():
    assert terminal(board()) == False
    assert terminal(board(Xs = [(0,0), (1,1),(2,2) ], Os = [(0,1), (0,2)])) == True
    assert terminal(board(Xs = [(0,0), (1,0),(2,0) ], Os = [(0,1), (0,2)])) == True

def test_utility():
    assert utility(board(Xs = [(0,0), (1,0),(2,0) ], Os = [(0,1), (0,2)])) == 1
    assert utility(board(Xs = [(0,1), (0,2), (1,2)], Os = [(0,0), (1,0),(2,0) ])) == -1
    assert utility(board(Xs = [(0,1), (0,2), (1,2)], Os = [(0,0), (1,1),(2,2) ])) == -1


def test_minimax():
    assert minimax(board(Xs = [(0,1), (1,0), (2,0), (1,1)], Os = [(0,0), (0,2), (2,1)])) == (1,2)
    assert minimax(board(Xs = [(0,1), (1,0), (2,0), (1,1)], Os = [(0,0), (0,2), (1,2)])) == (2,2)

