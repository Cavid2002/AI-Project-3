from adverserial import GenTicTacToe



if __name__ == '__main__':
    teamID = "1453"
    teamID2 = "1449"
    game = GenTicTacToe(12, 6)
    game.ai_vs_online(teamID, teamID2)