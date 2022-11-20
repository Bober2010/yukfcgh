x = 1
def setup():
    size(600,600)
def draw():
    global x
    background(255)
    strokeWeight(x)
    line(300,300,210,300)
    line(300,300,390,300)
    line(300,300,300,210)
    line(300,300,370,390)
    line(300,300,260,390)
    x = x + 1
