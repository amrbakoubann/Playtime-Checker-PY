import requests
from config import API_KEY, RIOT_API_BASE_URL

def get_summoner_id(summoner_name): #function to obtain summoner id 
    url = f"{RIOT_API_BASE_URL}summoner/v4/summoners/by-name/{summoner_name}" #riot API URL
    response = requests.get(url, headers={"X-Riot-Token": API_KEY})
    
    if response.status_code == 200:
        return response.json()['id']
    else:
        print(f"Error fetching summoner ID: {response.status_code}")
        return None

def calculate_total_playtime(summoner_id): #function to calculate summoner playtime
    url = f"{RIOT_API_BASE_URL}match/v4/matchlists/by-account/{summoner_id}"
    response = requests.get(url, headers={"X-Riot-Token": API_KEY})

    if response.status_code == 200:
        matches = response.json()['matches']
        total_playtime = sum([get_match_duration(match['gameId']) for match in matches])
        return total_playtime
    else:
        print(f"Error fetching matchlist: {response.status_code}")
        return 0

# other Riot API related functions
def get_match_duration(match_id):
    url = f"{RIOT_API_BASE_URL}match/v4/matches/{match_id}"
    response = requests.get(url, headers={"X-Riot-Token": API_KEY})

    if response.status_code == 200:
        match_details = response.json()
        # Assuming 'gameDuration' is the field containing match duration in seconds
        return match_details.get('gameDuration', 0) / 60  # Convert seconds to minutes
    else:
        print(f"Error fetching match info: {response.status_code}")
        return 0
    pass