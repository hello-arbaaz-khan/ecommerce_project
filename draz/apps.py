from django.apps import AppConfig


class DrazConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'draz'

def ready(self):
    import draz.signals