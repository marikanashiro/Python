#Faça um programa que abra e reproduza um áudio MP3

import pygame
pygame.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()
pygame.event.wait()