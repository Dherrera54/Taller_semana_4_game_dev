from src.create.prefab_creator import create_explosion
from src.create.prefab_creator import create_mine_frag
from src.ecs.components.tags.c_tag_special import CTagSpecial
import esper
import pygame
import math

def system_detonate_mine(world: esper.World,
                  player_size: pygame.Vector2,
                  mine_info: dict, delta_time:float,
                  explosion_info:dict):

    components = world.get_components(CTagSpecial)

    
    for special_entity, c_spec in components:
            c_spec[0].create_time += delta_time
            if c_spec[0].special_type=="mine" and c_spec[0].create_time>=2.5 and c_spec[0].detonated==False:
                    
                    for i in range(8):
                        vel_x = math.cos(math.radians(45*i))*mine_info["vel"]
                        vel_y = math.sin(math.radians(45*i))*mine_info["vel"]
                        vel = pygame.Vector2(vel_x, vel_y)
                        create_mine_frag(world,c_spec[0].pos,player_size,vel,mine_info)

                    c_spec[0].detonated=True
                    world.delete_entity(special_entity)
                    create_explosion(world, c_spec[0].pos, explosion_info)
            if c_spec[0].special_type=="mine_frag" and c_spec[0].create_time>=0.25 and c_spec[0].detonated==False:
                    
                    c_spec[0].detonated=True
                    world.delete_entity(special_entity)


    