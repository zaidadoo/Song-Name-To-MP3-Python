from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

mp3 = MP3File("music/binki - Wiggle.mp3")

default_filename = "binki - Wiggle"

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
	
	singer = singer.replace(" ", "")
	title = title.replace(" ", "")
	
	mp3.artist = singer
	mp3.song = title
	mp3.album = ""
	mp3.comment = ""
	
	mp3.save()
	
	
