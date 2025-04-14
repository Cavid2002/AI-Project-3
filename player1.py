from adverserial import GenTicTacToe

teamID = "1453"
teamID2 = "1444"


if __name__ == '__main__':
    teamID = "1453"
    teamID2 = "1444"
    game = GenTicTacToe(8, 5)
    game.ai_vs_online(teamID, teamID2)