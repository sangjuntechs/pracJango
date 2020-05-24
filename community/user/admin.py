from django.contrib import admin
from .models import User
class userAdmin(admin.ModelAdmin):
    list_display = ('username','password','regiester_dttm','useremail')

admin.site.register(User, userAdmin)

