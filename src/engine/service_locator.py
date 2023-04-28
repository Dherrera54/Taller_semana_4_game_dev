from src.engine.services.images_service import ImagesService
from src.engine.services.sounds_service import SoundsService
from src.engine.services.fonts_service import FontsService
class ServiceLocator:
    images_services = ImagesService()
    sounds_service = SoundsService()
    fonts_services = FontsService()