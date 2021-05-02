import requests
import urllib
import os
import selenium
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_experimental_option("prefs", {
  "download.prompt_for_download": False,
})

options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver.exe')

open('nodownload.txt', 'w').close()


i = 0
names = []

f = open("songs.txt", "r")
for x in f:
	i = i + 1
	x = x.strip('\n')
	name = x
	names.append(name)

if i < 1:
		print('no songs founds in songs.txt')
		quit()
	
x = 0
	
while x < i:
	vids = []

	textToSearch = names[x]
	print('[',x + 1,'/',i,']')
	print('song searching for: ' + textToSearch)
	query = urllib.parse.quote(textToSearch)
	print('getting link...')
	url = "https://www.youtube.com/results?search_query=" + query
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, features="html.parser")
	vids = soup.findAll(attrs={'class':'yt-uix-tile-link'})
	
	link = 'youtube.com' + vids[0]['href'] + '\n'
	print('link found')
	
	print('sending youtube link to converter...')

	driver.get('https://2conv.com/')
	id_box = driver.find_element_by_id('convertUrl')
	id_box.send_keys(link)
	
	print('waiting for song to convert to mp3...')
	
	checker = "true"
	
	while checker == "true":
		try:
			elements = driver.find_element_by_partial_link_text('feedback')
		except NoSuchElementException:
			checker = "true"
		for elements in driver.find_elements_by_partial_link_text('feedback'):
			if elements.text == "send feedback":
				checker = "false"
				print('could not download ' + names[x])
				file = open("nodownload.txt","a")
				file.write(names[x] + "\n")
				file.close()
		urls = driver.current_url
		if "downloads/mp3" in urls:
			checker = "false"
			
	if "downloads/mp3" in urls:
		print('download commencing...')
		download = driver.find_element_by_class_name('text')
		download.click()
	x = x + 1
print('download done, check nodownload.txt in case any songs didnt download, and please make sure you saved these links as executing another search will delete the old nodownload.txt')
quit()