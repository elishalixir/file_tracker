from django.contrib import admin
from .models import file_movement
# Register your models here.

class file_movementAdmin(admin.ModelAdmin):
    list_display = ('Date', 'File_number', 'Project_title', 'Proponent', 'Project_location', 'Action')
    search_fields = ('File_number', 'Project_title', 'Proponent')
    list_per_page = 10
    list_max_show_all = 20

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(file_movement, file_movementAdmin)