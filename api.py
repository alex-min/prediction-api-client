import requests

class PredictionApiException(Exception):
    pass

class PredictionApi():
    def __init__(self, host):
        self.host = host
    def winning_probability_of(self, team1, team2):
        try:
            endpoint = "{}/api/prediction".format(self.host)
            if 'http://' not in endpoint:
              endpoint = "http://{}".format(endpoint)
            api_result = requests.get(endpoint, params={'teams[]':[team1, team2]})
            if api_result.status_code != 200:
                error = "Got a {} status from the API: {}".format(api_result.status_code, api_result.text)
                raise PredictionApiException(error)
            return int(api_result.text)
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as error:
          raise PredictionApiException(str(error))
        except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
          raise PredictionApiException("Unable to contact the api at {}.".format(self.host))

