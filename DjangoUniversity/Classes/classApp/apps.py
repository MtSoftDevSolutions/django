from django.apps import AppConfig


class ClassappConfig(AppConfig): #have to include this otherwise classApp would be meaningless
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classApp'
