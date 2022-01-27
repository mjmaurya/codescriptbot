import tweepy
import time
print("this is my twitter")

CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_KEY=""
ACCESS_SECRET=""

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)

FILE_NAME="lasthash.txt"
def retrieve_last_id(filename):
    f_read=open(filename,'r')
    last_id=int(f_read.read().strip())
    f_read.close()
    return last_id

def store_last_id(filename,last_id):
    f_write=open(filename,'w')
    f_write.write(str(last_id))
    f_write.close
    return

def action():    
    last_id=retrieve_last_id(FILE_NAME)
    timelines=api.home_timeline(last_id,
                                tweet_mode='extended')


    for timeline in reversed(timelines):
        last_id=timeline.id
        store_last_id(FILE_NAME,last_id)
        if "#codescript" or "#webdevelopment" in timeline.text.lower():
            print('responding...')
            api.retweet(timeline.id)
            print('@'+timeline.user.screen_name+" Awesome",timeline.id)
            print(timeline.id)
while True:
    action()
    time.sleep(15)
