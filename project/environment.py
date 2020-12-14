from snake import Snake
from snake import Cube
import math
import random
import pygame
from tkinter import messagebox
import numpy as np


class Environment():
    

    def __init__(self, height, width,rows,columns):
        self.ROWS = rows
        self.COLUMNS = columns
        self.WIDTH = width;
        self.HEIGHT = height;
        self.WINDOW = pygame.display.set_mode((width+5, width+5))
        self.SNAKE = Snake((255,0,0), (self.ROWS/2,self.ROWS/2))


    def drawGrid(self):
        sizeBtwn = self.WIDTH // self.ROWS
        x = 0
        y = 0
        for l in range(self.ROWS):
            x = x + sizeBtwn
            y = y + sizeBtwn
            pygame.draw.line(self.WINDOW, (255,255,255), (x,0), (x,self.WIDTH))
            pygame.draw.line(self.WINDOW, (255,255,255), (0,y), (self.WIDTH,y))



    def reset(self):
        self.SNAKE.reset((int(self.ROWS/2),int(self.ROWS/2)))
        self.snack = Cube(self.random_apple(), color = (0,255,0))
        state = self.SNAKE.state_info_2(self.snack)
        return state

    def step(self, action):
        reward = 0
        done = False
        food_eaten = False
        update = False
        x_change, y_change = 0, 0
        distance = math.sqrt(math.pow(self.SNAKE.head.pos[0] - self.snack.pos[0], 2) + math.pow(self.SNAKE.head.pos[1] - self.snack.pos[1] , 2))

        if action == 0:
            if self.SNAKE.dirny != 0:
                self.SNAKE.dirnx = 1
                self.SNAKE.dirny = 0
                update = True
        if action == 1:
            if self.SNAKE.dirnx != 0:
                self.SNAKE.dirnx = 0
                self.SNAKE.dirny = 1
                update = True
        if action == 2:
            if self.SNAKE.dirny != 0:
                self.SNAKE.dirnx = -1
                self.SNAKE.dirny = 0
                update = True
        if action == 3:
            if self.SNAKE.dirnx != 0:
                self.SNAKE.dirnx = 0
                self.SNAKE.dirny = -1
                update = True
        
        if self.SNAKE.block_in_body_except_head((self.SNAKE.head.pos[0], self.SNAKE.head.pos[1])):
            reward = -50
            done = True

        if self.SNAKE.head.pos == self.snack.pos:
            self.SNAKE.addCube()
            self.snack = Cube(self.random_apple(), color = (0,255,0))
            reward = 50
            foot_eaten = True

#        distance_after = math.sqrt(math.pow(self.SNAKE.head.pos[0] - self.snack.pos[0] , 2 ) + math.pow(self.SNAKE.head.pos[1] - self.snack.pos[1], 2))       

        if self.SNAKE.head.pos[0] >= self.ROWS or self.SNAKE.head.pos[0] < 0 or self.SNAKE.head.pos[1] >= self.ROWS or self.SNAKE.head.pos[1] < 0:
            done = True
            reward = -50

        if not done and not food_eaten:
            self.SNAKE.move(update)
            

# might need to reset the snake, we'll see            
        return self.SNAKE.state_info_2(self.snack), reward, done, len(self.SNAKE.body)
            
    
    def random_apple(self):
        positions = self.SNAKE.body
        while True:
            x = random.randrange(self.ROWS)
            y = random.randrange(self.ROWS)
            if len(list(filter(lambda snakeblock: snakeblock.pos == (x,y), positions))) > 0:
                continue
            else:
                break
        return (x,y)

    
    def render(self):
        self.WINDOW.fill((0,0,0))
        self.SNAKE.draw(self.WINDOW)
        self.snack.draw(self.WINDOW)
        self.drawGrid()
        pygame.display.update()




        
