import pygame
import numpy as np

class body:
    def __init__(self,screen,pos,mass,screen_width,screen_height, vel=[],gravity = 50) -> None:
        self.screen = screen
        self.pos = np.array(pos,dtype=float)
        self.radius = mass/2
        self.mass = mass
        self.acc = np.array([0,0],dtype=float)
        self.vel = vel if len(vel)>0 else np.random.uniform(-0.8, 0.8, 2)
        self.gravity = gravity
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = [255,255,255,100]
        self.max_pos = 100
        self.past =[]
        

    def magnitude(self,vector): 
        return np.linalg.norm(vector)
    def set_mag(self,arr,new_mag):
        mag = self.magnitude(arr)
        arr[0] = arr[0] * new_mag / mag
        arr[1] = arr[1] * new_mag / mag

    def move(self):
        if self.max_pos<len(self.past):
            self.past.pop(0)
        self.past.append(self.pos.copy())
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]

        # if self.pos[0]-self.radius<0 or self.pos[0]+self.radius>self.screen_width:
        #     if self.pos[0]-self.radius<0:
        #         self.pos[0] = self.radius
        #     else: 
        #         self.pos[0] = self.screen_width-self.radius
        #     self.vel[0] = 0.9*self.vel[0]* -1
        #     # self.acc[0] =0.0

        # if self.pos[1]-self.radius<0 or self.pos[1]+self.radius>=self.screen_height:
        #     if self.pos[1]-self.radius<0:
        #         self.pos[1] = self.radius
        #     else: 
        #         self.pos[1] = self.screen_height-self.radius
        #     self.vel[1] =0.9*self.vel[1]* -1
            # self.acc[1] =0.0

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
    def draw_past(self):
        color = self.color.copy()
        sub = int(255/self.max_pos)
        for pos in reversed(self.past):
            if color[3]>sub:
                color[3]-=sub
            target_rect = pygame.Rect(pos, (0, 0)).inflate((self.radius * 2, self.radius * 2))
            shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
            pygame.draw.circle(shape_surf,color,(self.radius,self.radius),self.radius)
            self.screen.blit(shape_surf, target_rect)
    def draw(self,past=False):
        target_rect = pygame.Rect(self.pos, (0, 0)).inflate((self.radius * 2, self.radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surf,self.color,(self.radius,self.radius),self.radius)
        self.screen.blit(shape_surf, target_rect)
        if past:
            self.draw_past()

    def constrain(self,value,min,max):
        if value<min:
            return min
        if value>max:
            return max
        return value
    def atract(self,atracted):
        force = self.pos-atracted.pos
        destanceSq = self.constrain(self.magnitude(force)**2,100,200)
        strength = (self.gravity*(self.mass * atracted.mass))/destanceSq
        self.set_mag(force,strength)
        atracted.applyForce(force)
        # print(dir)
        # print(destanceSq)

    def applyForce(self,force):
        # print((force/self.mass))
        # print(self.acc)
        self.acc = (force/self.mass)
        # print(self.acc)