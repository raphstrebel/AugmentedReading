import pygame
from pygame import mixer


pygame.init()

current_song = ""

def play_sound(song_name):
	global current_song
	if(current_song == song_name):
		return
	else:
		try:
			song_path = 'sound/' + song_name + '.wav'
			mixer.music.load(song_path)
			mixer.music.fadeout(1500)
			mixer.music.play(-1)
			current_song = song_path
		except:
			pass

def stop_sound():
	global current_song
	current_song = ""
	mixer.music.stop()

