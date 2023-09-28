import espnfantasyfootball as espn
import pandas
import secret

league = espn.FantasyLeague(league_id=secret.league_id, year=2023, swid=secret.swid, espn_s2=secret.espn_s2)

player_data = league.get_league_data()
matchup_data = league.get_matchup_data()

player_data.to_csv("data/players.csv", index=False)
matchup_data.to_csv("data/matches.csv", index=False)
