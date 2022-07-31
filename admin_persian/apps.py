from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AdminPersianConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_persian'
    verbose_name = "بخش انتخاب فونت"


    def ready(self):
        from admin_persian.models import Font
        post_migrate.connect(Font.post_migrate_handler, sender=self)