# reset_pipeline.py
from dlt import pipeline, resource
from dotenv import load_dotenv
import requests
import os
from datetime import datetime

load_dotenv()
# Read environment variables
API_KEY = os.environ["FOOTBALL_API_KEY"]
DB_NAME = os.environ.get("DB_NAME", "football_analytics")

# Define football matches resource
@resource
def football_matches():
    url = "https://api.football-data.org/v4/competitions/PL/matches"
    headers = {"X-Auth-Token": API_KEY}
    data = requests.get(url, headers=headers).json().get("matches", [])
    for match in data:
        yield {
            "match_id": match["id"],
            "competition": match["competition"]["name"],
            "season": f"{match['season']['startDate']}-{match['season']['endDate']}",
            "utc_date": match["utcDate"],
            "home_team": match["homeTeam"]["name"],
            "away_team": match["awayTeam"]["name"],
            "home_score": match["score"]["fullTime"]["home"],
            "away_score": match["score"]["fullTime"]["away"],
            "status": match["status"],
            "fetched_at": datetime.utcnow()
        }

# Create pipeline in dev_mode=True to reset state
football_pipeline = pipeline(
    pipeline_name="football_pipeline",
    destination="motherduck",
    dataset_name=f"{DB_NAME}.stg_matches",
    dev_mode=True  # full refresh / reset pipeline state
)

# Run pipeline once to clear state and create tables
football_pipeline.run(football_matches())

print("Pipeline reset complete. Resource tables created.")
