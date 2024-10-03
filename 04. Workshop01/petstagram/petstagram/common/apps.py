from django.apps import AppConfig # type: ignore


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petstagram.common'
