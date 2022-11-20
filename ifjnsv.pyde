x = 0
def setup():
    size(400,400)
def draw():
    global x
    background(100)
    ellipse(x,x,x,x)
    x += 1
