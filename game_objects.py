import pygame, settings, random, math

class puck:

    def __init__(self, x, y, size, color, width = 1):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.width = width
        self.x_velo = 0
        self.y_velo = 0
        self.friction_coeff = 0.07
        # each puck has a corresponding arrow object
        self.arrow = arrow(self, self.color)
        # true when arrow has been drawn
        self.drawing_arrow = False

    def display(self):
        pygame.draw.circle(settings.screen, self.color, (self.x, self.y), self.size) 
        if self.arrow.get_length() <= self.size:
            pygame.draw.circle(settings.screen, self.color, (self.x, self.y), self.size+5, 2)
            
    # sets velocity of the puck with a vector v in the form (x, y)
    def set_velo(self, v):
        self.x_velo = v[0]
        self.y_velo = v[1]

    def get_velo(self):
        return self.x_velo, self.y_velo


class arrow:

    def __init__(self, puck, color):
        self.puck = puck
        self.start_x = puck.x
        self.start_y = puck.y
        self.end_x = puck.x+1
        self.end_y = puck.y
        self.color = color

    def set_arrow(self, coords):
        self.end_x = coords[0]
        self.end_y = coords[1]

    def reset_arrow(self):
        self.start_x = self.puck.x
        self.start_y = self.puck.y
        self.end_x = self.puck.x+1
        self.end_y = self.puck.y
        
    def display(self):
        self.dx = self.end_x - self.start_x
        self.dy = self.end_y - self.start_y
        # magnitude = (dx**2 + dy**2)**0.5
        self.unit_dx = self.dx / max(1, self.get_length())
        self.unit_dy = self.dy / max(1, self.get_length())
        L = 17
        # First arrowhead line
        arrow_x1 = self.end_x - L * (self.unit_dx - self.unit_dy)
        arrow_y1 = self.end_y - L * (self.unit_dy + self.unit_dx)

        # Second arrowhead line
        arrow_x2 = self.end_x - L * (self.unit_dx + self.unit_dy)
        arrow_y2 = self.end_y - L * (self.unit_dy - self.unit_dx)


        pygame.draw.lines(settings.screen, self.color, False, [(self.start_x, self.start_y), (self.end_x, self.end_y), (arrow_x1, arrow_y1), (self.end_x, self.end_y), (arrow_x2, arrow_y2)], 10)

    def get_length(self):
        return math.sqrt((self.start_x - self.end_x)**2 + (self.start_y - self.end_y)**2)

class ice:
    def __init__(self, surface):
        self.surface = surface
        self.color = settings.white
        self.x = 100
        self.y = 100
        self.width = 600
        self.height = 600

    def display(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

def all_arrows_drawn(pucks):
    for puck in pucks:
        if not puck.arrow.get_length() > puck.size:
            return False
    return True

def pucks_stationary(pucks):
    for puck in pucks:
        if not puck.get_velo() == (0, 0):
            return False
    return True

# initialize player 1 pucks
puck1 = puck(200, 250, 25, settings.blue)
puck2 = puck(333, 250, 25, settings.blue)
puck3 = puck(466, 250, 25, settings.blue)
puck4 = puck(600, 250, 25, settings.blue)
# puck1 = puck(25, settings.blue)
# puck2 = puck(25, settings.blue)
# puck3 = puck(25, settings.blue)
# puck4 = puck(25, settings.blue)
p1_pucks = [puck1, puck2, puck3, puck4]

# initialize player 2 pucks
puck5 = puck(200, 550, 25, settings.black)
puck6 = puck(333, 550, 25, settings.black)
puck7 = puck(466, 550, 25, settings.black)
puck8 = puck(600, 550, 25, settings.black)
# puck5 = puck(25, settings.black)
# puck6 = puck(25, settings.black)
# puck7 = puck(25, settings.black)
# puck8 = puck(25, settings.black)
p2_pucks = [puck5, puck6, puck7, puck8]

    
