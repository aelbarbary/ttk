from django.apps import AppConfig


class TakethekidsappConfig(AppConfig):
    name = 'takethekidsapp'
    def ready(self):
        import takethekidsapp.signals  # noqa
