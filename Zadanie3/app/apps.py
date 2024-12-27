from django.apps import AppConfig
from .data_import import import_csv_to_db_if_empty


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        import_csv_to_db_if_empty()
