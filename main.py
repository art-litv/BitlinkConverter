import requests
from dotenv import load_dotenv
import os
import argparse

HEADERS = {
  'Authorization': 'Bearer {0}'
}


def shorten_link(headers, long_url, group_guid=None, domain=None):
  '''Returns bitlink from long link'''
  payload = {
    'long_url': long_url,
    'group_guid': group_guid,
    'domain': domain
  }
  response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=payload)
  response.raise_for_status()
  return response.json()['link'].strip('https://')


def count_bitlink_clicks(headers, bitlink, unit="day", units=-1):
  '''Returns sum of clicks on bitlink'''
  payload = {
    'unit': unit,
    'units': units
  }
  response = requests.get(
    f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
    headers=headers,
    params=payload
    )
  response.raise_for_status()
  return response.json()['total_clicks']


def main():
  load_dotenv()
  HEADERS['Authorization'] = HEADERS['Authorization'].format(os.getenv("BITLY_TOKEN"))
  parser = argparse.ArgumentParser()
  parser.add_argument("link", help="link to create a bitlink or bitlink to see sum of clicks")
  url = parser.parse_args().link
  if url.startswith("bit.ly/"):
    clicks_count = None
    try:
      clicks_count = count_bitlink_clicks(HEADERS, url)
      print('Sum of clicks on the bitlink', clicks_count)
    except requests.exceptions.HTTPError:
      print("Your link or token is not correct")
  else:
    bitlink = None
    try:
      bitlink = shorten_link(HEADERS, url)
      print('Bitlink', bitlink)
    except requests.exceptions.HTTPError:
      print("Your link or token is not correct")


if __name__ == '__main__':
  main()
