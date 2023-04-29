from src.ecs.components.c_mine_reloader import CMineReloader
from src.create.prefab_creator import create_mine_reloader
import esper
import pygame 

def system_mine_reloader(world:esper.World, num_mines:int, delta_time:float, max_mines:int, reload_time:int):
      

    components = world.get_component( CMineReloader)
     
    if len(components)>0:
        for reloader_entity,  c_rel in components:
            c_rel.current_time += delta_time
            if c_rel.current_time>=reload_time:
                world.delete_entity(reloader_entity)
                return 0
            


    elif num_mines >= max_mines:
        create_mine_reloader(world)
    
    return num_mines
    
    
