from body import body
import time
import pygame
import numpy as np
import random

pygame.init()
size = width, height =  800,800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
gravity = 1
min_size=2
max_size=20
n_bodys =20

bodys = []
for i in range(n_bodys):

    bodys.append(body(screen,[random.uniform(max_size+1,width-max_size),random.uniform(max_size+1,height-max_size)],random.uniform(min_size,max_size),width, height,gravity=gravity))
    bodys[-1].color=[random.randint(0,255),random.randint(0,255),random.randint(0,255),200]
# bodys = [body(screen,[300,300],50,width, height,gravity=gravity,vel=np.array([0.0,10.0]))]
# bodys[0].radius=10


# bodys.append(body(screen,[400,400],100,width, height,gravity=gravity,vel=np.array([0.0,0.0])))
# bodys[-1].radius=3
# bodys[-1].color=[255,0,0,200]

screen.fill((0,0,0))
flip=30
while True:
    # for event in pygame.event.get():
    #     # handle MOUSEBUTTONUP
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         x,y = pygame.mouse.get_pos()
    #         print(x,y)
    #         bodys[-1].pos = np.array([x,y],dtype=float)

    screen.fill((0,0,0))
    for mover in bodys:
        for other in bodys:
            if mover != other:
                mover.atract(other)   
                    # time.sleep(10)


    for b in bodys:
        # if not b == bodys[0]:
        #     b.move()
        # else:
        #     bodys[0].vel = np.array([0.0,0.0])
        #     bodys[0].acc = np.array([0.0,0.0])
        b.move()
        b.draw(True)
    
    pygame.display.update()
    # time.sleep(0.1)
    clock.tick(60)
    # print(clock.get_fps())
    
