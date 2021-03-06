import math
import pygame
import numpy as np
import time


PRINT = 0

class Cube(object):
    
    w = 500
    def __init__(self, rows, start, dirnx = 1, dirny = 0, color = (255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        self.rows = rows

        
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
        
    def draw(self, surface, eyes=False):
        dis= self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            center = dis//2
            radius = 3
            circleMiddle = (i*dis+center-radius,j*dis+8)
            circleMiddle2 = (i*dis+ dis- radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class Snake(object):
    body = []
    turns = {}
    
    def __init__(self, rows, color, pos):
        self.color = color
        self.head = Cube(rows, pos)
        self.rows = rows
        self.body.append(self.head)
        self.dirnx = 1
        self.dirny = 0
        self.addCube()
        self.addCube()

    def block_in_body(self, block):
        for i in self.body:
            if block[1] == self.head.pos[0] and block[0] == self.head.pos[1]:
                return 0.2
            elif block[1] == i.pos[0] and block[0] == i.pos[1]:
                return 0.1
        return 0

    def block_in_body_except_head(self, block):
        for i in self.body:
            if i == self.head:
                continue
            elif block[0] == i.pos[0] and block[1] == i.pos[1]:
                return True
        return False

    def state_info(self, snack):
        state = np.array([])
        for i in range(0, self):
            for j in range(0, self.rows):
                rtn = self.block_in_body((i,j))
                if snack.pos[0] == i and snack.pos[1] == j:
                    rtn = 0.3
                state = np.append(state, rtn)
        return state


    def state_info_2(self, snack):
        state = np.array([])
        if self.dirnx == 1 and self.dirny == 0:
            direction = np.array([1 , 0 , 0 ,0])
        if self.dirnx == -1 and self.dirny == 0:
            direction = np.array([0 , 0 , 1 ,0])
        if self.dirnx == 0 and self.dirny == 1:
            direction = np.array([0 , 1 , 0 ,0])
        if self.dirnx == 0 and self.dirny == -1:
            direction = np.array([0 , 0 , 0 ,1])
        state = np.append(state, direction)
        if self.body[-1].dirnx == 1 and self.body[-1].dirny == 0:
            direction_tail = np.array([1, 0 ,0 ,0])
        if self.body[-1].dirnx == -1 and self.body[-1].dirny == 0:
            direction_tail = np.array([0, 0 ,1 ,0])
        if self.body[-1].dirnx == 0 and self.body[-1].dirny == 1:
            direction_tail = np.array([0, 1 ,0 ,0])
        if self.body[-1].dirnx == 0 and self.body[-1].dirny == -1:
            direction_tail = np.array([0, 0 ,0 ,1])
        state = np.append(state, direction_tail)

        # right
        distance = (self.rows - 1 - self.head.pos[0]) / self.rows
        d_right = distance        
        snack_available_1 = 0
        if snack.pos[1] == self.head.pos[1] and snack.pos[0]  > self.head.pos[0]:
            snack_available_1 = 1
            distance = (snack.pos[0] - 1 - self.head.pos[0])/self.rows
        body_in_range = 0
        for i in range(self.head.pos[0] + 1, self.rows):
            if self.block_in_body_except_head((i, self.head.pos[1])):
                if(i < snack.pos[0]):
                    snack_available_1 = 0
                distance = (i - 1 - self.head.pos[0]) / self.rows
                body_in_range = 1
                break
        state = np.append(state, [distance, snack_available_1, body_in_range])
        if(PRINT):
            print("Distance right: " + str(distance))


        # up
        distance = (self.head.pos[1]) / self.rows
        d_up = distance        
        snack_available_2 = 0
        if snack.pos[0] == self.head.pos[0] and snack.pos[1] < self.head.pos[1]:
            snack_available_2 = 1
            distance = (self.head.pos[1] - 1 - snack.pos[1]) / self.rows
        body_in_range = 0
        for i in range(self.head.pos[1] - 1, -1, -1):
            if self.block_in_body_except_head((self.head.pos[0], i)):
                if(i > snack.pos[1]):
                    snack_available_2 = 0
                body_in_range = 1
                distance = (self.head.pos[1] - 1 - i) / self.rows
                break
        state = np.append(state, [distance, snack_available_2, body_in_range])
        if(PRINT):
            print("Distance up: " + str(distance))

        # left
        distance = (self.head.pos[0]) / self.rows
        d_left = distance
        snack_available_3 = 0
        if snack.pos[1] == self.head.pos[1] and snack.pos[0] < self.head.pos[0]:
            snack_available_3 = 1
            distance = (self.head.pos[0] - 1 - snack.pos[0]) / self.rows
        body_in_range = 0
        for i in range(self.head.pos[0] - 1, -1 , -1):
            if self.block_in_body_except_head((i, self.head.pos[1])):
                if(i > snack.pos[0]):
                    snack_available_3 = 0
                body_in_range = 1
                distance = (self.head.pos[0] - 1 - i) / self.rows
                break
        state = np.append(state, [distance, snack_available_3, body_in_range])
        if(PRINT):
            print("Distance left: " + str(distance))

        # down
        distance = (self.rows - 1 - self.head.pos[1]) / self.rows
        d_down = distance
        snack_available_4 = 0
        if snack.pos[0] == self.head.pos[0] and snack.pos[1]  > self.head.pos[1]:
            snack_available_4 = 1
            distance = (snack.pos[1] - 1 - self.head.pos[1]) / self.rows
        body_in_range = 0
        for i in range(self.head.pos[1] + 1,self.rows):
            if self.block_in_body_except_head((self.head.pos[0], i)):
                if(i < snack.pos[1]):
                    snack_available_4 = 0
                body_in_range = 1
                distance = (snack.pos[1] - 1 - self.head.pos[1]) / self.rows
                break
        state = np.append(state, [distance, snack_available_4, body_in_range])
        if(PRINT):
            print("Distance down: " + str(distance))

        # diagonal up right
        i, j = self.head.pos[0], self.head.pos[1]
        i1 = 0
        snack_available = 0
        body_in_range = 0
        distance = min(d_up, d_right)
        while(i < self.rows and j > 0):
            i1 += 1
            i += 1
            j -= 1
            if self.block_in_body_except_head((i,j)):
                body_in_range = 1
                distance = (i1 - 1) / self.rows
                break
            if snack.pos[0] == i and snack.pos[1] == j:
                snack_available = 1
                distance = (i1 - 1) / self.rows
                break
        state = np.append(state, [distance, snack_available, body_in_range])
        if(PRINT):
            print("Distance up right: " + str(distance))    

        # diagonal up left
        i, j = self.head.pos[0], self.head.pos[1]
        i1 = 0 
        snack_available = 0
        body_in_range = 0
        distance = min(d_up, d_left)
        while(i > 0 and j > 0):
            i -= 1
            j -= 1
            i1 += 1
            if self.block_in_body_except_head((i,j)):
                body_in_range = 1
                distance = (i1 - 1) / self.rows
                break
            if snack.pos[0] == i and snack.pos[1] == j:
                snack_available = 1
                distance = (i1 - 1) / self.rows
                break
        state = np.append(state, [distance, snack_available, body_in_range])
        if(PRINT):
            print("Distance up left: " + str(distance))    

        
        # diagonal down left
        i, j = self.head.pos[0], self.head.pos[1]
        i1 = 0
        snack_available = 0
        body_in_range = 0
        distance = min(d_down, d_left)
        while(i > 0 and j < self.rows):
            i -= 1
            j += 1
            i1 += 1
            if self.block_in_body_except_head((i,j)):
                distance = (i1 - 1) / self.rows
                body_in_range = 1
                break
            if snack.pos[0] == i and snack.pos[1] == j:
                distance = (i1 - 1) / self.rows
                snack_available = 1
                break
        state = np.append(state, [distance, snack_available, body_in_range])
        if(PRINT):
            print("Distance down left: " + str(distance))    
        
        
        # diagonal down right
        i, j = self.head.pos[0], self.head.pos[1]
        i1 = 0
        snack_available = 0
        body_in_range = 0
        distance = min(d_down, d_right)
        while(i < self.rows and j < self.rows):
            i += 1
            j += 1
            i1 += 1
            if self.block_in_body_except_head((i,j)):
                body_in_range = 1
                distance = (i1 - 1) / self.rows
                break
            if snack.pos[0] == i and snack.pos[1] == j:
                snack_available = 1
                distance = (i1 - 1) / self.rows
                break
        state = np.append(state, [distance, snack_available, body_in_range])
        if(PRINT):
            print("Distance down right: " + str(distance))    


        
#        time.sleep(5)
        if(PRINT):
            print("----------------")
#        print(state)
        return state
        
        
    def move(self, update):
        if self.dirnx == 1 and self.dirny == 0 and update:
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        if self.dirnx == -1 and self.dirny == 0 and update:
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        if self.dirnx == 0 and self.dirny == 1 and update:
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        if self.dirnx == 0 and self.dirny == -1 and update:
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else: c.move(c.dirnx, c.dirny)

                    
    def reset(self, pos):
        self.head = Cube(self.head.rows, pos)
        self.body = []
        self.body.append(self.head)
        self.addCube()
        self.addCube()
        self.turns = {}
        self.dirnx = 1
        self.dirny = 0
        
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube(self.head.rows, (tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube(self.head.rows, (tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube(self.head.rows, (tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube(self.head.rows, (tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i,c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

