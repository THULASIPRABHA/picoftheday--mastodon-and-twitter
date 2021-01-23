import tweepy
import os

def get_keys():
    consumer_key        = input("Enter Consumer key : ")
    consumer_secret     = input("Enter Consumer Secret : ")
    access_token        = input("Enter access token : ")
    access_secret       = input("Enter access secret : ")
    keys="{},{},{},{}".format(consumer_key,consumer_secret,access_token,access_secret)
    #keys={'consumer_key':consumer_key,'consumer_secret':consumer_secret,'access_token':access_token,'access_secret':access_secret}
    with open('twitterauth','w') as file:
        file.write(keys)
    return consumer_key,consumer_secret,access_token,access_secret
    

def load_keys():
    with open('twitterauth','r') as file :
        string=file.read()
        s=string.split(',')
    return s
    

def post_tweet(img,imgurl,img_page_url):
    if os.path.exists("twitterauth") :
        keys=load_keys()
    else:
        keys=get_keys()
     
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = tweepy.API(auth)
    
    msg ="Pic of the day \nImage Link:{} \n Image Page:{} ".format(imgurl,img_page_url)
    
    api.update_with_media(img,msg)
    
    
    
