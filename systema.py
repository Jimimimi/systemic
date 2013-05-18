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