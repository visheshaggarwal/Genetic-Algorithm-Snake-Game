import random
import random
import time
import math
from tqdm import tqdm
import numpy as np
import pygame



def display_snake(snake_position, display):
    for position in snake_position:
        pygame.draw.rect(display, (255, 0, 0), pygame.Rect(position[0], position[1], 10, 10))


def display_apple(apple_position, display):
    pygame.draw.rect(display, (0, 255, 0), pygame.Rect(apple_position[0], apple_position[1], 10, 10))


def starting_positions():
    snake_start = [100, 100]
    snake_position = [[100, 100], [90, 100], [80, 100]]
    apple_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
    score = 0
    currDirection = 'R'

    return snake_start, snake_position, apple_position, score, currDirection


def generate_snake(snake_start, snake_position, apple_position, button_direction, score,currDirection):

    if snake_start == apple_position:
        snake_position.insert(0, list(snake_start))
        apple_position, score = collision_with_apple(apple_position, score, snake_position)
        
    else:
        snake_position.insert(0, list(snake_start))
        snake_position.pop()

    return snake_position, apple_position, score


def collision_with_apple(apple_position, score, snake_position):
    apple_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
    # if apple_position[0]<100:
    #     apple_position[0] += 40
    # elif apple_position[0] > 400:
    #     apple_position[0] -= 40

    # if apple_position[1]<100:
    #     apple_position[1] += 40
    # elif apple_position[1] > 400:
    #     apple_position[1] -= 40

    while apple_position in snake_position:
        apple_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        # if apple_position[0]<100:
        #     apple_position[0] += 40
        # elif apple_position[0] > 400:
        #     apple_position[0] -= 40

        # if apple_position[1]<100:
        #     apple_position[1] += 40
        # elif apple_position[1] > 400:
        #     apple_position[1] -= 40
            
    score += 1
    return apple_position, score


def collision_with_boundaries(snake_start):
    if snake_start[0] >= 500 or snake_start[0] < 0 or snake_start[1] >= 500 or snake_start[1] < 0:
        return 1
    else:
        return 0


def collision_with_self(snake_start, snake_position):
    # snake_start = snake_position[0]
    if snake_start in snake_position[1:]:
        return 1
    else:
        return 0


def play_game(snake_start, snake_position, apple_position, button_direction, score, display, clock,currDirection):
    crashed = False
    while crashed is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        display.fill((255, 255, 255))

        snake_position, apple_position, score = generate_snake(snake_start, snake_position, apple_position,
                                                               button_direction, score,currDirection)
        
        display_apple(apple_position, display)
        display_snake(snake_position, display)

        pygame.display.set_caption("SCORE: " + str(score))
        pygame.display.update()
        clock.tick(50000)

        return snake_position, apple_position, score

def isLeftOccupied(snake_start, snake_position,currDirection):
    if currDirection=='R':
        return ([snake_start[0],snake_start[1]-10] in snake_position[:-1]) or snake_start[1]<0
    elif currDirection=='U':
        return ([snake_start[0]-10,snake_start[1]] in snake_position[:-1]) or snake_start[0]<0
    elif currDirection=='L':
        return ([snake_start[0],snake_start[1]+10] in snake_position[:-1]) or snake_start[1]>=500
    else:
        return ([snake_start[0]+10,snake_start[1]] in snake_position[:-1]) or snake_start[0]>=500

def isFrontOccupied(snake_start, snake_position,currDirection):
    if currDirection=='R':
        return ([snake_start[0]+10,snake_start[1]] in snake_position[:-1]) or snake_start[0]>=500
    elif currDirection=='U':
        return ([snake_start[0],snake_start[1]-10] in snake_position[:-1]) or snake_start[1]<0
    elif currDirection=='L':
        return ([snake_start[0]-10,snake_start[1]] in snake_position[:-1]) or snake_start[0]<0
    else:
        return ([snake_start[0],snake_start[1]+10] in snake_position[:-1]) or snake_start[1]>=500

def isRightOccupied(snake_start, snake_position,currDirection):
    if currDirection=='R':
        return ([snake_start[0],snake_start[1]+10] in snake_position[:-1]) or snake_start[1]>=500
    elif currDirection=='U':
        return ([snake_start[0]+10,snake_start[1]] in snake_position[:-1]) or snake_start[0]>=500
    elif currDirection=='L':
        return ([snake_start[0],snake_start[1]-10] in snake_position[:-1]) or snake_start[1]<0
    else:
        return ([snake_start[0]-10,snake_start[1]] in snake_position[:-1]) or snake_start[0]<0

