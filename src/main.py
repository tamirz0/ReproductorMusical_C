#
#   Punto de entrada de la aplicacion
#

from player import *

def main():
    init()
    load_song("90.mp3")
    play_song()
    print(get_volume())
    old_sec = 0
    while(mixer.music.get_busy()):
        if old_sec != int(mixer.music.get_pos() / 1000):
            print('seconds: ', int(mixer.music.get_pos() / 1000))
            old_sec = int(mixer.music.get_pos() / 1000)
            # Implementar pygame.event.get() para manejar eventos + pygame.QUIT en pygame.event.get()
        pass
    unload_song()
    quit()

main()