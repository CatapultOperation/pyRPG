import time
import sys

from objects import attack
import display
from items import item
import world
from objects import world_object
from spells import spell
from random import randrange

def MiniBoss_update(this, delta_time):
    eff_del_list = []
    for eff in this.attributes["effects"]:
        this.attributes["effects"][eff][0](this, delta_time)       # Tick code
        this.attributes["effects"][eff][2] -= delta_time           # Lower time
        if this.attributes["effects"][eff][2] <= 0:                # Remove effect
            eff_del_list.append(eff)
    for to_del in eff_del_list:
        this.attributes["effects"][to_del][1](this)
        del this.attributes["effects"][to_del]
    del eff_del_list
    if this.attributes["HP"] <= 0:
        world.to_del.append(this)
    else:        
        if randrange(0, 500) < delta_time:  
            this.X += randrange(-1, 2)
            this.Y += randrange(-1, 2)
            if this.X < 0:
                this.X = 0
            if this.Y < 0:
                this.Y = 0

def MiniBosscollide(this, obj):
    if obj.type == "player":
        pass #   Issue: Does massive damage, must add effect here to give player immunity   # obj.attributes["HP"] -= this.attributes["damage"]


def MiniBossColor(this):
  return display.CYAN

def MiniBossChar(this):
  return 'B'

MiniBoss_type = "enemy"

MiniBoss_attributes =                     \
    { "HP" : 100.0,                     \
      "MP" : 50,                        \
      "effects" : {},                   \
      "mov_spd" : 30,                    \
      "atk_spd" : 150,                   \
      "damage" : 10,                      \
      "EXP" : 5
    }