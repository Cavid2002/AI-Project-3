from adverserial import GenTicTacToe



n, m = map(int, input("Select n, m:").split())
game = GenTicTacToe(n, m)
game.human_vs_ai()