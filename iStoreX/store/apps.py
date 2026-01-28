from django.apps import AppConfig
class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        from .models import Category
        if not Category.objects.exists():
            Category.objects.create(name="iPhone")
            Category.objects.create(name="Mac")
            Category.objects.create(name="iPad")
            Category.objects.create(name="AirPods")
