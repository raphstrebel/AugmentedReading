import pygame
from pygame import mixer


pygame.init()

current_song = ""
song_to_path = {
	'dragon' : 'sound/dragon_shout.mp3',
	'rain' : 'sound/light_rain.mp3',
	'storm' : 'sound/rainy_storm.mp3'
}
def play_sound(song_path):
    global current_song
    if(current_song == song_path):
        return
    else:
        mixer.music.fadeout(1500)
        mixer.music.load(song_path)
        mixer.music.play(-1)
        current_song = song_path
