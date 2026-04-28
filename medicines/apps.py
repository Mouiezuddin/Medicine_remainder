from django.apps import AppConfig


class MedicinesConfig(AppConfig):
    name = 'medicines'
    
    def ready(self):
        import medicines.signals
