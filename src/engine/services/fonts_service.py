import pygame
class FontsService:
    def __init__(self) -> None:
        self._fonts = {}

    def get_title(self,path:str, size:int)-> pygame.Surface:
        if path not in self._fonts:
            self._fonts[path]= pygame.font.Font(path, size)
        return self._fonts[path]
    def get_text(self,path:str, size:int)-> pygame.Surface:
        if path not in self._fonts:
            self._fonts[path]= pygame.font.Font(path, size)
        return self._fonts[path]