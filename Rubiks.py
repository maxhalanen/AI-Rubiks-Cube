

white = [["w"],["w"],["w"],
         ["w"],["w"],["w"],
         ["w"],["w"],["w"],]
         

red = [["r"],["r"],["r"],
       ["r"],["r"],["r"],
       ["r"],["r"],["r"],]

green = [["g"],["g"],["g"],
        ["g"],["g"],["g"],
        ["g"],["g"],["g"],]

blue = [["b"],["b"],["b"],
        ["b"],["b"],["b"],
        ["b"],["b"],["b"],]

yellow = [["y"],["y"],["y"],
        ["y"],["y"],["y"],
        ["y"],["y"],["y"],] 

orange= [["o"],["o"],["o"],
         ["o"],["o"],["o"],
         ["o"],["o"],["o"],]


#legend:
#   w   
# o b r g 
#   y   


def turnBlue():
    top = []
    right = []
    left = []
    down = []
    o = []
    y = []
    w = []
    r = []
    
    o.append(orange[0])
    o.append(orange[1])
    o.append(orange[2])
    y.append(yellow[0])
    y.append(yellow[1])
    y.append(yellow[2])
    r.append(red[0])
    r.append(red[1])
    r.append(red[2])
    w.append(white[0])
    w.append(white[1])
    w.append(white[2])
    
    yellow[0] = r[0]
    yellow[1] = r[1]
    yellow[2] = r[2]
    
    orange[0] = y[0]
    orange[1] = y[1]
    orange[2] = y[2]
    
    white[0] = o[0]
    white[1] = o[1]
    white[2] = o[2]
    
    red[0] = w[0]
    red[1] = w[1]
    red[2] = w[2]
    
    top.append(blue[0])
    top.append(blue[1])
    top.append(blue[2])
    right.append(blue[2])
    right.append(blue[5])
    right.append(blue[8])
    down.append(blue[8])
    down.append(blue[7])
    down.append(blue[6])
    left.append(blue[6])
    left.append(blue[3])
    left.append(blue[0])
    
    blue[0] = left[0]
    blue[1] = left[1]
    blue[2] = left[2]
    blue[2] = top[0]
    blue[5] = top[1]
    blue[8] = top[2]
    blue[8] = right[0]
    blue[7] = right[1]
    blue[6] = right[2]
    blue[6] = down[0]
    blue[3] = down[1]
    blue[0] = down[2]
    
def turnGreen():
    top = []
    right = []
    left = []
    down = []
    o = []
    y = []
    w = []
    r = []
    
    o.append(orange[6])
    o.append(orange[7])
    o.append(orange[8])
    y.append(yellow[6])
    y.append(yellow[7])
    y.append(yellow[8])
    r.append(red[6])
    r.append(red[7])
    r.append(red[8])
    w.append(white[6])
    w.append(white[7])
    w.append(white[8])
    
    yellow[6] = r[0]
    yellow[7] = r[1]
    yellow[8] = r[2]
    
    orange[6] = y[0]
    orange[7] = y[1]
    orange[8] = y[2]
    
    white[6] = o[0]
    white[7] = o[1]
    white[8] = o[2]
    
    red[6] = w[0]
    red[7] = w[1]
    red[8] = w[2]
    
    top.append(green[0])
    top.append(green[1])
    top.append(green[2])
    right.append(green[2])
    right.append(green[5])
    right.append(green[8])
    down.append(green[8])
    down.append(green[7])
    down.append(green[6])
    left.append(green[6])
    left.append(green[3])
    left.append(green[0])
    
    green[0] = left[0]
    green[1] = left[1]
    green[2] = left[2]
    green[2] = top[0]
    green[5] = top[1]
    green[8] = top[2]
    green[8] = right[0]
    green[7] = right[1]
    green[6] = right[2]
    green[6] = down[0]
    green[3] = down[1]
    green[0] = down[2] 

def turnYellow():    
    
    top = []
    right = []
    left = []
    down = []
    o = []
    r = []
    b = []
    g = []
    
    o.append(orange[2])
    o.append(orange[5])
    o.append(orange[8])
    b.append(blue[8])
    b.append(blue[7])
    b.append(blue[6])
    r.append(red[6])
    r.append(red[3])
    r.append(red[0])
    g.append(green[8])
    g.append(green[7])
    g.append(green[6])
    
    blue[8] = o[0]
    blue[7] = o[1]
    blue[6] = o[2]
    
    orange[2] = g[0]
    orange[5] = g[1]
    orange[8] = g[2]
    
    green[8] = r[0]
    green[7] = r[1]
    green[6] = r[2]
    
    red[6] = b[0]
    red[3] = b[1]
    red[0] = b[2]
    
    
    top.append(yellow[0])
    top.append(yellow[1])
    top.append(yellow[2])
    right.append(yellow[2])
    right.append(yellow[5])
    right.append(yellow[8])
    down.append(yellow[8])
    down.append(yellow[7])
    down.append(yellow[6])
    left.append(yellow[6])
    left.append(yellow[3])
    left.append(yellow[0])
    
    yellow[0] = left[0]
    yellow[1] = left[1]
    yellow[2] = left[2]
    yellow[2] = top[0]
    yellow[5] = top[1]
    yellow[8] = top[2]
    yellow[8] = right[0]
    yellow[7] = right[1]
    yellow[6] = right[2]
    yellow[6] = down[0]
    yellow[3] = down[1]
    yellow[0] = down[2]
    
