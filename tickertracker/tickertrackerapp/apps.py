from django.apps import AppConfig


class TickertrackerappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tickertrackerapp'

    def ready(self):
        from tickerupdater import updater
        updater.start()