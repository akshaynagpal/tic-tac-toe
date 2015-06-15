import pygame
import sys
from pygame.locals import *

#initialization and window setup
pygame.init()
DISPLAYSURF = pygame.display.set_mode((290,290),0,32)
pygame.display.set_caption('tic tac toe')

#defining colors for easy use
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN =(0,255,0) 
BLUE = (0,0,255)
"""
drawCross(self,box_number):
    x1=
    y1=
    x2=
    y2=


drawCircle(self,box_number):
"""    

DISPLAYSURF.fill(BLUE)
pygame.draw.rect(DISPLAYSURF,WHITE,(10,10,270,270))
pygame.draw.line(DISPLAYSURF,BLACK,(100,10),(100,280),2)
pygame.draw.line(DISPLAYSURF,BLACK,(190,10),(190,280),2)
pygame.draw.line(DISPLAYSURF,BLACK,(10,190),(280,190),2)
pygame.draw.line(DISPLAYSURF,BLACK,(10,100),(280,100),2)

"""                 
90,10-------90,280
180,10------180,280
"""

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
