'''
    Defines game driver class, used to play a game of Othello.
'''
import sys
from players import *
from othello_board import OthelloBoard
import argparse


class GameDriver:
    def __init__(self, p1type, p2type, num_rows, num_cols, depth):
        if p1type.lower() in "human":
            self.p1 = HumanPlayer('X')
        elif p1type.lower() in "minimax" or p1type in "ai":
            self.p1 = MinimaxPlayer('X', depth)
        else:
            print("Invalid player 1 type!")
            exit(-1)

        if p2type.lower() in "human":
            self.p2 = HumanPlayer('O')
        elif p2type.lower() in "minimax" or p1type in "ai":
            self.p2 = MinimaxPlayer('O', depth)
        else:
            print("Invalid player 2 type!")
            exit(-1)

        self.board = OthelloBoard(num_rows, num_cols, self.p1.symbol, self.p2.symbol)
        self.board.initialize()

    def display(self):
        print("Player 1 (", self.p1.symbol, ") score: ",
                self.board.count_score(self.p1.symbol))

    def process_move(self, curr_player, opponent):
        invalid_move = True
        while invalid_move:
            (col, row) = curr_player.get_move(self.board)
            if not self.board.is_legal_move(col, row, curr_player.symbol):
                print("Invalid move")
            else:
                print("Move:", [col,row], "\n")
                self.board.play_move(col,row,curr_player.symbol)
                return

    def run(self):
        current = self.p1
        opponent = self.p2
        self.board.display()

        cant_move_counter, toggle = 0, 0

        print("Player 1(", self.p1.symbol, ") move:")
        while True:
            if self.board.has_legal_moves_remaining(current.symbol):
                cant_move_counter = 0
                self.process_move(current, opponent)
                self.board.display()
            else:
                print("Can't move")
                if cant_move_counter == 1:
                    break
                else:
                    cant_move_counter +=1
            toggle = (toggle + 1) % 2
            if toggle == 0:
                current, opponent = self.p1, self.p2
                print("Player 1(", self.p1.symbol, ") move:")
            else:
                current, opponent = self.p2, self.p1
                print("Player 2(", self.p2.symbol, ") move:")

        #decide win/lose/tie state
        state = self.board.count_score(self.p1.symbol) - self.board.count_score(self.p2.symbol)
        if state == 0:
            print("Tie game!!")
        elif state >0:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")

        if isinstance(game.p1, MinimaxPlayer):
            avg_time = game.p1.get_avg_time()
            print("Player 1 average time to move:", avg_time, "seconds")

        if isinstance(game.p2, MinimaxPlayer):
            avg_time = game.p2.get_avg_time()
            print("Player 2 average time to move:", avg_time, "seconds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play a game of Othello.")
    parser.add_argument("player1_type", help="Type of player for Player 1")
    parser.add_argument("player2_type", help="Type of player for Player 2")
    parser.add_argument("--board_size", type=int, default=4, help="Size of the board (default: 4)")
    parser.add_argument("--depth", type=int, default=3, help="Depth of recursion for minimax search (default: 3)")
    args = parser.parse_args()
    game = GameDriver(args.player1_type, args.player2_type, args.board_size, args.board_size, args.depth)
    game.run()
