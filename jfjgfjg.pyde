x = 200
y = 1
c = 200
v = 1
g = 0
def setup():
    size(600,600)
def draw():
    global x,y,c,v,g
    background(100)
    fill(g,0,0)
    rect(200,300,x,c)
    fill(0,g,0)
    rect(200,400,y,v)
    fill(0,0,g)
    rect(400,300,c,x)
    fill(g)
    rect(400,400,v,y)
    x -= 1
    y += 1
    c -= 1
    v += 1
    g += 1
