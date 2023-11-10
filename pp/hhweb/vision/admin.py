from django.contrib import admin

# Register your models here.
# Register your models here.
from vision.models import Skills


class SkillsAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]

admin.site.register(Skills, SkillsAdmin)