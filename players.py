'''
    Defines Player class, and subclasses Human and Minimax Player.
'''

from board import Direction

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()


class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return col, row


class MinimaxPlayer(Player):

    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.maximizing_player = True
            self.oppSym = 'O'
        else:
            self.maximizing_player = False
            self.oppSym = 'X'

    def get_move(self, board):
        print("get_move Board:", board)
        _, move = self.minimax(board, 7, self.maximizing_player)
        return move

    def utility(self, board):
        print("utility Board:", board)
        return board.count_score(self.symbol) - board.count_score(self.oppSym)

    def get_successors(self, board, symbol):
        print("get_successors Board:", board)
        successors = []
        for c in range (0, board.cols):
            for r in range (0, board.rows):
                if board.is_cell_empty(c, r) and board.is_legal_move(c, r, symbol):
                    successors.append((c, r))
        return successors

    def minimax(self, board, depth, maximizing_player):
        print("minimax Board:", board)
        # https://www.youtube.com/watch?v=l-hh51ncgDI

        if board is None or depth == 0 or not self.get_successors(board, self.symbol):
            return self.utility(board), None
        
        if maximizing_player:
            max_val = float('-inf')
            best_move = None
            for successor in self.get_successors(board, self.symbol):
                new_board = board.play_move(successor[0], successor[1], self.symbol)
                val, _ = self.minimax(new_board, depth-1, False)
                if val > max_val:
                    max_val = val
                    best_move = successor
            return max_val, best_move
        else:
            min_val = float('inf')
            best_move = None
            for successor in self.get_successors(board, self.oppSym):
                new_board = board.play_move(successor[0], successor[1], self.oppSym)
                val, _ = self.minimax(new_board, depth-1, True)
                if val < min_val:
                    min_val = val
                    best_move = successor
            return min_val, best_move

        # if depth == 0 or game over in position
            # return static evaluation of position
        
        # if maximizingPlayer
            # maxEval = negative infinity
            # for each child of position
                # eval = minimax(child, depth-1, false)
                # maxEval = max(maxEval, eval)
            # return maxEval
            
        # else
            # minEval = infinity
            # for each child of position
                # eval = minimax(child, depth -1, true)
                # minEval = min(minEval, eval)
        # pass


       
        





