from src.create.prefab_creator import create_screen_message
from src.ecs.systems.s_rendering import system_rendering
import pygame

 
from src.engine.service_locator import ServiceLocator

def system_pause( pause_text_info:dict, screen:pygame.Surface):
    pause= True
    
    while pause:
        pygame.display.update()
        screen.fill(pygame.Color(0,0,0))
        create_screen_message(screen, pause_text_info["paused"])
        create_screen_message(screen, pause_text_info["paused_msg"])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause=False
                