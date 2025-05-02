from django.contrib import admin

# Register your models here.
from .models import Student, Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'dob', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
