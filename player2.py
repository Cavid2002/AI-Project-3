from adverserial import GenTicTacToe



if __name__ == '__main__':
    teamID2 = "1453"
    gameID = "5458"
    game = GenTicTacToe(6, 5)
    game.online_vs_ai(teamID2, gameID)