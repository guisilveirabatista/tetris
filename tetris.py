import pygame
import sys
import random
import numpy as np
from shape import Shape

pygame.init()

# Screen size
WIDTH, HEIGHT = 640, 480

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)

GRAVITY = 1
VERTICAL_SQUARES = 10
HORIZONTAL_SQUARES = 10

SQUARE_HEIGTH = HEIGHT / VERTICAL_SQUARES
SQUARE_WIDTH = WIDTH / HORIZONTAL_SQUARES

# Initialize a 10x10 matrix with zeros
field = np.zeros((HORIZONTAL_SQUARES, VERTICAL_SQUARES), dtype=int)

# State of the game
state = "play"

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Gui's Tetris")

def random_start_position():
    return SQUARE_WIDTH * random.randint(1, 9)

def random_shape():
    r = random.randint(0, 4)
    return r

def check_collision(block, still_blocks):
    for still_block in still_blocks:
        for rect1 in still_block.rectangles:
            for rect2 in block.rectangles:
                if are_rects_touching(rect1, rect2):
                    return 0
    return 1

def check_touch_floor(block):
    for rect in block.rectangles:
        if rect.y + rect.height == HEIGHT:
            return True
    return False

def are_rects_touching(rect1, rect2):
    if rect1.top == rect2.bottom and (rect1.right > rect2.left and rect1.left < rect2.right):
        return True
    return False

running = True

shapes = ("L", "L", "L", "L", "L")
# shapes = ("T", "L", "I", "S", "O")
shape1 = Shape(shapes[random_shape()], 0, 0, SQUARE_WIDTH, SQUARE_HEIGTH, RED)

UPDATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_EVENT, 1000)

moving_blocks = [shape1]
still_blocks = []

while running:
    screen.fill(WHITE)
    current_time = pygame.time.get_ticks()
    if state == "play":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for block in moving_blocks:
                        block.spin()
            elif event.type == UPDATE_EVENT:
                for block in moving_blocks:
                    if check_touch_floor(block) or check_collision(block, still_blocks) == 0:
                        block.moving = 0
                        still_blocks.append(block)
                        moving_blocks.remove(block)
                        moving_blocks.append(Shape(shapes[random_shape()], random_start_position(), 0, SQUARE_WIDTH, SQUARE_HEIGTH, RED))
                    elif block.moving == 1:
                        for rect in block.rectangles:
                            rect.y = rect.y + SQUARE_HEIGTH
                        block.draw(screen)
                for block in still_blocks:
                    block.draw(screen)
                pygame.display.flip()
        clock.tick(60)
pygame.quit()
sys.exit()