import logging
from fastapi import FastAPI, Request
from nba_api_client import get_lineups_by_team
from sms import forward_message
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


@app.get("/get_lineups/{team_id}")
async def get_lineups(team_id: str):
    return await get_lineups_by_team(team_id)


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.post("/sms/")
async def sms(data: dict):
    logging.info(f"Received SMS: {data['data']['payload']['text']}")
    logging.info(f"From: {data['data']['payload']['from']['phone_number']}")
    if data['data']['payload']['from']['phone_number'] != "+18339300814":
        forward_message(data['data']['payload']['from']['phone_number'], data['data']['payload']['text'])

    return JSONResponse(content={"message": "Message received."}, status_code=200)
