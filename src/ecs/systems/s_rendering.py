
from src.create.prefab_creator import create_screen_message
import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.engine.service_locator import ServiceLocator

def system_rendering(world:esper.World, screen:pygame.Surface, level_text_info:dict):
    components = world.get_components(CTransform, CSurface)
    
    c_t:CTransform
    c_s:CSurface
    for _, (c_t, c_s) in components:
        screen.blit(c_s.surf, c_t.pos, area=c_s.area)
        create_screen_message(screen, level_text_info["title"])
        create_screen_message(screen, level_text_info["info_text"])