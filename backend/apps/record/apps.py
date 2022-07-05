from django.apps import AppConfig


class RecordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.record'

    def ready(self) -> None:
        # from apps.record import tracking
        import apps.record.signals
        
