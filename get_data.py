#import 
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

#pull data
stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season="2026-27",
    measure_type_detailed_defense="Base",
    per_mode_detailed="PerGame"
)
df = stats.get_data_frames()[0]
print(df.head())
per_mode_detailed="PerGame"
hawks = df[df["TEAM_ABBREVIATION"] == "ATL"]
hawks.to_csv("data/hawks_basic.csv", index=False)
