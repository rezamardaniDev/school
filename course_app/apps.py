from django.apps import AppConfig


class CourseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course_app'

    def ready(self):
        import course_app.signals
