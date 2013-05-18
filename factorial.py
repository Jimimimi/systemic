import random
import pygame
import sys



grid = {'start':(0,0),'end':(400,400)}     #should go in supersystem class




colors = {'black':(0,0,0),'white':(255,255,255)}

def pickrandom(obj):
    if obj != int:
        while len(obj) >0:
            pick = obj[random.randint(0,len(obj)-1)]
            return 'Randomly selected', pickrandom(obj.remove(pick))

def randomposition(x,y):
    return (random.randint(0,x),random.randint(0,y))


class syst(object):
    counter = []
    def __init__(self, dim1, dim2):
        self.id = syst.systid()
        self.dimensions = [dim1, dim2]
        self.output = syst.speak(dim1,dim2)
        self.position = randomposition(grid['end'][0],grid['end'][1])
        
    def draw(self):
        pass
            
                
    @staticmethod
    def systid():
        try:
            syst.counter.append(len(syst.counter)+1)
        except NameError:
            print 'Error'
            return None
              
        return len(syst.counter)

    @staticmethod
    def speak(dim1,dim2):
        if dim1 == dim2:
            return 1
        if dim1 == 0:
            return 0
        else:
            return dim2 + dim1

    

bas1 = syst.speak(0,1)
bas2 = syst.speak(0,0)
def supersystem(n):
    global sup
    sup = []
    
    

    

supersystem(10)

def viewsys(system):

    pygame.init()
    plane = pygame.display.set_mode(grid['end'])
    
    clock = pygame.time.Clock()
    done = False
    
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True            # QUIT

        msElapsed = clock.tick(30)
        plane.fill(colors['black'])
        
        for i in range(0,len(system)):
            pygame.draw.circle(plane, colors['white'], system[i].position, 3)
            
        pygame.display.update()
    
        
