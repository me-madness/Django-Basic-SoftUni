from django.apps import AppConfig # type: ignore


class PetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petstagram.pets'