def getSinusValue(snake_start, apple_position,currDirection):
    if currDirection=='R':
        perpendicular = apple_position[1] - snake_start[1]
        base = apple_position[0] - snake_start[0]
        if base==0 and perpendicular==0:
            return 0
        return perpendicular/math.sqrt(base**2 + perpendicular**2)

    elif currDirection=='U':
        perpendicular = apple_position[0] - snake_start[0]
        base = -(apple_position[1] - snake_start[1])
        if base==0 and perpendicular==0:
            return 0
        return perpendicular/math.sqrt(base**2 + perpendicular**2)
    
    elif currDirection=='L':
        perpendicular = -(apple_position[1] - snake_start[1])
        base = -(apple_position[0] - snake_start[0])
        if base==0 and perpendicular==0:
            return 0
        return perpendicular/math.sqrt(base**2 + perpendicular**2)

    else:
        perpendicular = -(apple_position[0] - snake_start[0])
        base = (apple_position[1] - snake_start[1])
        if base==0 and perpendicular==0:
            return 0
        return perpendicular/math.sqrt(base**2 + perpendicular**2)

def getFoodDirection(snake_start, apple_position, currDirection):

    if currDirection=='R':
        return [ apple_position[1]>snake_start[1], apple_position[1]<snake_start[1], apple_position[0]>snake_start[0], apple_position[0]<snake_start[0]]
    elif currDirection=='U':
        return [ apple_position[0]>snake_start[0], apple_position[0]<snake_start[0], apple_position[1]<snake_start[1], apple_position[1]>snake_start[1]]
    elif currDirection=='L':
        return [ apple_position[1]<snake_start[1], apple_position[1]>snake_start[1], apple_position[0]<snake_start[0], apple_position[0]>snake_start[0]]
    else:
        return [ apple_position[0]<snake_start[0], apple_position[0]>snake_start[0], apple_position[1]>snake_start[1], apple_position[1]<snake_start[1]]
    

def getLeftScaledDistance(snake_start,snake_position,currDirection):
    if currDirection=='R':
        step = 0
        y = snake_start[1]-10
        while y>=0:
            if [snake_start[0],y] in snake_position:
                return step/50
            else:
                y -= 10
                step += 1
        return step/50
    
    elif currDirection=='U':
        step = 0
        y = snake_start[0]-10
        while y>=0:
            if [y,snake_start[1]] in snake_position:
                return step/50
            else:
                y -= 10
                step += 1
        return step/50

    elif currDirection=='L':
        step = 0
        y = snake_start[1]+10
        while y<500:
            if [snake_start[0],y] in snake_position:
                return step/50
            else:
                y += 10
                step += 1
        return step/50

    else:
        step = 0
        y = snake_start[0]+10
        while y<500:
            if [y,snake_start[1]] in snake_position:
                return step/50
            else:
                y += 10
                step += 1
        return step/50

def getRightScaledDistance(snake_start,snake_position,currDirection):
    if currDirection=='L':
        step = 0
        y = snake_start[1]-10
        while y>=0:
            if [snake_start[0],y] in snake_position:
                return step/50
            else:
                y -= 10
                step += 1
        return step/50
    
    elif currDirection=='D':
        step = 0
        y = snake_start[0]-10
        while y>=0:
            if [y,snake_start[1]] in snake_position:
                return step/50
            else:
                y -= 10
                step += 1
        return step/50

    elif currDirection=='R':
        step = 0
        y = snake_start[1]+10
        while y<500:
            if [snake_start[0],y] in snake_position:
                return step/50
            else:
                y += 10
                step += 1
        return step/50

    else:
        step = 0
        y = snake_start[0]+10
        while y<500:
            if [y,snake_start[1]] in snake_position:
                return step/50
            else:
                y += 10
                step += 1
        return step/50

def getForwardScaledDistance(snake_start,snake_position,currDirection):
    if currDirection=='U':
        step = 0
        y = snake_start[1]-10
        while y>=0:
            if [snake_start[0],y] in snake_position:
                return step/50
            else:
                y -= 10
                step += 1
        return step/50
    
    elif currDirection=='L':
        step = 0
        y = snake_start[0]-10
        while y>=0:
            if [y,snake_start[1]] in snake_position:
                return step/50
            else:
                y -= 10
                step += 1
        return step/50

    elif currDirection=='D':
        step = 0
        y = snake_start[1]+10
        while y<500:
            if [snake_start[0],y] in snake_position:
                return step/50
            else:
                y += 10
                step += 1
        return step/50

    else:
        step = 0
        y = snake_start[0]+10
        while y<500:
            if [y,snake_start[1]] in snake_position:
                return step/50
            else:
                y += 10
                step += 1
        return step/50

display_width = 500
display_height = 500
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

pygame.init()
display=pygame.display.set_mode((display_width,display_height))
clock=pygame.time.Clock()