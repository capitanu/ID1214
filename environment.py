from snake import Snake
from snake import Cube
import math
import time
import random
import pygame
from tkinter import messagebox
import numpy as np

RED = (255, 0, 0)
WHITE = (255,255,255)
GREEN = (0, 255 ,0)
PRINT = False

class Environment():
    

    def __init__(self, height, width,rows,columns):
        self.see_apple_1 = False
        self.see_apple_2 = False
        self.see_apple_3 = False
        self.see_apple_4 = False
        self.see_apple_5 = False
        self.see_apple_6 = False
        self.see_apple_7 = False
        self.see_apple_8 = False

        
        self.ROWS = rows
        self.COLUMNS = columns
        self.WIDTH = width;
        self.HEIGHT = height;
        self.WINDOW = pygame.display.set_mode((height+5, width+5))
        self.SNAKE = Snake(self.ROWS, (0,0,255), (self.ROWS/2,self.ROWS/2))


    def drawGrid(self):
        sizeBtwn = self.WIDTH // self.ROWS
        self.CONST = sizeBtwn
        x = 0
        y = 0
        for l in range(self.ROWS):
            x = x + sizeBtwn
            y = y + sizeBtwn
            pygame.draw.line(self.WINDOW, (255,255,255), (x,0), (x,self.WIDTH))
            pygame.draw.line(self.WINDOW, (255,255,255), (0,y), (self.WIDTH,y))


    def draw_line_1(self, color, pos):
        pygame.draw.line(self.WINDOW, color, (pos[0], pos[1]), ( self.WIDTH, pos[1]), 5)
    def draw_line_2(self, color ,pos):
        pygame.draw.line(self.WINDOW, color, (pos[0], pos[1]), ( pos[0], 0), 5)
    def draw_line_3(self, color,pos ):
        pygame.draw.line(self.WINDOW, color, (pos[0],pos[1]), ( 0, pos[1]), 5)
    def draw_line_4(self, color, pos):
        pygame.draw.line(self.WINDOW, color, (pos[0],pos[1]), ( pos[0], self.WIDTH) , 5)
    def draw_line_5(self, color,pos):
        i, j = self.SNAKE.head.pos[0], self.SNAKE.head.pos[1]
        while i < self.ROWS and j >= 0:
            i = i + 1
            j = j - 1
        pygame.draw.line(self.WINDOW, color, (pos[0], pos[1]), ( i * self.CONST + self.CONST/2, j * self.CONST + self.CONST /2), 5)
    def draw_line_6(self, color,pos):
        i, j = self.SNAKE.head.pos[0], self.SNAKE.head.pos[1]
        while i > 0 or j > 0:
            i = i - 1
            j = j - 1
        pygame.draw.line(self.WINDOW, color, (pos[0], pos[1]), ( i*self.CONST , j * self.CONST ), 5)
    def draw_line_7(self, color,pos):
        i, j = self.SNAKE.head.pos[0], self.SNAKE.head.pos[1]
        while j < self.ROWS and i >= 0:
            i = i - 1
            j = j + 1
        pygame.draw.line(self.WINDOW, color, (pos[0], pos[1]), ( i * self.CONST + self.CONST / 2, j* self.CONST + self.CONST /2),5)
    def draw_line_8(self, color, pos):
        i, j = self.SNAKE.head.pos[0], self.SNAKE.head.pos[1]
        while i < self.ROWS or i < self.ROWS:
            i = i + 1
            j = j + 1
        pygame.draw.line(self.WINDOW, color, (pos[0], pos[1]), ( i * self.CONST, j * self.CONST ),5)



    

    def reset(self):
        self.SNAKE.reset((int(self.ROWS/2),int(self.ROWS/2)))
        self.snack = Cube(self.ROWS, self.random_apple(), color = (0,255,0))
        state = self.SNAKE.state_info_2(self.snack)
        return state

    
    def step(self, action, moves):
        reward = -1
        done = False
        food_eaten = False
        update = False
        info = 0
        
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
            info = 2
            reward = -50
            done = True

        food_eaten = False
        if self.SNAKE.head.pos == self.snack.pos:
            self.SNAKE.addCube()
            if len(self.SNAKE.body) != self.ROWS * self.ROWS:
                self.snack = Cube(self.ROWS, self.random_apple(), color = (0,255,0))
            food_eaten = True
            reward = 100
            info = 3

        if len(self.SNAKE.body) == self.ROWS * self.ROWS:
            reward = 1000
            done = True
            info = 4
        

        if self.SNAKE.head.pos[0] >= self.ROWS or self.SNAKE.head.pos[0] < 0 or self.SNAKE.head.pos[1] >= self.ROWS or self.SNAKE.head.pos[1] < 0:
            done = True
            reward = -50
            info = 1

        if moves >= 100:
            done = True
            reward = -100
            info = 5
        if moves >= 100:
            reward = -10

        if not done:
            self.SNAKE.move(update)
        distance_after = math.sqrt(math.pow(self.SNAKE.head.pos[0] - self.snack.pos[0] , 2 ) + math.pow(self.SNAKE.head.pos[1] - self.snack.pos[1], 2))      

#        if distance_after > distance and (self.see_apple_1 or self.see_apple_2 or self.see_apple_3 or self.see_apple_4 or self.see_apple_5 or self.see_apple_6 or self.see_apple_7 or self.see_apple_8):
 #           reward -= 10
            
