import tweepy
import textblob
import pandas as pd
import matplotlib.pyplot as plt
import re
from array import *

api_key = 'SeSHtUbPmmuKvzudEu0sCjwhE'
api_key_secret = 'pNfT1G0W1c8Dm2fUYWGVFDHdImIQTXH9uUtcEWddQsXEY5ZlG0'
access_token = '1424397060573319171-To50fBUUtzEeHUebxwzwgyuhGp4VMl'
access_token_secret = 'KLF8KFFVQUNaUB7ZghgoAKGGSeD3UNRfiHHtgWwf005wY'

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)


b=array('i',[])
for i in range(2):
    a=input(print("enter player name"))

    search= f'#{a} -filter:retweets lang:en'

    tweet_cursor = tweepy.Cursor(api.search_tweets, q=search, tweet_mode='extended').items(10)

    tweets = [tweet.full_text for tweet in tweet_cursor]

    tweets_df = pd.DataFrame(tweets, columns=['Tweets'])

    for _, row in tweets_df.iterrows():
        row['tweets'] = re.sub('https\S+', '', row['Tweets'])
        row['tweets'] = re.sub('#\S+', '', row['Tweets'])
        row['tweets'] = re.sub('@\S+', '', row['Tweets'])
        row['tweets'] = re.sub('\\n', '', row['Tweets'])
    #print(tweets_df)
    #print(tweets)


    tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
    tweets_df['Result'] = tweets_df['Polarity'].map(lambda pol: '+' if pol > 0 else '-')

    positive = tweets_df[tweets_df.Result == '+'].count()['Tweets']
    negative = tweets_df[tweets_df.Result == '-'].count()['Tweets']
#    print(b)
    b.append(positive)
    print(positive)
    print(negative)
    langs = ['Positive', 'Negative']
    students = [positive,negative]
    a=plt.bar(langs,students)
    a[0].set_color('g')
    a[1].set_color('r')

    plt.xlabel("Tweet Sentiment")
    plt.ylabel("No. of Tweets")
    plt.title("Sentiment Analysis")
    plt.legend

    plt.show()
    print(i)

if(b[0]>b[1]):
    print('player 1 is better')

else:
    print('player 2 is better' )
