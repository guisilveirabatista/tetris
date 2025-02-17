import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)

class Shape:
    def __init__(self, shape, x, y, square_width, square_height, color):
        self.shape = shape
        self.x = x
        self.y = y
        self.square_width = square_width
        self.square_height = square_height
        self.color = color
        self.orientation = "UP"
        self.moving = 1
        self.rectangles = [
                    pygame.Rect(self.x, self.y, self.square_width, self.square_height),
                    pygame.Rect(self.x, self.y + self.square_height, self.square_width * 3, self.square_height)
        ]
        

    def move(self, dx, dy):
        self.x += dx * self.speed
        
    def spin(self):
        if self.orientation == "UP":
            self.orientation = "RIGHT"
        elif self.orientation == "RIGHT":
            self.orientation = "DOWN"
        elif self.orientation == "DOWN":
            self.orientation = "LEFT"
        elif self.orientation == "LEFT":
            self.orientation = "UP"
        self.rectangles.clear()
        match self.shape:
            case "L":
                match self.orientation:
                    case "UP":
                        self.rectangles = [
                            pygame.Rect(self.x, self.y, self.square_width, self.square_height),
                            pygame.Rect(self.x, self.y + self.square_height, self.square_width * 3, self.square_height)
                        ]
                    case "RIGHT":
                        self.rectangles = [
                            pygame.Rect(self.x + self.square_width, self.y, self.square_width , self.square_height),
                            pygame.Rect(self.x, self.y, self.square_width , self.square_height * 3)
                        ]
                    case "DOWN":
                        self.rectangles = [
                            pygame.Rect(self.x, self.y, self.square_width * 3, self.square_height),
                            pygame.Rect(self.x + (self.square_width * 2), self.y + self.square_height, self.square_width, self.square_height),
                        ]
                    case "LEFT":
                        self.rectangles = [
                            pygame.Rect(self.x, self.y + (self.square_height * 3), self.square_width, self.square_height),
                            pygame.Rect(self.x + self.square_width, self.y + self.square_height, self.square_width, self.square_height * 3),
                        ]

    def draw(self, screen):
        match self.shape:
            case "L":
                for rect in self.rectangles:
                    pygame.draw.rect(screen, RED, rect)            
            case "T":
                self.rectangles = [
                    pygame.draw.rect(screen, BLUE, pygame.Rect(self.x + self.square_width, self.y, self.square_width, self.square_height)),
                    pygame.draw.rect(screen, BLUE, pygame.Rect(self.x, self.y + self.square_height, self.square_width * 3, self.square_height))
                ]
            case "S":
                self.rectangles = [
                    pygame.draw.rect(screen, GREEN, pygame.Rect(self.x + self.square_width, self.y, self.square_width * 2, self.square_height)),
                    pygame.draw.rect(screen, GREEN, pygame.Rect(self.x, self.y + self.square_height, self.square_width * 2, self.square_height))
                ]
            case "I":
                self.rectangles = [
                    pygame.draw.rect(screen, PINK, pygame.Rect(self.x, self.y, self.square_width , self.square_height * 3))
                ]
            case "O":
                self.rectangles = [
                    pygame.draw.rect(screen, YELLOW, pygame.Rect(self.x, self.y, self.square_width * 2, self.square_height * 2))
                ]

    def ensure_boundaries(self, width, height):
        self.x = max(self.radius, min(self.x, width - self.radius))
        self.y = max(self.radius, min(self.y, height - self.radius))