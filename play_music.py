import pygame
from pygame import mixer


pygame.init()

current_song = ""
current_music = ""
sound_channel = 0
def play_music(music_name):
	global current_music
	if(current_music == music_name):
		return
	else:
		try:
			music_path = 'music/' + music_name + '.wav'
			mixer.music.load(music_path)
			mixer.music.fadeout(2000)
			mixer.music.play(-1)
			current_music = music_name
		except:
			pass

def play_sound(song_name):
	global current_song
	global sound_channel
	if(current_song == song_name):
		return
	else:
		try:
			song_path = 'sound/' + song_name + '.wav'
			sound = mixer.Sound(song_path)
			mixer.Channel(sound_channel).fadeout(2000)
			mixer.Channel((sound_channel + 1)%2).play(sound,-1, fade_ms = 2000)
			#mixer.music.load(song_path)
			#mixer.music.fadeout(1500)
			#mixer.music.play(-1)
			current_song = song_name
			sound_channel = (sound_channel + 1) % 2
		except:
			pass

def stop_sound():
	global current_song
	current_song = ""
	mixer.Channel(0).stop()
	mixer.Channel(1).stop()
