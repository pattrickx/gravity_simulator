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
min_size=8
max_size=30
n_bodys = 50
bodys = [ body(screen,[random.uniform(max_size+1,width-max_size),random.uniform(max_size+1,height-max_size)],random.uniform(min_size,max_size),width, height,gravity=gravity) for i in range(n_bodys)]

# bodys = [body(screen,[50,50],50,width, height,gravity=gravity)]
# bodys[0].radius=10

bodys.append(body(screen,[400,400],500,width, height,gravity=gravity,vel=np.array([0.0,0.0])))
bodys[-1].radius=10
bodys[-1].color=(255,0,0,255)


while True:
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
        b.draw()

    pygame.display.update()
    # time.sleep(0.1)
    clock.tick(60)
    # print(clock.get_fps())
    
