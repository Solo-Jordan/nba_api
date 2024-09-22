import logging
from fastapi import FastAPI, Request
from nba_api_client import get_lineups_by_team
from sms import print_message
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


@app.get("/get_lineups/{team_id}")
async def get_lineups(team_id: str):
    return await get_lineups_by_team(team_id)


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.post("/sms")
async def sms(request: Request):
    form_data = await request.form()
    body = form_data.get("Body", "")
    from_number = form_data.get("From", "")

    print(f"Received message: {body}")
    print(f"From number: {from_number}")

    # You can access other parameters as needed
    # For example: to_country = form_data.get("ToCountry")

    return JSONResponse(content={"message": "Message received."}, status_code=200)
