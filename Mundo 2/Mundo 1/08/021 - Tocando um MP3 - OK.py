import os
import pygame
os.chdir('G:/Meu Drive/Programas/Python/Atividades/Mundo 1/08/')
pygame.init()
pygame.mixer.music.load('musiquinha.mp3')
pygame.mixer.music.play()
pygame.event.wait()