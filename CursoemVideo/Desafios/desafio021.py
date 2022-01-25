import pygame

while True:
    print('\nFaça um programa em Python que abra e reproduza um audio de um arquivo MP3')
    pygame.init()
    pygame.mixer.music.load('moolight.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
# TODO: Verificar forma de parar o script depois da execução do arquivo de áudio
