import tweepy
from textblob import TextBlob
import re
import os

class TwitterClientV2:
    def __init__(self):
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

        try:
            self.client = tweepy.Client(bearer_token=self.bearer_token)
        except Exception as e:
            print('Error: Authentication Failed')

    def clean_tweet(self, tweet):
        return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, max_results=10):
        tweets = []
        try:
            response = self.client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['text'])

            if not response.data:
                return []

            for tweet in response.data:
                parsed_tweet = {
                    'text': tweet.text,
                    'sentiment': self.get_tweet_sentiment(tweet.text)
                }
                tweets.append(parsed_tweet)

            return tweets

        except Exception as e:
            print(f"Error fetching tweets: {e}")
            return []

def main():
    api = TwitterClientV2()
    tweets = api.get_tweets("Donald Trump", max_results=15)

    if not tweets:
        print("No tweets retrieved.")
        return

    pos_tweets = [t for t in tweets if t['sentiment'] == 'positive']
    neg_tweets = [t for t in tweets if t['sentiment'] == 'negative']
    neu_tweets = [t for t in tweets if t['sentiment'] == 'neutral']

    print(f"Positive: {100 * len(pos_tweets) / len(tweets):.2f}%")
    print(f"Negative: {100 * len(neg_tweets) / len(tweets):.2f}%")
    print(f"Neutral: {100 * len(neu_tweets) / len(tweets):.2f}%")

    print("\nSample positive tweets:")
    for t in pos_tweets[:3]:
        print(t['text'])

    print("\nSample negative tweets:")
    for t in neg_tweets[:3]:
        print(t['text'])

if __name__ == '__main__':
    main()