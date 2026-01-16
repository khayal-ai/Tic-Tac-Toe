"""
Tic Tac Toe Player
"""

import copy

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
    X_count = 0
    O_count = 0

    for row in board: #the board is 3x3 matrix so we need to iterate over row and col
        for cell in row:
            if cell == X: #if cell we increment X
                X_count += 1
            elif cell == O: #if cell O we increment O
                O_count += 1
    if X_count == O_count: # x & o have same count so its X turn
        return X
    else: # diff count so its O turn
        return O


def actions(board): # Goal: return a set of (i, j) moves for every empty cell.
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: #if cell is empty we add it to set of poss actions
                possible_actions.add((i,j))
    return possible_actions

def result(board, action): # Goal: return a new board with the move made by player
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if board[i][j] != EMPTY: #if cell not empty raise error
        raise ValueError("Invalid Action")  #meaning the cell is already X or O CANT BE OVERWRITTEN

    new_board = copy.deepcopy(board) #deep copy to avoid mutating og board
    new_board[i][j] = player(board)  #make move on new board

    return new_board
            

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Checking if have same value on each row means there is a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
    
    #Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False #still there is emoty cell means the game not finished
    return True # no empty cells and no winner

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w= winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    turn = player(board)

    def max_value(state):
        if terminal(state):
            return utility(state)
        v = float("-inf") #negarive infinity
        for action in actions(state):
            v = max(v, min_value(result(state, action)))
        return v

    def min_value(state):
        if terminal(state):
            return utility(state)
        v = float("inf") #positive infinity
        for action in actions(state):
            v = min(v, max_value(result(state, action)))
        return v

    best_action = None

    if turn == X:
        best_score = float("-inf")
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
    else:  # turn == O
        best_score = float("inf")
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action

    return best_action

