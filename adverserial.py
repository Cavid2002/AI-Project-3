from typing import List, Tuple, Set
import api


class GenTicTacToe():

    human = 'X'
    ai = 'O'

    def __init__(self, n: int, m: int):
        self.m = m
        self.n = n
        self.board = self.create_board(self.n)
        self.opMoveHistory = set()
        self.aiMoveHistory = set()
        self.print_board()

    
    def create_board(self, n: int) -> List[List[str]]:
        board = [['-' for _ in range(n)] for _ in range(n)]
        return board


    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()
        return
    
    def print_result(self, score: int):
        if score == 0: 
            print("TIE")
        winner = "Human" if score == 1 else "AI"
        print(f"{winner} Won!")
    

    def is_valid(self, row: int, col: int) -> bool:
        if row >= self.n or row < 0: 
            return False
        if col >= self.n or col < 0: 
            return False
        return self.board[row][col] == "-"

    
    def checkWinner(self, moveHistory: Set[Tuple]):
        dc = [1, -1, 0, 0, 1, -1, 1, -1]
        dr = [0, 0, 1, -1, -1, -1, 1, 1]
        for move in moveHistory:
            for i in range(len(dr)):
                count = 1
                for step in range(1, self.m):
                    nr = move[0] + step * dr[i]
                    nc = move[1] + step * dc[i]
                    if (nr, nc) not in moveHistory:
                        break
                    count += 1
                if count == self.m:
                    return True
        return False

        

    def evaluate(self):
        if self.checkWinner(self.aiMoveHistory):
            return -1
        if self.checkWinner(self.opMoveHistory):
            return 1
        if len(self.get_all_aviable_moves()) == 0:
            return 0
        return -5
        

    def get_all_aviable_moves(self) -> List[Tuple]:
        allMoves = []
        for i in range(self.n):
            for j in range(self.n):
                if(self.board[i][j] == "-"):
                    allMoves.append((i, j))
        return allMoves

    
    def ai_move(self):
        allMoves = self.get_all_aviable_moves()
        if len(allMoves) == 0:
            return
        bestVal = 999999999
        bestMove = (-1, -1)
        for move in allMoves:
            self.board[move[0]][move[1]] = GenTicTacToe.ai
            value = self.minimax(0, False)
            self.board[move[0]][move[1]] = '-'
            if(value < bestVal):
                bestMove = (move[0], move[1])
                bestVal = value
        self.board[bestMove[0]][bestMove[1]] = GenTicTacToe.ai
        self.aiMoveHistory.add((bestMove[0], bestMove[1]))
        return   
            
    def op_move(self):
        self.print_board()
        while True:
            r, c = map(int, input("Make a move (row col): ").split())
            if self.is_valid(r, c):
                break
            print("Move is invalid")
        self.board[r][c] = GenTicTacToe.human
        self.opMoveHistory.add((r, c))
        return
        

    def minimax(self, depth: int, isMax: bool) -> int:
        score = self.evaluate()
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
            minVal = min(minVal, self.minimax(depth + 1, True))
            self.board[move[0]][move[1]] = '-'
        return minVal
    

    def gameLoop(self):
        while True:
            if len(self.get_all_aviable_moves()) == 0:
                print("Tie")
                return
            
            self.op_move()
            
            if self.checkWinner(self.opMoveHistory):
                print("You WON")
                return

            self.ai_move()

            if self.checkWinner(self.aiMoveHistory):
                print("AI won")
                return
            
                
        