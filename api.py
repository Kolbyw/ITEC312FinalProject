import requests
import json


def search(teamName):
    teamList = {
        "arsenal": 57,
        "aston villa": 58,
        "chelsea": 61,
        "everton": 62,
        "fulham": 63,
        "liverpool": 64,
        "manchester city": 65,
        "manchester united": 66,
        "newcastle": 67,
        "tottenham hotspur": 73,
        "wolverhampton wanderers": 76,
        "leicester city": 338,
        "southampton": 340,
        "ipswich town": 349,
        "nottingham forest": 351,
        "crystal palace": 354,
        "brighton": 397,
        "brentford": 402,
        "west ham": 563,
        "bournemouth": 1044
    }

    try:
        print("input: ", teamName.lower())
        teamId = teamList[teamName.lower()]
        print("team id: ", teamId)
    except:
        print("Team not in team list")
        return("")

    # uri = 'https://api.football-data.org/v4/competitions/PL/standings'
    # headers = { 'X-Auth-Token': '9e728cd7a7054bf7a4e062a0038c29b1' }

    # response = requests.get(uri, headers=headers)
    # for team in response.json()['standings']:
    #     print(team['table'])

    uri = 'https://api.football-data.org/v4/teams/' + str(teamId)
    headers = { 'X-Auth-Token': '9e728cd7a7054bf7a4e062a0038c29b1' }
    try:
        teamInfo = requests.get(uri, headers=headers)
        fixtures = requests.get(uri + "/matches?status=SCHEDULED", headers=headers)
        results = requests.get(uri + "/matches?status=FINISHED", headers=headers)

        # print(fixtures.json())
        upcoming = "Upcoming Matches:\n"
        count = 0
        for game in reversed(fixtures.json()['matches']):
            if(game['competition']['name'] == 'Premier League' and count < 5):
                upcoming += ("\n" + game['homeTeam']['name'] + " vs " + game['awayTeam']['name'])
            count += 1
            
        recent = "Recent 5 Matches:\n"
        count = 0
        for game in reversed(results.json()['matches']):
            if(game['competition']['name'] == 'Premier League' and count < 5):
                recent += (f"\n {game['homeTeam']['name']} {game['score']['fullTime']['home']} - {game['score']['fullTime']['away']} {game['awayTeam']['name']}")
            count += 1
            
        response = [teamInfo.json(), upcoming, recent]
        return(response)
        # for team in response.json():
        # print(response.json()['name'])
        # print(response.json()['founded'])
        # print(response.json()['coach'])
    except:
        print("error")

    
    