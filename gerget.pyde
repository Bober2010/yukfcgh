x = 200
y = 1
c = 200
v = 1
def setup():
    size(600,600)
def draw():
    global x,y,c,v
    background(100)
    rect(200,300,x,c)
    rect(200,400,y,v)
    rect(400,300,c,x)
    rect(400,400,v,y)
    x -= 1
    y += 1
    c -= 1
    v += 1
