'''
    Defines Player class, and subclasses Human and Minimax Player.
'''
import time

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

    def __init__(self, symbol, depth):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'
        self.depth = depth
        self.total_move_time = 0
        self.num_moves = 0

    def get_move(self, board):
        start_time = time.time()
        _, move = self.minimax(board, self.depth, True)
        end_time = time.time()
        move_time = end_time - start_time
        self.total_move_time += move_time
        self.num_moves += 1
        return move
    
    def get_avg_time(self):
        if self.num_moves == 0:
            return 0
        return round(self.total_move_time / self.num_moves, 6)

    def utility(self, board):
        # this is the win condition logic in GameDriver class
        return board.count_score(self.symbol) - board.count_score(self.oppSym)

    def get_successors(self, board, symbol):
        # This is pretty much has_legal_moves_remaining from OthelloBoard class
        successors = []
        for c in range (0, board.cols):
            for r in range (0, board.rows):
                if board.is_cell_empty(c, r) and board.is_legal_move(c, r, symbol):
                    successors.append((c, r))
        return successors

    def minimax(self, board, depth, maximizing_player):
        # used pseudocode from this video https://www.youtube.com/watch?v=l-hh51ncgDI
        # used pseudocode from p.196 in "Artifical Intelligence: A Modern Approach 4th Edition"
        # by Stuart Russell and Peter Norvig

        if depth == 0 or not self.get_successors(board, self.symbol):
            return self.utility(board), None
        
        if maximizing_player:
            max_val = float('-inf')
            best_move = None
            for successor in self.get_successors(board, self.symbol):
                new_board = board.clone_of_board()
                new_board.play_move(successor[0], successor[1], self.symbol)
                val, _ = self.minimax(new_board, depth-1, False)
                if val > max_val:
                    max_val = val
                    best_move = successor
            return max_val, best_move
        else:
            min_val = float('inf')
            best_move = None
            for successor in self.get_successors(board, self.oppSym):
                new_board = board.clone_of_board()
                new_board.play_move(successor[0], successor[1], self.oppSym)
                val, _ = self.minimax(new_board, depth-1, True)
                if val < min_val:
                    min_val = val
                    best_move = successor
            return min_val, best_move


       
        





