import potd 
import posttoot
import tweet
from datetime import date
from PIL import Image
#extract pic of the day
imgdata=potd.fetch_potd(cur_date=date.today())
imgsrc=imgdata['image_src']
pageurl=imgdata['image_page_url']

potd.saveimg(imgsrc)
#toot
posttoot.post("picoftheday.jpg",imgsrc,pageurl)
print("Sucessfully posted your toot")
#tweet
img = Image.open("picoftheday.jpg")       
w=img.width
h=img.height
if w>=800 and h>=500:
    new_wid = 500
    new_heig=300
    img1 = img.resize((new_wid,new_heig),Image.ANTIALIAS).show()
img.save("resize.jpg")
tweet.post_tweet("resize.jpg",imgsrc,pageurl)
print("Sucessfully posted your tweet")