#        print(reward)
        return self.SNAKE.state_info_2(self.snack), reward, done, len(self.SNAKE.body), food_eaten, info
    
    
    def random_apple(self):
        positions = self.SNAKE.body
        while True:
            x = random.randrange(self.ROWS)
            y = random.randrange(self.ROWS)
            if(len(self.SNAKE.body) == self.ROWS * self.ROWS):
                break
            if len(list(filter(lambda snakeblock: snakeblock.pos == (x,y), positions))) > 0:
                continue
            else:
                break
        return (x,y)

    
    def render(self, state):
        self.WINDOW.fill((0,0,0))
        self.SNAKE.draw(self.WINDOW)
        self.snack.draw(self.WINDOW)
        self.drawGrid()
        self.print_state(state)
        pygame.display.update()


        
    def print_state(self,state):
        weird_flex_1 = self.SNAKE.head.pos[0] * self.CONST + self.CONST/2
        weird_flex_2 = self.SNAKE.head.pos[1] * self.CONST + self.CONST/2
        # --- RIGHT ---
        if PRINT:
            print("right snack")
            print(state[9])
            print("Right body")
            print(state[10])
            
        if(state[10] == 1):
            self.draw_line_1(RED,(weird_flex_1, weird_flex_2) )
            self.see_apple_1 = False
        elif(state[9] == 1):
            self.draw_line_1(GREEN,  (weird_flex_1, weird_flex_2))
            self.see_apple_1 = True
        else:
            self.draw_line_1(WHITE,  (weird_flex_1, weird_flex_2))
            self.see_apple_1 = False


            # -- UP ---
        if PRINT:
            print("Up snack")
            print(state[12])
            print("Up body")
            print(state[13])
            
        if(state[13] == 1):
            self.draw_line_2(RED,(weird_flex_1, weird_flex_2))
            self.see_apple_2 = False
        elif(state[12] == 1):
            self.see_apple_2 = True
            self.draw_line_2(GREEN,(weird_flex_1, weird_flex_2))
        else:
            self.draw_line_2(WHITE,(weird_flex_1, weird_flex_2))
            self.see_apple_2 = False

            # --- LEFT ---
        if PRINT:
            print("Left snack")
            print(state[15])
            print("Left body")
            print(state[16])
            
        if(state[16] == 1):
            self.draw_line_3(RED,(weird_flex_1, weird_flex_2))
            self.see_apple_3 = False
        elif(state[15] == 1):
            self.draw_line_3(GREEN,(weird_flex_1, weird_flex_2))
            self.see_apple_3 = True
        else:
            self.draw_line_3(WHITE,(weird_flex_1, weird_flex_2))
            self.see_apple_3 = False


            # --- DOWN ---
        if PRINT:
            print("Down snack")
            print(state[18])
            print("Down body")
            print(state[19])

        if(state[19] == 1):
            self.draw_line_4(RED,(weird_flex_1, weird_flex_2))
            self.see_apple_4 = False
        elif(state[18] == 1):
            self.draw_line_4(GREEN,(weird_flex_1, weird_flex_2))
            self.see_apple_4 = True
        else:
            self.draw_line_4(WHITE,(weird_flex_1, weird_flex_2))
            self.see_apple_4 = False

            # --- UP RIGHT ---
        if PRINT:
            print("Up right snack",(weird_flex_1, weird_flex_2))
            print(state[21])
            print("Up right body",(weird_flex_1, weird_flex_2))
            print(state[22])

        if(state[22] == 1):
            self.draw_line_5(RED,(weird_flex_1, weird_flex_2))
            self.see_apple_5 = False
        elif(state[21] == 1):
            self.draw_line_5(GREEN,(weird_flex_1, weird_flex_2))
            self.see_apple_5 = True
        else:
            self.draw_line_5(WHITE,(weird_flex_1, weird_flex_2))
            self.see_apple_5 = False



            # --- UP LEFT ---
        if PRINT:
            print("Up left snack")
            print(state[24])
            print("Up left body")
            print(state[25])

        if(state[25] == 1):
            self.draw_line_6(RED,(weird_flex_1, weird_flex_2))
            self.see_apple_6 = False
        elif(state[24] == 1):
            self.draw_line_6(GREEN,(weird_flex_1, weird_flex_2))
            self.see_apple_6 == True
        else:
            self.draw_line_6(WHITE,(weird_flex_1, weird_flex_2))
            self.see_apple_6 = False


            # --- DOWN LEFT ---
        if PRINT:
            print("Down left snack")
            print(state[27])
            print("Down left body")
            print(state[28])
            
        if(state[28] == 1):
            self.draw_line_7(RED,(weird_flex_1, weird_flex_2))
            self.see_apple_7 = False
        elif(state[27] == 1):
            self.draw_line_7(GREEN,(weird_flex_1, weird_flex_2))
            self.see_apple_7 = True
        else:
            self.draw_line_7(WHITE,(weird_flex_1, weird_flex_2))
            self.see_apple_7 = False



            # --- DOWN RIGHT ---
        if PRINT:
            print("Down right snack")
            print(state[30])
            print("Down right body")
            print(state[31])

        if(state[31] == 1):
            self.draw_line_8(RED,(weird_flex_1, weird_flex_2))
            self.see_apple_8 = False
        elif(state[30] == 1):
            self.draw_line_8(GREEN,(weird_flex_1, weird_flex_2))
            self.see_apple_8 = True
        else:
            self.draw_line_8(WHITE,(weird_flex_1, weird_flex_2))
            self.see_apple_8 = False

        if PRINT:
            print("----------------------------------------------")
            print("----------------------------------------------")
        #time.sleep(1)




        
