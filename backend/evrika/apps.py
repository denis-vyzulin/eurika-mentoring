from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EvrikaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'evrika'
    verbose_name = _('Main application')
