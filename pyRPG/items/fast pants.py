name ="Fast pants"
type = "pants"
attributes = {}
def on_equip (this,player):
    player.attributes["move_spd"+4]
def on_unequip (this, player):
    player.attributes["move_spd"-4]
