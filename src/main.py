import logging
from fastapi import FastAPI, Form
from nba_api_client import get_lineups_by_team
from sms import print_message

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


@app.get("/get_lineups/{team_id}")
async def get_lineups(team_id: str):
    return await get_lineups_by_team(team_id)


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.post("/sms")
async def sms(Body: str = Form(...), From: str = Form(...), **kwargs):
    print(f"Received message: {Body}")
    print(f"From number: {From}")
    return {"message": "Message received."}
