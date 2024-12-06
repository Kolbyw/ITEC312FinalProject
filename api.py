import requests
import json


def search(teamName):
    # dictionary of teams: key = team name, value = teamId (For API)
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

    # Make input lowercase for case in-sensitivity and check if team name is in list
    try:
        print("input: ", teamName.lower())
        teamId = teamList[teamName.lower()]
        print("team id: ", teamId)
    except: # if team name not in list, let the user know
        print("Team not in team list")
        return("")

    uri = 'https://api.football-data.org/v4/teams/' + str(teamId) # API link
    headers = { 'X-Auth-Token': '9e728cd7a7054bf7a4e062a0038c29b1' }
    try:
        teamInfo = requests.get(uri, headers=headers) # API call for basic team info
        fixtures = requests.get(uri + "/matches?status=SCHEDULED", headers=headers) # API call for upcoming matches
        results = requests.get(uri + "/matches?status=FINISHED", headers=headers) # API call for finished matches


        # loop through upcoming matches, and collect the first 5 matches in the Premier League
        upcoming = "Upcoming Matches:\n"
        count = 0
        for game in reversed(fixtures.json()['matches']):
            if(game['competition']['name'] == 'Premier League' and count < 5):
                upcoming += ("\n" + game['homeTeam']['name'] + " vs " + game['awayTeam']['name'])
            count += 1
        
            
        # loop through recent matches, and collect the first 5 matches in the Premier League
        recent = "Recent 5 Matches:\n"
        count = 0
        for game in reversed(results.json()['matches']):
            if(game['competition']['name'] == 'Premier League' and count < 5):
                recent += (f"\n {game['homeTeam']['name']} {game['score']['fullTime']['home']} - {game['score']['fullTime']['away']} {game['awayTeam']['name']}")
            count += 1

        # add the three responses (team info, upcoming matches, finished matches) into a list and return
        response = [teamInfo.json(), upcoming, recent]
        return(response)
    
    # handle error in the API call
    except: 
        print("Error in calling the API")

    
    