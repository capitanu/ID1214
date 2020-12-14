from environment import Environment
from snake import Cube
import random
import pygame


env = Environment(500,500,20,20)


def main():
    flag = True
    clock = pygame.time.Clock()
    snack = Cube(env.random_apple(), color = (0,255,0))
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        env.SNAKE.move()
        if env.SNAKE.body[0].pos == snack.pos:
            env.SNAKE.addCube()
            snack = Cube(env.random_apple(), color = (0,255,0))
        for x in range(len(env.SNAKE.body)):
            if env.SNAKE.body[x].pos in list(map(lambda x:x.pos, env.SNAKE.body[x+1:])):
                print('Score: ', len(env.SNAKE.body))
                env.SNAKE.reset((10,10))
                break

        env.render(snack)
         
main()


