from typing import List, Tuple, Set
import api


class GenTicTacToe():

    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, -1, -1, 1, 1]
    human = 'X'
    ai = 'O'

    def __init__(self, n: int, m: int):
        self.m = m
        self.n = n
        self.board = self.create_board(self.n)
        self.opMoveHistory = {}
        self.aiMoveHistory = {}

    
    def create_board(self, n: int) -> List[List[str]]:
        board = [[GenTicTacToe.empty for _ in range(n)] for _ in range(n)]
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

    def checkWinner(side: str, moveHistory: Set[Tuple]):
        ...

    def evaluate(self):
        self.aiMoveHistory

    def get_all_aviable_moves(self) -> List[Tuple]:
        allMoves = []
        for i in range(self.n):
            for j in range(self.n):
                if(self.board[i][j] == "-"):
                    allMoves.append((i, j))
        return allMoves

    
    def make_best_move(self):
        allMoves = self.get_all_aviable_moves()
        bestVal = 999999999
        bestMove = (-1, -1)
        for move in allMoves:
            self.board[move[0]][move[1]] = GenTicTacToe.ai
            value = self.minimax(0, False)
            self.board[move[0]][move[1]] = '-'
            if(value < bestVal):
                bestMove = (move[0], move[1])
                bestVal = value
        
        self.board[bestMove[0]][bestMove[1]]        
            


    def minimax(self, depth: int, isMax: bool) -> int:
        score = self.evalutate
        if(score != -5):
            return score
        if(isMax == True):
            return self.maximizer(depth)
        else:
            return self.minimizer(depth)

    
    def maximizer(self, depth: int) -> int:
        allMoves = self.get_all_aviable_moves()
        maxVal = -99999999
        for move in allMoves:
            self.board[move[0]][move[1]] = GenTicTacToe.human
            maxVal = max(maxVal, self.minimax(depth + 1, False))
            self.board[move[0]][move[1]] = '-'
        return maxVal
    
    
    def minimizer(self, depth: int) -> int:
        allMoves = self.get_all_aviable_moves()
        minVal = 99999999
        for move in allMoves:
            self.board[move[0]][move[1]] = GenTicTacToe.ai
            minVal = min(minVal, self.minimax(depth + 1, False))
            self.board[move[0]][move[1]] = '-'
        return minVal