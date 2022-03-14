#import files and give access to tokens and keys
import tweepy,json

access_token = "*************************************************"
access_token_secret = "********************************************"
consumer_key = "**********************************************"
consumer_secret = "***********************************************"
auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

tweet_list=[]
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,count):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweetJSON3.txt","w")
        self.count = count
    def on_status(self,status):
        tweet=status._json
        self.file.write(json.dumps(tweet)+ '\n')
        tweet_list.append(status)
        self.num_tweets+=1
        if self.num_tweets<self.count:
            return True
        else:
            return False
        self.file.close()

#create streaming object and authenticate
count = int(input("enter number of tweets to be extracted : "))
l = MyStreamListener(count)
stream = tweepy.Stream(auth,l)
#this line filters twiiter streams to capture data by keywords
# stream.filter(track=['covid','corona','covid19','coronavirus','facemask','sanitizer','social-distancing'])
stream.filter(track=['election','elections','up','uttarakhand','upelection','uttarakhandelection','upelections','uttarakhandelections'], languages=['en'])
print("Done extracting tweets.")