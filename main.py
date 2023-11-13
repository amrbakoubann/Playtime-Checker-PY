from riot_api import get_summoner_id, calculate_total_playtime

def main():
    summoner_name = input(" Welecome! Enter your Summoner Name: ")
    summoner_id = get_summoner_id(summoner_name)

    if summoner_id:
        total_playtime = calculate_total_playtime(summoner_id)
        print(f" Your total playtime for {summoner_name}: {total_playtime} minutes")
            if (total_playtime >= 50000)
                print (f" Did you really waste over a month playing this trash? Get a life lol" )
    else:
        print("Error! Summoner not found.")

if __name__ == "__main__":
    main()
