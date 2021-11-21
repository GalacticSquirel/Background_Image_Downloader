from pexels_api import API
from urllib.request import Request
import urllib.request
import os
import pyautogui
import glob

user_screen_width, user_screen_height= pyautogui.size()

PEXELS_API_KEY = "563492ad6f91700001000001cca20aa6588242adb99a5a4756a5834b"
amount=input("Amount")
amount = int(amount)
if amount <= 10:
    page_size = 10
elif amount <=20:
    page_size = 20
elif amount <= 30:
    page_size = 30
elif amount <= 40:
    page_size = 40
elif amount <= 50:
    page_size = 50
elif amount <= 60:
    page_size = 60
elif amount <= 70:
    page_size = 70
else:
    page_size = 80
path = os.getcwd()
jpgs = [os.path.join(path, file)
        for file in os.listdir(path)
        if file.endswith('.jpeg') or file.endswith('.jpg')]
i = len(jpgs)/page_size
i = round(i)
print("Starting at...", i)
api = API(PEXELS_API_KEY)
api.search('night sky lake space river sunset sunrise', results_per_page=page_size, page=i)
photos = api.get_entries()

photos = []
i =+ i
while len(photos) < int(amount):
    api.search('night sky', results_per_page=page_size, page=i)
    photo_list = api.get_entries()
    for photo in photo_list:
        filename = photo.original.split("/")[5]
        url = photo.original + "?auto=compress&cs=tinysrgb&fit=crop&h=" + str(user_screen_height) + "&w=" + str(user_screen_width)
        if not filename in os.listdir() and not filename in photos:
            photos.append(url)
    i = i + 1


for photo in photos:
    filename = photo.split("/")[5].split("?")[0]
    req = Request(photo, headers={'User-Agent': 'Mozilla/5.0'})
    resource = urllib.request.urlopen(req)
    output = open(filename,"wb")
    output.write(resource.read())
    output.close()
