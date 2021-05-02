from pytube import YouTube
import os
import subprocess

yt = YouTube('https://www.youtube.com/watch?v=TcPkfhEerZw')
stream = yt.streams.get_by_itag('140')
stream.download('videos/')

#print("The song is %s" % yt.title)

default_filename = yt.title
default_filename = default_filename.replace("/", "")
default_filename = default_filename.replace(".", "")
print(default_filename)
subprocess.call([
	'ffmpeg',
	'-i', 'videos/%s.mp4' % default_filename, 
	'music/%s.mp3' % default_filename
])
os.remove("videos/%s.mp4" % default_filename)