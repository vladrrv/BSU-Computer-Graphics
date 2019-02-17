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
# Function to put pixels 
# at subsequence points 
def draw8points(xc, yc, x, y):
    draw4points(xc, yc, x, y)
    draw4points(xc, yc, y, x)
  
# Function for circle-generation 
# using Bresenham's algorithm 
def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r 
    while y >= x:
        # for each pixel we will 
        # draw all eight pixels 
        draw8points(xc, yc, x, y)
        x += 1 
  
        # check for decision parameter 
        # and correspondingly  
        # update d, x, y 
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        draw8points(xc, yc, x, y)
    

def midpoint_circle(x_centre, y_centre, r):
    x = r
    y = 0 
      
    # Printing the initial point on the axes  
    # after translation 
    set_pixel(x + x_centre, y + y_centre)
      
    # When radius is zero only a single 
    # point will be printed 
    if r > 0: 
        set_pixel(y + x_centre, -x + y_centre)
        set_pixel(y + x_centre, x + y_centre)
        set_pixel(-x + x_centre, y + y_centre)
      
    P = 1 - r
    while x > y:
        y += 1
          
        # Mid-point is inside or on the perimeter 
        if P <= 0:
            P = P + 2*y + 1 
        # Mid-point is outside the perimeter 
        else:
            x -= 1 
            P = P + 2*y - 2*x + 1
          
        # All the perimeter points have already been printed 
        if x < y: 
            break 
          
        # Printing the generated point and its reflection 
        # in the other octants after translation 
        draw4points(x_centre, y_centre, x, y)
          
        # If the generated point is on the line x = y then  
        # the perimeter points have already been printed 
        if x != y:
            set_pixel(y + x_centre, x + y_centre)
            set_pixel(-y + x_centre, x + y_centre)
            set_pixel(y + x_centre, -x + y_centre)
            set_pixel(-y + x_centre, -x + y_centre)


def mousePressed():
    
    global begin_line, x1, y1, m, n, grid
    
    x2, y2 = mouseX/w, mouseY/w
    
    if begin_line:
        midpoint_circle(x1, y1, int(sqrt((x1-x2)**2 + (y1-y2)**2)))
        #bresenham_circle(x1, y1, int(sqrt((x1-x2)**2 + (y1-y2)**2)))
        begin_line = False
    else:
        grid = [ [-1]*m  for i in range(n)]
        begin_line = True
        if (x2 < m and y2 < n) and (x2 >= 0 and y2 >= 0):
            grid[y2][x2] = 1
        x1, y1 = x2, y2
