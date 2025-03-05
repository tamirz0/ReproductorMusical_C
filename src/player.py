#
#   Funciones basicas para cargar, reproducir, pausar, detener
#   ajustar volumen y cambiar de cancion.
#
from pygame import mixer

def init():
    mixer.init()

def load_song(song):
    mixer.music.load(song)

def unload_song():
    mixer.music.unload()

def play_song():
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)


def get_volume():
    return mixer.music.get_volume()

def quit():
    mixer.quit()


    