from django.contrib import admin

from users.models import Rules, User

admin.site.register(User)
admin.site.register(Rules)
