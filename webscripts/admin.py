from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import MyMainMenu
# Register your models here.
admin.site.register(MyMainMenu, MarkdownxModelAdmin)