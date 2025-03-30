import http.client
import ast

conn = http.client.HTTPSConnection("www.notexponential.com")
url = "/aip2pgaming/api/index.php"
id = '3672'
key = '52eaecbe714f070fdf20'

headers = {
  'userId': id,
  'x-api-key': key,
  'Content-Type': 'application/x-www-form-urlencoded'
}

def make_request(method: str, data: str) -> dict:
    conn.request(method, url, data, headers)
    response = conn.getresponse()
    data = response.read().decode()
    return ast.literal_eval(data)


def create_team(tname: str) -> bool:
    payload = f"type=team&name={tname}"
    res = make_request('POST', payload)
    print(res)
    assert res['code'] == 'OK', 'create_team'
    return res
        

def add_team_member(teamId: str, userId: str)-> dict:
    payload = f"type=team&userId={userId}&teamId={teamId}"
    res = make_request("POST", payload)
    print(res)
    assert res['code'] == 'OK', 'add_team_member'
    return dict


def get_team_members(teamId: str) -> dict:
    payload = f"type=team&teamId={teamId}"
    res = make_request("GET", payload)
    print(res)
    assert res['code'] == 'OK', 'get_team_members'
    return res


def get_my_team() -> dict:
    payload = f"type=myTeam"
    res = make_request("GET", payload)
    print(res)
    assert res['code'] == 'OK', 'get_my_team'
    return res


def create_game(teamId1: str, teamId2: str) -> dict:
    payload = f"type=game&teamId1={teamId1}&teamId2={teamId2}&gameType=TTT"
    res = make_request("POST", payload)
    print(res)
    assert res['code'] == 'OK', 'create_game'
    return res

def get_my_games() -> dict:
    payload = f"type=myGames"
    res = make_request("GET", payload)
    print(res)
    assert res['code'] == 'OK', 'get_my_games'
    return res

def make_move(gameId: str, teamId: str, move) -> dict:
    payload = f"type=move&gameId={gameId}&teamId={teamId}&move={move}"
    res = make_request("POST", payload)
    print(res)
    assert res['code'] == 'OK', 'make_move'
    return res

def get_moves(gameId: str) -> dict:
    payload = f"type=moves&gameId={gameId}"
    res = make_request("GET", payload)
    print(res)
    assert res['code'] == 'OK', 'get_moves'
    return res

def get_game_details(gameId: str) -> dict:
    payload = f"type=gameDetails&gameId={gameId}"
    res = make_request("GET", payload)
    print(res)
    assert res['code'] == 'OK', 'get_game_details'
    return res

def get_board_string(gameId: str) -> dict:
    payload = f"type=boardString&gameId={gameId}"
    res = make_request("GET", payload)
    print(res)
    assert res['code'] == 'OK', 'get_board_string'
    return res

def get_board_map(gameId: str) -> dict:
    payload = f"type=boardMap&gameId={gameId}"
    res = make_request("GET", payload)
    print(res)
    assert res['code'] == 'OK', 'get_board_map'
    return res


create_team("TestTest")