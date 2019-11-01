import os
import sys
import requests
import ConfigParser
import datetime

def get_precip_today_in(config):
  API_URL = 'http://api.wunderground.com/api/{key}/conditions/q/{state}/{town}.json'
  r = requests.get(API_URL.format(key=config['api_key'],
                                  state=config['state'],
                                  town=config['town']))
  rainfall = None
  if r.ok:
    try:  
      rainfall = float(r.json()['current_observation']['precip_today_in'])
    except Exception as ex:
      rainfall = None
  return rainfall, r