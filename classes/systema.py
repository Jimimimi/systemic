class Systema(object):
    counter = []
    def __init__(self, dim1, dim2):
        self.id = Systema.systid()
        self.dimensions = [dim1, dim2]
        self.output = Systema.speak(dim1,dim2)
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

        for i in range(n):
            mid = []
            for f in range(2):
                mid.append(Systema(random.randint(0,1),random.randint(0,1)))
            self.subs.append(Systema(mid[0].output,mid[1].output))
            
    def viewsys(self):

        pygame.init()
        self.plane = pygame.display.set_mode(self.grid['end'])
        
        clock = pygame.time.Clock()
        done = False
        
        while not done:
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True            # QUIT
    
            msElapsed = clock.tick(30)
            self.plane.fill(colors['black'])
            
            for i in range(0,len(self.subs)):
                pygame.draw.circle(self.plane, colors['white'], self.subs[i].position, 3)
                
            pygame.display.update()