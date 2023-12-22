import logging
from fastapi import FastAPI
from nba_api_client import get_lineups_by_team

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


@app.get("/get_lineups/{team_id}")
async def get_lineups(team_id: str):
    return await get_lineups_by_team(team_id)


@app.get("/ping")
async def ping():
    return {"message": "pong"}