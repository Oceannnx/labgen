def gen5odds():
    for i in range(0,100,10):
        yield list(i+j for j in range(10) if j%2==1)
 
def Problem1(): 
    return [sum(i) for i in gen5odds()]
