import potd 
import posttoot
import tweet
from datetime import date
from PIL import Image
from resizeimage import resizeimage
#extract pic of the day
imgdata=potd.fetch_potd(cur_date=date.today())
imgsrc=imgdata['image_src']
pageurl=imgdata['image_page_url']

potd.saveimg(imgsrc)


#fileconvertion
fd_img = open("picoftheday.jpg", 'rb')
img = Image.open(fd_img)    
img = resizeimage.resize_contain(img, [1280, 1280])
img.save("resize.png", img.format)
fd_img.close()
#toot
posttoot.post("resize.png",imgsrc,pageurl)
print("Sucessfully posted your toot")
tweet.post_tweet("resize.png",imgsrc,pageurl)
print("Sucessfully posted your tweet")
