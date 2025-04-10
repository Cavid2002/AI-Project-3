import http.client
import ast

conn = http.client.HTTPSConnection("www.notexponential.com")
url = "/aip2pgaming/api/index.php"
id = '3672'
key = '52eaecbe714f070fdf20'
teamID = "1453"

headers = {
  'userId': id,
  'x-api-key': key,
  'Content-Type': 'application/x-www-form-urlencoded'
}

def make_post_request(parameters: str) -> str:
    conn.request("POST", url, parameters, headers)
    response = conn.getresponse()
    data = response.read().decode()
    return ast.literal_eval(data)

def make_get_request(parameters: str) -> str:
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


def create_game(teamId1: str, teamId2: str, boardSize: int, target: int) -> dict:
    payload = f"type=game&teamId1={teamId1}&teamId2={teamId2}&gameType=TTT&boardSize={boardSize}&target={target}"
    res = make_post_request(payload)
    print(res)
    assert res['code'] == 'OK', 'create_game'
    return res

def get_my_games() -> dict:
    payload = f"type=myGames"
    res = make_get_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_my_games'
    return res

def make_move(gameId: str, teamId: str, move) -> dict:
    payload = f"type=move&gameId={gameId}&teamId={teamId}&move={move}"
    res = make_post_request(payload)
    print(res)
    assert res['code'] == 'OK', 'make_move'
    return res

def get_moves(gameId: str) -> dict:
    payload = f"type=moves&gameId={gameId}"
    res = make_get_request(payload)
    print(res)
    assert res['code'] == 'OK', 'get_moves'
    return res

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

# teamId = create_team("TEST")
# add_team_member("1453", "3675")
# add_team_member("1453", id)
# get_team_members(teamID)
# get_my_team()
# get_team_members(teamID)