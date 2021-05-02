import requests
import urllib
import os
import time
import subprocess
from bs4 import BeautifulSoup
from pytube import YouTube
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

checkIn = open("nodownload.txt", "r")

if checkIn.read()=='1':
	with open('songs.txt', 'r') as fin:
		data = fin.read().splitlines(True)
	with open('songs.txt', 'w') as fout:
		fout.writelines(data[1:])

i = 0
names = []

f = open("songs.txt", "r")
for x in f:
	i = i + 1
	x = x.strip('\n')
	name = x
	names.append(name)

if i < 1:
	print('No songs founds in songs.txt')
	quit()
	
x = 0
	
while x < i:

	with open('nodownload.txt', 'w') as checkOut:
		checkOut.write('1')

	vids = []

	textToSearch = names[x]
	print('[',x + 1,'/',i,']')
	print('Song searching for: ' + textToSearch)
	query = urllib.parse.quote(textToSearch)
	print('getting link...')
	url = "https://www.youtube.com/results?search_query=" + query
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, features="html.parser")
	vids = soup.findAll(attrs={'class':'yt-uix-tile-link'})
	
	link = 'youtube.com' + vids[0]['href'] + '\n'
	
	print('Link found')
	print('\n')
	
	print('Sending youtube link to converter...')
	print('\n')
	
	print('Downloading video to storage...')
	print('\n')
	
	yt = YouTube(link)
	stream = yt.streams.get_by_itag('140')
	stream.download('videos/')
	
	default_filename = yt.title
	
	default_filename = default_filename.replace("/", "")
	default_filename = default_filename.replace(".", "")
	default_filename = default_filename.replace(",", "")
	default_filename = default_filename.replace("'", "")
	default_filename = default_filename.replace("\"", "")
	default_filename = default_filename.replace(";", "")
	default_filename = default_filename.replace(":", "")
	
	print('Waiting for video to convert to mp3...')
	print('\n')
	
	subprocess.call([
		'ffmpeg',
		'-i', 'videos/%s.mp4' % default_filename, 
		'music/%s.mp3' % default_filename
	])
	os.remove("videos/%s.mp4" % default_filename)
	
	print('\n')
	
	mp3 = MP3File('music/%s.mp3' % default_filename)
	
	if default_filename.find('-')==-1:
	
		mp3.artist = ""
		mp3.song = default_filename
		mp3.album = ""
		mp3.comment = ""
		
		mp3.save()
		
	else:
	
		splitter = default_filename.split('-', 1)
		
		singer = splitter[0]
		title = splitter[1]
		
		mp3.artist = singer
		mp3.song = title
		mp3.album = ""
		mp3.comment = ""
		
		mp3.save()
	
	print('Song converted successfully...')
	print('\n')
	
	with open('nodownload.txt', 'w') as checkOut:
		checkOut.write('0')
	
	with open('songs.txt', 'r') as fin:
		data = fin.read().splitlines(True)
	with open('songs.txt', 'w') as fout:
		fout.writelines(data[1:])
	
	x = x + 1
print('Download done.')
input()
os.system("pause")