from django.contrib import admin
from .models import Video

#tells django to track the Video model
admin.site.register(Video)