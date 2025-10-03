import requests, os
API_KEY = ''
uri = 'https://api.football-data.org/v4/competitions/PL/matches'
headers = {'X-Auth-Token': API_KEY}

response = requests.get(uri, headers=headers)

if response.status_code == 200:
    matches = response.json().get('matches', [])
    print(f"Total matches: {len(matches)}")
    for match in matches[:5]:  # print first 5 matches
        print(match)
else:
    print(f"Error: {response.status_code} - {response.text}")
