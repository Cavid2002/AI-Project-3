from adverserial import GenTicTacToe



if __name__ == '__main__':
    teamID = "1453"
    teamID2 = "1454"
    game = GenTicTacToe(8, 5)
    game.ai_vs_online(teamID, teamID2)