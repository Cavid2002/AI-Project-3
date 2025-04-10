from typing import List, Tuple, Set
# import api


class GenTicTacToe():

    PROCEED = 0x3F3F3F3F
    INFINITY = 1000000

    def __init__(self, n: int, m: int):
        self.AI = 'O'
        self.OP = 'X'
        self.m = m
        self.max_depth = m * m
        self.n = n
        self.board = self.create_board(self.n)
        self.opMoveHistory = set()
        self.aiMoveHistory = set()

    
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
    
    
    def op_move(self) -> Tuple[int, int]:
        self.print_board()
        while True:
            r, c = map(int, input("Select row, col:").split())
            if self.move_isvalid(r, c):
                break
        
        self.make_move(self.OP, (r, c), self.opMoveHistory)
        return (r, c)
    

    def make_move(self, side: str, move: Tuple, moveHistory: Set[Tuple]):
        moveHistory.add((move[0], move[1]))
        self.board[move[0]][move[1]] = side

    
    def unmake_move(self, move: Tuple, moveHistory: Set[Tuple]):
        moveHistory.remove((move[0], move[1]))
        self.board[move[0]][move[1]] = '-'
    
    def ai_move(self) -> Tuple[int, int]:
        best_move = (-1, -1)
        best_val = GenTicTacToe.INFINITY
        for move in self.get_all_available_moves():
            self.make_move(self.AI, move, self.aiMoveHistory)
            val = self.minimax(True, 0, -GenTicTacToe.INFINITY, GenTicTacToe.INFINITY, move)
            self.unmake_move(move, self.aiMoveHistory)
            if val < best_val:
                best_val = val
                best_move = (move[0], move[1])

        self.make_move(self.AI, best_move, self.aiMoveHistory)
        return best_move
    

    def minimax(self, isMax: bool, depth: int, alpha: int, beta: int, lastMove: Tuple) -> int:
        res = self.evaluate(depth, isMax, lastMove)
        if res != GenTicTacToe.PROCEED:
            return res
        
        if isMax == True:
            return self.maximizer(depth, alpha, beta)
        
        return self.minimizer(depth, alpha, beta)
    

    def maximizer(self, depth: int, alpha: int, beta: int):
        max_val = -GenTicTacToe.INFINITY
        for move in self.get_all_available_moves():
            self.make_move(self.OP, move, self.opMoveHistory)
            res = self.minimax(False, depth + 1, alpha, beta, move)
            self.unmake_move(move, self.opMoveHistory)

            max_val = max(max_val, res)
            alpha = max(alpha, res)
            if alpha >= beta:
                break
        
        return max_val
    
    def minimizer(self, depth: int, alpha: int, beta: int):
        min_val = GenTicTacToe.INFINITY
        for move in self.get_all_available_moves():
            self.make_move(self.AI, move, self.aiMoveHistory)
            res = self.minimax(True, depth + 1, alpha, beta, move)
            self.unmake_move(move, self.aiMoveHistory)

            min_val = min(min_val, res)
            beta = min(beta, res)
            if alpha >= beta:
                break
        
        return min_val

    def evaluate(self, depth: int, isMax: bool, lastMove: Tuple):
        if isMax == True and self.check_winner(self.aiMoveHistory, lastMove):
            return -1 * GenTicTacToe.INFINITY
        if isMax == False and self.check_winner(self.opMoveHistory, lastMove):
            return 1 * GenTicTacToe.INFINITY
        if len(self.get_all_available_moves()) == 0:
            return 0
        if depth == 4:
            return self.heuristics(isMax, lastMove)
        return GenTicTacToe.PROCEED


    def heuristics(self, isMax: bool, lastMove: Tuple):
        score = 0
        
        segments = self.extract_segments(self.board, self.m)
        
        for segment in segments:
            score += self.cal_score(segment, isMax)

        return score
            

    def extract_segments(self, grid, m):
        n = self.n
        segments = []

        if m > n:
            return segments

        for i in range(n):
            for j in range(n - m + 1):
                segments.append([grid[i][j + k] for k in range(m)])

        for j in range(n):
            for i in range(n - m + 1):
                segments.append([grid[i + k][j] for k in range(m)])

        for i in range(n - m + 1):
            for j in range(n - m + 1):
                segments.append([grid[i + k][j + k] for k in range(m)])

        for i in range(n - m + 1):
            for j in range(m - 1, n):
                segments.append([grid[i + k][j - k] for k in range(m)])

        return segments

    
    def cal_score(self, segment, isMax):
        counts = self.count_values(segment)

        ai_count = counts[self.AI] if self.AI in counts else 0
        op_count = counts[self.OP] if self.OP in counts else 0

        if ai_count == self.m:
            return -GenTicTacToe.INFINITY
        
        if op_count == self.m:
            return GenTicTacToe.INFINITY
        
        if op_count > 0:
            if ai_count == 0:
                return self.n ** op_count
            else:
                return 0
        
        return -1 * (self.n ** ai_count)



    def count_values(self, segment):
        value_counts = {}
        for value in segment:
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1
        return value_counts
    

    
    def check_winner(self, move_history: Set[Tuple], lastMove: Tuple) -> bool:
        if lastMove == (-1, -1):
            return False

        direction_pairs = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for (dr1, dc1) in direction_pairs:
            count = 1  
            for step in range(1, self.m):
                nr = lastMove[0] + step * dr1
                nc = lastMove[1] + step * dc1
                if (nr, nc) not in move_history:
                    break
                count += 1
            
            for step in range(1, self.m):
                nr = lastMove[0] - step * dr1
                nc = lastMove[1] - step * dc1
                if (nr, nc) not in move_history:
                    break
                count += 1

            if count >= self.m:
                return True

        return False
    
    
  
    
    def gameLoop(self):
        while True:
                
            move = self.op_move()
            if self.check_winner(self.opMoveHistory, move):
                print('OP won')
                break
            
            if len(self.get_all_available_moves()) == 0:
                print('TIE')
                break

            move = self.ai_move()
            if self.check_winner(self.aiMoveHistory, move):
                print('AI won')
                break
            if len(self.get_all_available_moves()) == 0:
                print('TIE')
                break

        print("AI moves", self.aiMoveHistory)
        print("OP moves", self.opMoveHistory)
        self.print_board()

        return