
from django.contrib import admin

from blog.models import Blog, UserComment


admin.site.register(Blog)
admin.site.register(UserComment)