def turnWhite():   
    top = []
    right = []
    left = []
    down = []
    o = []
    r = []
    b = []
    g = []
    o.append(orange[6])
    o.append(orange[3])
    o.append(orange[0])
    b.append(blue[0])
    b.append(blue[1])
    b.append(blue[2])
    r.append(red[2])
    r.append(red[5])
    r.append(red[8])
    g.append(green[0])
    g.append(green[1])
    g.append(green[2])
    
    blue[0] = o[0]
    blue[1] = o[1]
    blue[2] = o[2]
    
    orange[6] = g[0]
    orange[3] = g[1]
    orange[0] = g[2]
    
    green[0] = r[0]
    green[1] = r[1]
    green[2] = r[2]
    
    red[2] = b[0]
    red[5] = b[1]
    red[8] = b[2]
    
    top.append(yellow[0])
    top.append(yellow[1])
    top.append(yellow[2])
    right.append(yellow[2])
    right.append(yellow[5])
    right.append(yellow[8])
    down.append(yellow[8])
    down.append(yellow[7])
    down.append(yellow[6])
    left.append(yellow[6])
    left.append(yellow[3])
    left.append(yellow[0])
    
    yellow[0] = left[0]
    yellow[1] = left[1]
    yellow[2] = left[2]
    yellow[2] = top[0]
    yellow[5] = top[1]
    yellow[8] = top[2]
    yellow[8] = right[0]
    yellow[7] = right[1]
    yellow[6] = right[2]
    yellow[6] = down[0]
    yellow[3] = down[1]
    yellow[0] = down[2]

def turnRed():
    top = []
    right = []
    left = []
    down = []
    b = []
    y = []
    w = []
    g = []   
    b.append(blue[2])
    b.append(blue[5])
    b.append(blue[8])
    y.append(yellow[2])
    y.append(yellow[5])
    y.append(yellow[8])
    g.append(green[2])
    g.append(green[5])
    g.append(green[8])
    w.append(white[6])
    w.append(white[3])
    w.append(white[0])
    
    yellow[2] = g[0]    
    yellow[5] = g[1]
    yellow[8] = g[2]
    
    blue[2] = y[0]
    blue[5] = y[1]
    blue[8] = y[2]
    
    white[6] = b[0]
    white[3] = b[1]
    white[0] = b[2]
    
    green[2] = w[0]
    green[5] = w[1]
    green[8] = w[2]
    
    top.append(red[0])
    top.append(red[1])
    top.append(red[2])
    right.append(red[2])
    right.append(red[5])
    right.append(red[8])
    down.append(red[8])
    down.append(red[7])
    down.append(red[6])
    left.append(red[6])
    left.append(red[3])
    left.append(red[0])
    
    red[0] = left[0]
    red[1] = left[1]
    red[2] = left[2]
    red[2] = top[0]
    red[5] = top[1]
    red[8] = top[2]
    red[8] = right[0]
    red[7] = right[1]
    red[6] = right[2]
    red[6] = down[0]
    red[3] = down[1]
    red[0] = down[2]

def turnOrange():
    
    top = []
    right = []
    left = []
    down = []
    
    b = []
    y = []
    w = []
    g = []   
    
    b.append(blue[6])
    b.append(blue[3])
    b.append(blue[0])
    y.append(yellow[6])
    y.append(yellow[3])
    y.append(yellow[0])
    g.append(green[6])
    g.append(green[3])
    g.append(green[0])
    w.append(white[2])
    w.append(white[5])
    w.append(white[8])
    
    yellow[6] = g[0]    
    yellow[3] = g[1]
    yellow[0] = g[2]
    
    blue[6] = y[0]
    blue[3] = y[1]
    blue[0] = y[2]
    
    white[2] = b[0]
    white[5] = b[1]
    white[8] = b[2]
    
    green[6] = w[0]
    green[3] = w[1]
    green[0] = w[2]
    
    top.append(orange[0])
    top.append(orange[1])
    top.append(orange[2])
    right.append(orange[2])
    right.append(orange[5])
    right.append(orange[8])
    down.append(orange[8])
    down.append(orange[7])
    down.append(orange[6])
    left.append(orange[6])
    left.append(orange[3])
    left.append(orange[0])
    
    orange[0] = left[0]
    orange[1] = left[1]
    orange[2] = left[2]
    orange[2] = top[0]
    orange[5] = top[1]
    orange[8] = top[2]
    orange[8] = right[0]
    orange[7] = right[1]
    orange[6] = right[2]
    orange[6] = down[0]
    orange[3] = down[1]
    orange[0] = down[2]


turnOrange()


print(yellow[0] + yellow[1] + yellow[2])
print(yellow[3] + yellow[4] + yellow[5])
print(yellow[6] + yellow[7] + yellow[8])

print(orange[0] + orange[1] + orange[2])
print(orange[3] + orange[4] + orange[5])
print(orange[6] + orange[7] + orange[8])

print(red[0] + red[1] + red[2])
print(red[3] + red[4] + red[5])
print(red[6] + red[7] + red[8])

print(white[0] + white[1] + white[2])
print(white[3] + white[4] + white[5])
print(white[6] + white[7] + white[8])

print(blue[0] + blue[1] + blue[2])
print(blue[3] + blue[4] + blue[5])
print(blue[6] + blue[7] + blue[8])

print(green[0] + green[1] + green[2])
print(green[3] + green[4] + green[5])
print(green[6] + green[7] + green[8])




