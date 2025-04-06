from typing import List, Tuple, Set
import api


class GenTicTacToe():

    PROCEED = 0x3F3F
    INFINITY = 1000000

    def __init__(self, n: int, m: int):
        self.AI = 'O'
        self.OP = 'X'
        self.m = m
        self.n = n
        self.board = self.create_board(self.n)
        self.opMoveHistory = set()
        self.aiMoveHistory = set()
        self.lastMove = (-1, -1)
        self.lastMoveSide = self.OP
    
    def create_board(self, n: int) -> List[List[str]]:
        board = [['-' for _ in range(n)] for _ in range(n)]
        return board


    def move_isvalid(self, r: int, c: int) -> bool:
        if r >= self.n or r < 0:
            return False
        if c >= self.n or c < 0:
            return False
        return self.board[r][c] == '-'
    

    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()
        return
    
    
    def get_all_available_moves(self) -> List[Tuple]:
        all_moves = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == '-':
                    all_moves.append((i, j))
        return all_moves
    
    
    def op_move(self):
        self.print_board()
        while True:
            r, c = map(int, input("Select row, col:").split())
            if self.move_isvalid(r, c):
                break
        self.board[r][c] = self.OP
        self.opMoveHistory.add((r, c))
        self.lastMove = (r, c)
        return
    

    def make_move(self, side: str, move: Tuple, moveHistory: Set[Tuple]):
        moveHistory.add((move[0], move[1]))
        self.lastMove = (move[0], move[1])
        self.board[move[0]][move[1]] = side

    
    def unmake_move(self, move: Tuple, moveHistory: Set[Tuple]):
        moveHistory.remove((move[0], move[1]))
        self.board[move[0]][move[1]] = '-'
    
    def ai_move(self):
        best_move = (-1, -1)
        best_val = 9999999
        all_moves = self.get_all_available_moves()
        for move in all_moves:
            self.make_move(self.AI, move, self.aiMoveHistory)
            val = self.minimax(True, 0)
            self.unmake_move(move, self.aiMoveHistory)
            if val < best_val:
                best_val = val
                best_move = (move[0], move[1])

        self.make_move(self.AI, best_move, self.aiMoveHistory)
        return 
    
    
    def check_winner(self, move_history: Set[Tuple]) -> bool:
        if self.lastMove == (-1, -1):
            return False

        direction_pairs = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for (dr1, dc1) in direction_pairs:
            count = 1  
            for step in range(1, self.m):
                nr = self.lastMove[0] + step * dr1
                nc = self.lastMove[1] + step * dc1
                if (nr, nc) not in move_history:
                    break
                count += 1
            
            for step in range(1, self.m):
                nr = self.lastMove[0] - step * dr1
                nc = self.lastMove[1] - step * dc1
                if (nr, nc) not in move_history:
                    break
                count += 1

            if count >= self.m:
                return True

        return False
    
    def evaluate(self, isMax: bool, depth: int):
        if isMax == False and self.check_winner(self.opMoveHistory):
            return 1 * (GenTicTacToe.INFINITY - depth)
        if isMax == True and self.check_winner(self.aiMoveHistory):
            return -1 * (GenTicTacToe.INFINITY - depth)
        if len(self.get_all_available_moves()) == 0 or depth >= 3:
            return 0
        return GenTicTacToe.PROCEED
 
    
    def minimax(self, isMax: bool, depth: int) -> int:
        res = self.evaluate(isMax, depth)
        if res != GenTicTacToe.PROCEED:
            return res

        if isMax:
            return self.maximizer(depth)
        
        return self.minimizer(depth)

    
    def maximizer(self, depth: int):
        max_res = -GenTicTacToe.INFINITY
        all_moves = self.get_all_available_moves()
        old_last_move = (self.lastMove[0], self.lastMove[1])
        
        for move in all_moves:
            self.make_move(self.OP, move, self.opMoveHistory)
            max_res = max(max_res, self.minimax(False, depth + 1))
            self.unmake_move(move, self.opMoveHistory)
            

        self.lastMove = (old_last_move[0], old_last_move[1])
        return max_res
    
    
    def minimizer(self, depth: int):
        min_res = GenTicTacToe.INFINITY
        all_moves = self.get_all_available_moves()
        old_last_move = (self.lastMove[0], self.lastMove[1])

        for move in all_moves:
            self.make_move(self.AI, move, self.aiMoveHistory)
            min_res = min(min_res, self.minimax(True, depth + 1))
            self.unmake_move(move, self.aiMoveHistory)

        self.lastMove = (old_last_move[0], old_last_move[1])
        return min_res
  
    
    def gameLoop(self):
        while True:
                
            self.op_move()
            if self.check_winner(self.opMoveHistory):
                print('OP won')
                break
            
            if len(self.get_all_available_moves()) == 0:
                print('TIE')
                break

            self.ai_move()
            if self.check_winner(self.aiMoveHistory):
                print('AI won')
                break
            if len(self.get_all_available_moves()) == 0:
                print('TIE')
                break

        print("AI moves", self.aiMoveHistory)
        print("OP moves", self.opMoveHistory)
        self.print_board()

        return