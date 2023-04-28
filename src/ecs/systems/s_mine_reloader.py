from src.create.prefab_creator import create_screen_message
from src.ecs.components.c_mine_reloader import CMineReloader
from src.create.prefab_creator import create_mine_reloader
import esper
import pygame 

def system_mine_reloader(world:esper.World, screen:pygame.Surface, num_mines:int, delta_time:float, max_mines:int, mesg_info:dict):
    
    msg_1:dict ={"text": "mines: "+ str(max_mines-num_mines),
            "font":mesg_info["font"],
            "size":mesg_info["size"],
            "color":mesg_info["color"],
            "pos":{
                "x":100,
                "y":425
            }
    }
    
    create_screen_message(screen, mesg_info)   

    components = world.get_component( CMineReloader)
     
    if len(components)>0:
        for reloader_entity,  c_rel in components:
            c_rel.current_time += delta_time
            if c_rel.current_time>=10:
                print("reload")
                world.delete_entity(reloader_entity)
                return 0


    elif num_mines >= max_mines:
        create_mine_reloader(world)
    
    return num_mines
    
    
