import logging
from nba_api.stats.endpoints import leaguedashlineups
import httpx
from fastapi import HTTPException


logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()], format='%(asctime)s - %(levelname)s - %('
                                                                                    'message)s')


async def get_lineups_by_team(team_id):
    try:
        logging.debug('Fetching lineup for team_id: %s', team_id)
        team_id_int = int(team_id)
        data = leaguedashlineups.LeagueDashLineups(
            team_id_nullable=team_id_int,
            measure_type_detailed_defense='Advanced'
        ).get_data_frames()[0]
        logging.debug('Data fetched successfully')
        return data.to_dict('records')
    except ValueError as e:
        logging.exception('ValueError occurred with team_id: %s', team_id)
        raise HTTPException(status_code=400, detail='Invalid TeamID format.')
    except httpx.HTTPError as e:
        logging.exception('HTTPError when calling NBA API')
        raise HTTPException(status_code=503, detail='NBA API service unavailable')
    except Exception as e:
        logging.exception('Unexpected error')
        raise HTTPException(status_code=500, detail='Server Error')