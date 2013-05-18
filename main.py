import random
import pygame
from classes import *
from rand import *

colors = {'black':(0,0,0),'white':(255,255,255), 'grey':(100,100,100)}

pygame.init()
class Systema(object):
    hovered = False
    counter = []
    
    def __init__(self, dim1, dim2,parent):
        self.id = Systema.systid()
        self.dimensions = [dim1, dim2]
        self.output = Systema.speak(dim1,dim2)
        self.position = randomposition(parent.grid['end'][0],parent.grid['end'][1])
        self.set_rect()
        self.plane = parent.plane
        
    def draw(self):
        self.set_rend()
        self.set_circ()
        self.plane.blit(self.rend, self.rect)
            
        
    def set_rend(self):
        self.rend = menu_font.render(str(self.position), True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return colors['grey']
        else:
            return colors['white']
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.position
        
    def set_circ(self):
        self.circ = pygame.draw.circle(self.plane, colors['white'], self.position, 3)
                        
    @staticmethod
    def systid():
        try:
            syst.counter.append(len(syst.counter)+1)
        except NameError:
            print 'Error'
            return None
              
        return len(Systema.counter)

    @staticmethod
    def speak(dim1,dim2):
        if dim1 == dim2:
            return 1
        if dim1 == 0:
            return 0
        else:
            return dim2 + dim1
        

class MegaSystema(object):
    def __init__(self,n):
        self.subs = []
        self.grid = {'start':(0,0),'end':(400,400)}     #should go in supersystem class
        self.colors = {'black':(0,0,0),'white':(255,255,255)}
        self.plane = pygame.display.set_mode(self.grid['end'])
        for i in range(n):
            mid = []
            for f in range(2):
                mid.append(Systema(random.randint(0,1),random.randint(0,1),self))
            self.subs.append(Systema(mid[0].output,mid[1].output,self))
            
    def viewsys(self):

        
       
        menu_font = pygame.font.Font(None, 1)
        clock = pygame.time.Clock()
        done = False
        
        while not done:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True            # QUIT
    
            msElapsed = clock.tick(30)
            self.plane.fill(colors['black'])
                
            
            for syst in self.subs:
                if syst.rect.collidepoint(pygame.mouse.get_pos()):
                    syst.hovered = True
                else:
                    syst.hovered = False
                    syst.draw()    
            pygame.display.update()



menu_font = pygame.font.Font(None, 40)
def pickrandom(obj):
    if obj != int:
        while len(obj) >0:
            pick = obj[random.randint(0,len(obj)-1)]
            return 'Randomly selected', pickrandom(obj.remove(pick))


def randomposition(x,y):
    return (random.randint(0,x),random.randint(0,y))

test = MegaSystema(10)
test.viewsys()