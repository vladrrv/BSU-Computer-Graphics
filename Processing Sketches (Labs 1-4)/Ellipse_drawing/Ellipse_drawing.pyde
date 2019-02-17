m = 70 # columns
n = 70 # rows

width = 700
height = 700

w = min(width/m, height/n) # width of each cell

grid = [ [-1]*m  for i in range(n)]

x1, y1 = -1, -1
begin_line = False


def setup():
    size(width,height)
    

def draw():
    
    x,y = 0,0 # starting position

    for row in grid:
        for col in row:
            if col == 1:
                fill(250,0,0)
            else:
                fill(255)
            stroke(200)
            rect(x, y, w, w)
            x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge

    
def set_pixel(x, y):
    grid[y % n][x % m] = 1 
    

def draw4points(xc, yc, x, y):
    set_pixel(xc+x, yc+y)
    set_pixel(xc-x, yc+y)
    set_pixel(xc-x, yc-y)
    set_pixel(xc+x, yc-y)
  

def bresenham_ellipse(x1, y1, x2, y2):
    xc = (x1+x2)//2
    yc = (y1+y2)//2
    a = abs(x1-x2)//2
    b = abs(y1-y2)//2
    
    sa = 2 * a**2
    sb = 2 * b**2
    x = a
    y = 0
    dx = b**2 * (1 - 2*a)
    dy = a**2
    e = 0
    sx = sb * a
    sy = 0
    
    while sx >= sy:
        draw4points(xc, yc, x, y)
        y += 1 
        sy += sa
        e += dy
        dy += sa

        if 2*e + dx > 0:
            x -= 1
            sx -= sb
            e += dx
            dx += sb
    
    x = 0
    y = b
    dx = b**2
    dy = a**2 * (1 - 2*b)
    e = 0
    sx = 0
    sy = sa * b
    
    while sx <= sy:
        draw4points(xc, yc, x, y)
        x += 1 
        sx += sb
        e += dx
        dx += sb

        if 2*e + dy > 0:
            y -= 1
            sy -= sa
            e += dy
            dy += sa
    

    
def midpoint_ellipse(x1, y1, x2, y2):
    x_centre = (x1+x2)//2
    y_centre = (y1+y2)//2
    a = abs(x1-x2)//2
    b = abs(y1-y2)//2
    x = 0
    y = b
    fx = 0
    fy = 2 * a**2 * b
    p = b**2 - a**2 * b + a**2 / 4
    
    while fx < fy: # |slope| < 1
        draw4points(x_centre, y_centre, x, y)
        x += 1
        fx += 2 * b**2
        
        if p < 0:
            p += fx + b**2
        else:
            y -= 1
            fy -= 2 * a**2
            p += fx + b**2 - fy
    
    draw4points(x_centre, y_centre, x, y)
      
    p = b**2 * (x+0.5)**2 + a**2 * (y-1)**2 - a**2 * b**2
    while y > 0:
        y -= 1
        fy -= 2 * a**2
        if p >= 0:
            p += - fy + a**2
        else:
            x += 1
            fx += 2 * b**2
            p += fx - fy + a**2
        draw4points(x_centre, y_centre, x, y)


def mousePressed():
    
    global begin_line, x1, y1, m, n, grid
    
    x2, y2 = mouseX/w, mouseY/w
    
    if begin_line:
        #midpoint_ellipse(x1, y1, x2, y2)
        bresenham_ellipse(x1, y1, x2, y2)
        begin_line = False
    else:
        grid = [ [-1]*m  for i in range(n)]
        begin_line = True
        if (x2 < m and y2 < n) and (x2 >= 0 and y2 >= 0):
            grid[y2][x2] = 1
        x1, y1 = x2, y2
