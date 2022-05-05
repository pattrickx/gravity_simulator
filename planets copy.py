from body import body
import time
import pygame
import numpy as np

pygame.init()
size = width, height =  800,800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
gravity = 1
min_size=2
max_size=20
n_bodys =20
bodys=[]
bodys = [body(screen,[700,430],1,width, height,gravity=gravity,vel=np.array([-5.0,-41.0]))]
bodys[-1].radius=4
bodys[-1].color=[151, 151, 159,200]

bodys.append(body(screen,[700,400],30,width, height,gravity=gravity,vel=np.array([0.0,-40.0])))
bodys[-1].radius=10
bodys[-1].color=[96, 129, 255,200]

bodys.append(body(screen,[400,400],1000,width, height,gravity=gravity,vel=np.array([0.0,0.01])))
bodys[-1].color=[255, 204, 51,200]
bodys[-1].radius=30


screen.fill((0,0,0))
flip=30
while True:
    screen.fill((0,0,0))
    for mover in bodys:
        for other in bodys:
            if mover != other:
                mover.atract(other)   
                    # time.sleep(10)


    for b in bodys:
        if b != bodys[-1]:
            b.move()
        b.draw()
    
    pygame.display.update()
    time.sleep(0.08)
    clock.tick(120)
    
