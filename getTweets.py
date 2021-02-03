import tweepy as tw
import csv
import KeysApiTwitter

consumer_key = KeysApiTwitter.consumer_key
consumer_secret = KeysApiTwitter.consumer_secret
access_token = KeysApiTwitter.access_token
access_token_secret = KeysApiTwitter.access_token_secret

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth = tw.AppAuthHandler(consumer_key, consumer_secret)

#auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)



csvFile = open('/home/said/Bureau/dataFrame2.csv', 'a')
csvWriter = csv.writer(csvFile)
# Define the search term and the date_since date as variables
search_words = "vaccin OR covid OR vacciner OR covid 19 OR covid-19 OR me vacciner OR #CovidVaccin OR #Covid-19Vaccin OR #VaccinCovid19"
date_since = "2021-01-05"
places = api.geo_search(query="France", granularity="country")
place_id = places[0].id
tweets = tw.Cursor(api.search,
              q=("place:%s" % place_id) + search_words + " -filter:retweets",
              lang="fr",
              since=date_since,
              tweet_mode='extended')
try:              
    for tweet in tweets.items():
     csvWriter.writerow([tweet.id_str, tweet.user.id, tweet.user.followers_count, tweet.user.friends_count, tweet.full_text, 
     tweet.retweet_count, tweet.favorite_count])
except tw.error.TweepError:
        pass