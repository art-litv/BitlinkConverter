import requests
from dotenv import load_dotenv
import os
import argparse


def shorten_link(token, long_url, group_guid=None, domain=None):
  '''Returns bitlink from long link'''
  HEADERS = {
    'Authorization': f'Bearer {token}'
  }
  payload = {
    'long_url': long_url,
    'group_guid': group_guid,
    'domain': domain
  }
  response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=HEADERS, json=payload)
  response.raise_for_status()
  return response.json()['link'].strip('https://')


def count_bitlink_clicks(token, bitlink, unit="day", units=-1):
  '''Returns sum of clicks on bitlink'''
  HEADERS = {
    'Authorization': f'Bearer {token}'
  }
  payload = {
    'unit': unit,
    'units': units
  }
  response = requests.get(
    f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
    headers=HEADERS,
    params=payload
    )
  response.raise_for_status()
  return response.json()['total_clicks']


def main():
  load_dotenv()
  TOKEN = os.getenv("BITLY_TOKEN")
  parser = argparse.ArgumentParser()
  parser.add_argument("link", help="link to create a bitlink or bitlink to see sum of clicks")
  url = parser.parse_args().link
  if url.startswith("bit.ly/"):
    clicks_count = None
    try:
      clicks_count = count_bitlink_clicks(TOKEN, url)
      print('Sum of clicks on the bitlink', clicks_count)
    except requests.exceptions.HTTPError:
      print("Your link or token is not correct")
  else:
    bitlink = None
    try:
      bitlink = shorten_link(TOKEN, url)
      print('Bitlink', bitlink)
    except requests.exceptions.HTTPError:
      print("Your link or token is not correct")


if __name__ == '__main__':
  main()

