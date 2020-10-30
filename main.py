import pygame
from pygame.locals import *
import numpy as np
import time

from draw_widjets import *

pygame.init()
screen = pygame.display.set_mode((480,320))
pygame.display.set_caption('test')
running = True

#vitesse
speed = pygame.font.Font(None,94).render("12",True,pygame.Color("#232323"))
speed_unity = pygame.font.Font(None,35).render("km/h",True,pygame.Color("#232323"))

#chrono
chrono = pygame.font.Font(None,50).render("00 : 00 : 00",True,pygame.Color("#232323"))

#rapport
gear = pygame.font.Font(None,94).render("N",True,pygame.Color(gear_color))

#FONCTIONS

def getGear(gear_selected, neutral):
    if gear_selected in range (1,7) and gear_selected != 0:
        print("une vitesse enclenchée")
        gear_color = "#A2A2A2"
    if gear_selected == 0:
        gear_color = "#36DB51"


def alert(text, valu):
    if valu == "warning":
        pygame.draw.rect(screen, (245,171,45), pygame.Rect(14, 44, 160, 40))
        alert_text = pygame.font.Font(None,25).render(text,True,pygame.Color("#000000"))
        screen.blit(alert_text,(27,55))
    elif valu == "danger":
        pygame.draw.rect(screen, (245,45,45), pygame.Rect(14, 44, 160, 40))
        alert_text = pygame.font.Font(None,25).render(text,True,pygame.Color("#000000"))
        screen.blit(alert_text,(27,55))
    elif valu == "success":
        pygame.draw.rect(screen, (45,245,85), pygame.Rect(14, 44, 160, 40))
        alert_text = pygame.font.Font(None,25).render(text,True,pygame.Color("#000000"))
        screen.blit(alert_text,(27,55))





#INITIALISATION DE L'INTERFACE (sans les informations)
screen.fill((255,255,255))
#black rect
pygame.draw.rect(screen, (0,0,0), pygame.Rect(10, 90, 164, 182))
#bottom bar
pygame.draw.rect(screen, (112,112,112), pygame.Rect(0, 286, 480, 34))
#top regime bar
pygame.draw.rect(screen, (222,222,222), pygame.Rect(9, 10, 462, 22))
#top regime bar line
pygame.draw.rect(screen, (112,112,112), pygame.Rect(9.5, 32.5, 462, 1))
#alert
pygame.draw.rect(screen, (245,171,45), pygame.Rect(14, 44, 160, 40))
#rapport engagé
pygame.draw.rect(screen, (0,0,0), pygame.Rect(178, 161, 70, 112))#bordure
pygame.draw.rect(screen, (255,255,255), pygame.Rect(180, 163, 66, 108))

screen.blit(speed,(301,181))
screen.blit(speed_unity,(380,200))

screen.blit(chrono,(187,46))
screen.blit(gear,(190, 191))

clock = pygame.time.Clock()
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_DOWN:
                value = value-1
            if event.key == K_UP:
                value = value+1
            if event.key == K_RIGHT:
                pitlimiter = not pitlimiter
                print("pit limiter activated")
            if event.key == K_LEFTPAREN:
                gear_selected = gear_selected + 1
                print("rapport +1")
            if event.key == K_z:
                print("rapport -1")
                gear_selected = gear_selected - 1


    gear_selected = str(gear_selected)

    value = str(value)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(250, 174, 190, 105))
    speed = pygame.font.Font(None,94).render(value,True,pygame.Color("#232323"))
    screen.blit(speed,(260,181))
    screen.blit(speed_unity,(390,200))
    value = int(value)

    alert("READY", "success")

    if value > 100:
        alert("HIGH SPEED", "danger")
    if pitlimiter == True:
        alert("PIT LIMITER", "warning")


    gear = pygame.font.Font(None,94).render(gear_selected,True,pygame.Color(gear_color))
    print(gear_selected)


    gear_selected = int(gear_selected)
    pygame.display.update()
    clock.tick(60)
pygame.display.quit()