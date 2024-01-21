#!/usr/bin/env python3

import hashlib
import requests
import sys
import time

URL = 'https://report.update.example.io'
DELAY = 10 * 60 # 10 minutes

def fetch_url(url: str) -> str:
    """This function fetches the contents of a URL"""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve the website. Status code: {response.status_code}")

def hash_url(url: str) -> str:
    """This function returns the SHA-256 hash of data"""
    body_data = fetch_url(url)
    return hashlib.sha256(body_data.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    last_hash = None
    while True:
        try:
            current_hash = hash_url(URL)
            if last_hash is None:
                last_hash = current_hash
                print('Initial hash recorded: {}, {}'.format(last_hash, time.ctime()))
            elif last_hash != current_hash:
                last_hash = current_hash
                print('Website changed! {}, {}'.format(last_hash, time.ctime()))
                sys.exit(0)
            else:
                print('Polling again in {} minutes, {}'.format(DELAY//60, time.ctime()))
            time.sleep(DELAY)            
        except Exception as e:
            print(e)
            sys.exit(1)