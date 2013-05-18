def pickrandom(obj):
    if obj != int:
        while len(obj) >0:
            pick = obj[random.randint(0,len(obj)-1)]
            return 'Randomly selected', pickrandom(obj.remove(pick))


def randomposition(x,y):
    return (random.randint(0,x),random.randint(0,y))
