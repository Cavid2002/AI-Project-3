import http.client
import ast

url = "/aip2pgaming/api/index.php"
id = '3672'
key = '6f7504789dda4c53374b'

headers = {
  'userId': id,
  'x-api-key': key,
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'humans_21909=1'
}

def make_post_request(parameters: str) -> str:
    conn = http.client.HTTPSConnection("www.notexponential.com")
    conn.request("POST", url, parameters, headers)
    response = conn.getresponse()
    data = response.read().decode()
    return ast.literal_eval(data)

def make_get_request(parameters: str) -> str:
    conn = http.client.HTTPSConnection("www.notexponential.com")
    full_path = url + "?" + parameters
    conn.request("GET", full_path, None, headers)
    response = conn.getresponse()
    data = response.read().decode()
    return ast.literal_eval(data)


def create_team(tname: str) -> dict:
    payload = f"type=team&name={tname}"
    res = make_post_request(payload)
    print(res)
    assert res['code'] == 'OK', 'create_team'
    return res['teamId']
        

def add_team_member(teamId: str, userId: str)-> dict:
    payload = f"type=member&userId={userId}&teamId={teamId}"
    res = make_post_request(payload)
    print(res)
    assert res['code'] == 'OK', 'add_team_member'
    return res


def remove_team_member(teamId: str, userId: str) -> dict:
    payload = f"type=removeMember&userId={userId}&teamId={teamId}"
    res = make_post_request(payload)
    print(res)
    assert res['code'] == 'OK', 'remove_team_member'
    return res


def get_team_members(teamId: str) -> dict:
    payload = f"type=team&teamId={teamId}"
    res = make_get_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_team_members'
    return res


def get_my_team() -> dict:
    payload = f"type=myTeams"
    res = make_get_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_my_team'
    return res


def create_game(teamId1: str, teamId2: str, boardSize: int, target: int) -> str:
    payload = f"type=game&teamId1={teamId1}&teamId2={teamId2}&gameType=TTT&boardSize={boardSize}&target={target}"
    res = make_post_request(payload)
    print(res)
    assert res['code'] == 'OK', 'create_game'
    return res['gameId']

def get_my_games() -> dict:
    payload = f"type=myGames"
    res = make_get_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_my_games'
    return res

def get_my_open_games() -> dict:
    payload = f"type=myOpenGames"
    res = make_get_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_my_games'
    return res

def make_move(gameId: str, teamId: str, move: str) -> dict:
    payload = f"type=move&gameId={gameId}&teamId={teamId}&move={move}"
    res = make_post_request(payload)
    print(res)
    assert res['code'] == 'OK', 'make_move'
    return str(res['moveId'])

def get_moves(gameId: str, count: str) -> dict:
    payload = f"type=moves&gameId={gameId}&count={count}"
    res = make_get_request(payload)
    assert res['code'] == 'OK', 'get_moves'
    return res['moves'][0]

def get_game_details(gameId: str) -> dict:
    payload = f"type=gameDetails&gameId={gameId}"
    res = make_get_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_game_details'
    return res

def get_board_string(gameId: str) -> dict:
    payload = f"type=boardString&gameId={gameId}"
    res = make_post_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_board_string'
    return res

def get_board_map(gameId: str) -> dict:
    payload = f"type=boardMap&gameId={gameId}"
    res = make_get_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_board_map'
    return res




# teamId = create_team("TEST23")


# add_team_member("1453", "3675")
# add_team_member(teamID2, id)
# get_team_members(teamID2)
# get_my_team()
# get_team_members(teamID)
# get_my_games()

# gameId = create_game(teamID, teamID2, 5, 3)
# d = get_moves(gameId, "1")
# moveid = make_move(gameId, teamID, "0,1")
# print(d)
# moveid = make_move("5211", teamID2, "2,0")


