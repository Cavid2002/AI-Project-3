from adverserial import GenTicTacToe


if __name__ == '__main__':
    n, m = map(int, input("Select n, m:").split())
    game = GenTicTacToe(n, m)
    game.human_vs_ai() 
