#import 
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

#pull data
stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season="2026-27",
    measure_type_detailed_defense="Advanced"
)
df = stats.get_data_frames()[0]
print(df.head())
hawks = df[df["TEAM_ABBREVIATION"] == "ATL"]
hawks.to_csv("data/hawks_advanced.csv", index=False)

basic = leaguedashplayerstats.LeagueDashPlayerStats(
    season="2026-27",
    measure_type_detailed_defense="Base",
    per_mode_detailed="PerGame"
)

#filter hawks 
hawks = df[df["TEAM_ABBREVIATION"] == "ATL"]
print(hawks[["PLAYER_NAME", "GP", "MIN"]])
hawks = df[df["TEAM_ABBREVIATION"] == "ATL"]

#save to csv
hawks.to_csv("data/hawks_advanced.csv", index=False)





