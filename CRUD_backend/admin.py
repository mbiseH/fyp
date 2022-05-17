from django.apps import apps
from django.contrib import admin
from .models import user,appointment
from django.apps import apps

admin.site.register(user)
admin.site.register(appointment)




app = apps.get_app_config('graphql_auth')


for model_name, model in app.models.items():
    admin.site.register(model)