from mastodon import Mastodon

def create():
    appname=input("Enter your App name : ")
    toot=Mastodon.create_app(appname, scopes=['read', 'write'], api_base_url="https://mastodon.online")
    return toot
    
def get_token(key,secret):

    api = Mastodon(key,secret,api_base_url="https://mastodon.online")
    username=input("Enter your Mastodon mailid : ")
    password=input("Enter your Mastodon password : ")
    
    token = api.log_in(username, password, scopes=["read", "write"])
    return token

def post(img,imgurl,img_page_url):
    keys=create()
    mastodon = Mastodon(
        access_token = get_token(keys[0],keys[1]),
        api_base_url = 'https://mastodon.online'
    )
    msg ="Image Link:{} \n Image Page:{} ".format(imgurl,img_page_url)
    media=mastodon.media_post(img, "image/jpeg")
    status=mastodon.status_post(msg,media_ids=media)
