m = 70 # columns
n = 70 # rows

width = 700
height = 700

w = min(width/m, height/n) # width of each cell

grid = [ [0]*m  for i in range(n)]

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
            elif col == 2:
                fill(0,255,0)
            else:
                fill(255)
            stroke(200)
            rect(x, y, w, w)
            x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge

    
def set_pixel(x, y, val):
    grid[y % n][x % m] = val
    
def get_pixel(x, y):
    if (y >= n or x >= m) or (y < 0 or x < 0):
        return -1
    return grid[y][x] 
    
    
    
def flood_fill(x0, y0):
    if get_pixel(x0, y0) != 0:
        return
    st = [(x0,y0)]
    while st:
        x, y = st.pop()
        for nx, ny in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if get_pixel(nx, ny) == 0:
                set_pixel(nx, ny, 2)
                st.append((nx, ny))

def mouseDragged():
    
    global begin_line, x1, y1, m, n, grid
    
    x2, y2 = mouseX/w, mouseY/w
    
    if mouseButton == LEFT:
        
        if begin_line:
            begin_line = False
        else:
            #grid = [ [-1]*m  for i in range(n)]
            begin_line = True
        if (x2 < m and y2 < n) and (x2 >= 0 and y2 >= 0):
            set_pixel(x2, y2, 1)
        x1, y1 = x2, y2
        
        
def mousePressed():
    global m, n, grid
    x, y = mouseX/w, mouseY/w
    if mouseButton == CENTER:
        grid = [ [0]*m  for i in range(n)]
    elif mouseButton == RIGHT:
        flood_fill(x, y)
        
        
        
        
