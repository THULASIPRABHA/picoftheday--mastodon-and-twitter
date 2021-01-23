import requests
from datetime import date

ENDPOINT = "https://commons.wikimedia.org/w/api.php"
SESSION = requests.Session()


def fetch_potd(cur_date):
    date_iso = cur_date.isoformat()
    title = "Template:Potd/" + date_iso
    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "images",
        "titles": title
    }

    response = SESSION.get(url=ENDPOINT, params=params)
    data = response.json()
    filename = data["query"]["pages"][0]["images"][0]["title"]
    image_page_url = "https://commons.wikimedia.org/wiki/" + title

    image_data = {
        "filename": filename,
        "image_page_url": image_page_url,
        "image_src": fetch_image_src(filename),
        "date": date_iso
    }

    return image_data


def fetch_image_src(filename):
  params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": filename
  }

  response = SESSION.get(url = ENDPOINT, params = params)
  data = response.json()
  page = next(iter(data["query"]["pages"].values()))
  image_info = page["imageinfo"][0]
  image_url = image_info["url"]

  return image_url



#imgdata=fetch_potd(cur_date=date.today())
#print(imgdata['image_src'])
def saveimg(imgdata):
    r = requests.get(imgdata, stream=True)
    if r.status_code == 200:
        with open("picoftheday.jpg", 'wb') as f:
            for chunk in r:
                f.write(chunk)