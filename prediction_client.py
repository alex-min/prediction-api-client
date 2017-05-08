#!/usr/bin/env python3
import sys
import logging
import requests
from team_input import parse_team_file
from api import PredictionApi, PredictionApiException

def check_arguments():
    if len(sys.argv) != 3:
      logging.info("""
        -- Prediction API client --

        Returns the probability of teams winning by calling the Prediction API.

        Usage:
        $ {} <input file> <api host>

        The input file should have each teams separated with an ampersand.
        
        - Returns T if the probability is greater than 50%
        - Returns F otherwise
        Output example: TTFFFTFF
      """.format(sys.argv[0]))
      sys.exit(1)

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.getLogger("requests").setLevel(logging.WARNING)   

def get_teams_output(input_file, api_host):
    api = PredictionApi(host=api_host)
    try:
        teams = parse_team_file(input_file)
        for team_match in teams:
            probability = api.winning_probability_of(*team_match)
            if probability > 50:
                sys.stdout.write('T')
            else:
                sys.stdout.write('F')
    except (FileNotFoundError, PredictionApiException) as error:
        logging.error(str(error))
        sys.exit(1)
    except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
        logging.error("Unable to contact the api at {}.".format(api_host))   

def execute_client():
    setup_logging()
    check_arguments()
    get_teams_output(input_file=sys.argv[1], api_host=sys.argv[2])

if __name__ == '__main__':
    execute_client()

