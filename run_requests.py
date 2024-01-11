import requests
import os

import time
import datetime
import pandas


if not os.path.exists("html_files"):
	os.mkdir("html_files")


access_point = ("https://www.truecar.com/used-cars-for-sale/listings/location-clemson-sc/")


#lecture code on github
headers = {
  'accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
  'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
  'referer': 'https://www.google.com/'
}


for i in range(1,3):
	url = access_point + "?page=" + str(i)
	#gives us time, change format to make more useful(strftime into any format we want)
	current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time)

	#put time stamp to make each file unique
	f = open("html_files/" + "truecar_" + str(i) + "_" + current_time + ".html", "w")	

	#add header so website doesn't know you are a program
	req = requests.Session()
	response = req.get(url, headers = headers)
	html = response.text

	f.write(html)
	f.close()

	print("waiting")
	time.sleep(15)









	