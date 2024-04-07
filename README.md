# nba_api
This is a FastAPI app that can be used as a wrapper for the NBA API. 

This repo is updated on my mac and deployed manually to my server. Go to solo-server and in `~/repos/nba_api` run `git pull`. Then run `docker build -t jordanmsmithemail/nba_api .` and `docker run -itd -p 8153:8000 jordanmsmithemail/nba_api`.