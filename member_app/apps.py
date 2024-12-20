from django.apps import AppConfig



class MemberAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'member_app'

    def ready(self):
        import member_app.signals