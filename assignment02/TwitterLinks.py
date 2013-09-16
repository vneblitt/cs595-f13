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
        
        print("Michael Moore Tweets")
        print("")
        screen_name1 = "MMFlint"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name1 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Rachel Maddow Tweets")
        print("")
        screen_name2 = "maddow"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name2 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("New York Times Tweets")
        print("")
        screen_name3 = "nytimes"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name3 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Sesame Street Tweets")
        print("")
        screen_name4 = "sesamestreet"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name4 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("The Daily Show Tweets")
        print("")
        screen_name5 = "TheDailyShow"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name5 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Washington Post Tweets")
        print("")
        screen_name6 = "washingtonpost"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name6 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Barack Obama Tweets")
        print("")
        screen_name7 = "barackobama"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name7 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Cory Booker Tweets")
        print("")
        screen_name8 = "corybooker"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name8 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Joel Spolsky Tweets")
        print("")
        screen_name9 = "spolsky"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name9 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Governor Christie Tweets")
        print("")
        screen_name10 = "GovChristie"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name10 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Planned Parenthood Tweets")
        print("")
        screen_name11 = "PPact"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name11 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("National Zoo Tweets")
        print("")
        screen_name12 = "NationalZoo"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name12 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("United Nations")
        print("")
        screen_name13 = "UN"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name13 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Washington City Paper Tweets")
        print("")
        screen_name14 = "wcp"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name14 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Entertainment Weekly Tweets")
        print("")
        screen_name15 = "EW"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name15 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("TMZ Tweets")
        print("")
        screen_name16 = "TMZ"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name16 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("National Public Radio Tweets")
        print("")
        screen_name17 = "NPR"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name17 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Virginia Tech News Tweets")
        print("")
        screen_name18 = "vtnews"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name18 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("New York Public Library Tweets")
        print("")
        screen_name19 = "nypl"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name19 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Library of Congress Tweets")
        print("")
        screen_name20 = "librarycongress"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name20 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Chicago Sun Times Tweets")
        print("")
        screen_name21 = "Suntimes"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name21 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Chicago Tribune Tweets")
        print("")
        screen_name22 = "chicagotribune"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name22 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("USAgov Tweets")
        print("")
        screen_name23 = "USAgov"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name23 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("Harvard University Tweets")
        print("")
        screen_name24 = "Harvard"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name24 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("NFL Tweets")
        print("")
        screen_name25 = "nfl"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name25 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass

        print("")
        print("NPR News Tweets")
        print("")
        screen_name26 = "nprnews"
        count = "200"
        uri = "https://api.twitter.com/1.1/statuses/user_timeline.json?" + "screen_name=" + screen_name26 + "&count=" + count
        r = requests.get(uri, auth=oauth)
        l = r.json()
        for tweet in l:
            try:
                print(tweet['id'],tweet['entities']['urls'][0]['expanded_url'])
            except UnicodeEncodeError:
                pass
            except IndexError:
                pass
