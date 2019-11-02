import os
import sys
import requests
import datetime

from requests.exceptions import HTTPError

def get_rainfall():
  for URL in ['http://reg.bom.gov.au/fwo/IDV60901/IDV60901.94866.json']:
    try:
      response = requests.get(URL)
      response.raise_for_status()
    except HTTPError as HTTP_ERROR:
      print(f'HTTP error occurred: {HTTP_ERROR}')
    except Exception as ERROR:
      print(f'Non-HTTP error occured: {ERROR}')
    else:
      payload = response.json()
      query_header = payload["observations"]["header"][0]
      query_data = payload["observations"]["data"][0]
      print('Successful GET operation')
      print(f'{query_header["refresh_message"]}')
      print(f'Rain since 0900: {query_data["rain_trace"]}')
      print(f'Current Air Temperature: {query_data["air_temp"]}')

get_rainfall()