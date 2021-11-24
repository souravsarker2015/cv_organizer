from django.contrib import admin
from .models import CV


@admin.register(CV)
class CVModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_of_birth', 'gender', 'locality', 'city', 'pin', 'state', 'phone', 'email', 'job_city', 'profile_image', 'profile_file']
