from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'dob', 'gender', 'roll_num', 'state', 'mobile', 'email', 'id_card', 'resume_file']
