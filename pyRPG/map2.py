import world
from objects import *

def generate():
    world.map = [[ world.WORLD_GRASS for y in range(world.WORLD_Y)] for x in range(world.WORLD_X)]

    for x in range(22,29):
        world.map[x][5] = world.WORLD_WALL
        world.map[x][10] = world.WORLD_WALL
    for y in range(5,11):
        world.map[22][y] = world.WORLD_WALL
        world.map[28][y] = world.WORLD_WALL
   
    for x in range(23,28):
        for y in range(6,10):
            world.map[x][y] = [0,".", True]
        
    world.map[25][10] = [0,".", True]
    
    world.map[5][3] = [0, 'W', True]
    world.map[4][4] = [0, 'A', True]
    world.map[5][4] = [0, 'S', True]
    world.map[6][4] = [0, 'D', True]

    world.map[world.WORLD_X - 6][3] = [0, 'I', True]
    world.map[world.WORLD_X - 7][4] = [0, 'J', True]
    world.map[world.WORLD_X - 6][4] = [0, 'K', True]
    world.map[world.WORLD_X - 5][4] = [0, 'L', True]

