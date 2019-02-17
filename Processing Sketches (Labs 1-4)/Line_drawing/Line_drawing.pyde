m = 50 # columns
n = 50 # rows

width = 600
height = 600

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


def bresenham(x1, y1, x2, y2):
    
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    x, y = x1, y1
    
    while True:
        if (x < m and y < n) and (x >= 0 and y >= 0):
            grid[y][x] = 1
        if x == x2 and y == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


def mousePressed():
    
    global begin_line, x1, y1, m, n, grid
    
    x2, y2 = mouseX/w, mouseY/w
    
    if begin_line:
        bresenham(x1, y1, x2, y2)
        begin_line = False
    else:
        grid = [ [-1]*m  for i in range(n)]
        begin_line = True
        if (x2 < m and y2 < n) and (x2 >= 0 and y2 >= 0):
            grid[y2][x2] = 1
        x1, y1 = x2, y2
