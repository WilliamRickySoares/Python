import pygame


print('\nFaça um programa em Python que abra e reproduza um audio de um arquivo MP3')
pygame.init()
pygame.mixer.music.load('hebrides.mp3')
pygame.mixer.music.play()
pygame.event.wait()
