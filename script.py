import tweepy
import pandas as pd

API_KEY= "ZrimsE0GFJHux3IAV0U3yy7ny"
API_SECRET = "hWwFa9KiQXTLcnGGgERKNkHpzcqAZQNnjwn3x6yTyy4LYBAGdq"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHtRaQEAAAAA4nweYyYN2mvaMCdxF44hsiNOUy0%3DpWkvDTHBvNxm42CqIbqar43K8cDNySEvQsNvGe4Zu3A1tvRCaW"
ACCESS_TOKEN  = "947713694-MPC6UFhnXeysw1fUSZm8YmMfDFocOJUVJcPynpyx"
ACCESS_TOKEN_SECRET = "Uk0CYZeehCwwAJu1FkN2feYk3yG3Tn2dOgVDewuBELYdn"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

tweepy.API()
api = tweepy.API(auth, wait_on_rate_limit=True)
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET, return_type=dict, wait_on_rate_limit=True)

all = pd.read_csv("all_ids_join_PRO_only.csv")
new_col = []
for index, row in all[1000:6000].iterrows():
    tweet_id = row['id'] 

    try:
      retweeter_ids = api.get_retweeter_ids(id=tweet_id) #list id user yg ngeretweet
    except:
      retweeter_ids = []

    try:
      liked_ids = client.get_liking_users(id=tweet_id)
    except:
      liked_ids = []


    new_col.append([retweeter_ids, liked_ids])

pd.DataFrame(new_col).to_csv("1000,6000.csv", index=False)
