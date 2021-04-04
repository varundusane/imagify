from django.apps import AppConfig


class SmessagesConfig(AppConfig):
    name = 'smessages'
    def ready(self):
        import sarahah.smessages.signals