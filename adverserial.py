from typing import List, Tuple
import api


class GenTicTacToe():

    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, -1, -1, 1, 1]
    ai = 'X'
    human = 'O'
    infinity = 9999999

    def __init__(self, n: int, m: int):
        self.m = m
        self.n = n
        self.board = self.create_board(self.n)
        self.moveHistory = {}

    
    def create_board(self, n: int) -> List[List[str]]:
        board = [['-' for _ in range(n)] for _ in range(n)]
        return board


    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], sep=" ")
            print()
        return
    
    def is_valid(self, row: int, col: int) -> bool:
        if(row >= self.n or row < 0): 
            return False
        if(col >= self.n or col < 0): 
            return False
        return self.board[row][col] == "-"
    
    def make_move(self, row: int, col: int, char: str):
        self.board[row][col] = char
        return

    def unmake_move(self, row: int, col: int):
        self.board[row][col] = '-'
        return

    def get_all_aviable_moves(self) -> List[Tuple]:
        allMoves = []
        for i in range(self.n):
            for j in range(self.n):
                if(self.board[i][j] == "-"):
                    allMoves.append((i, j))
        return allMoves

    def make_best_move(self):
        allMoves = self.get_all_aviable_moves()
        ...    


    def minimax(self):
        ...