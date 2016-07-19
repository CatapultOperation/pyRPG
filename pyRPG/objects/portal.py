import world
import display

def update(this, delta_time):
    pass

def collide(this, other):
    if other.type == "player":
        world.load(this.attributes["newmap"])
        world.objects = [world.player] + world.objects

        world.player.X = this.attributes["locx"]
        world.player.Y = this.attributes["locy"]
        # Print world out
        for x in range(world.WORLD_X):
            for y in range(world.WORLD_Y):
                display.printc(x, y + 5, world.map[x][y][1], world.map[x][y][0])

def char(this):
    return 'O'

def color(this):
    return display.CYAN
type = "portal"

# \ contiunes the line
attributes = {      \
    "newmap" : "",  \
    "locx" : 0,     \
    "locy" : 10,    \
}   

