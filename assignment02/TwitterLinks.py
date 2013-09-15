# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "tJddXvSjQTw2RVzhcs22VQ"
CONSUMER_SECRET = "DL9PQntlfAxnk4Z6lxh51LwRbrkKYyuko5nrN3LUQ"

OAUTH_TOKEN = "34775622-NPSdzhU22Oc5Xcx6DVVEwHnyVALoK0F4lkrvxvx04"
OAUTH_TOKEN_SECRET = "z2UkULqtyCOH4DzBBtHbJ0ohF8zEx4BkCssjuFR6hQ"


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)

    credentials = parse_qs(r.content)

    resource_owner_key = credentials[b'oauth_token'][0].decode(encoding='UTF-8')
    resource_owner_secret = credentials[b'oauth_token_secret'][0].decode(encoding='UTF-8')
    
    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print('Please go here and authorize: ' + authorize_url)
    
    verifier = input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials[b'oauth_token'][0].decode(encoding='UTF-8')
    secret = credentials[b'oauth_token_secret'][0].decode(encoding='UTF-8')

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print( "OAUTH_TOKEN: " + token )
        print( "OAUTH_TOKEN_SECRET: " + secret )
        print( )
    else:
        oauth = get_oauth()
        screen_name1 = "MMFlint"
        count = "200"
        max_id = "1000000000000000000"
            uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name1 + "&count=" + count + "&" + max_id
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            print(tweet['id'],tweet['text'])              
        print(len(l))
