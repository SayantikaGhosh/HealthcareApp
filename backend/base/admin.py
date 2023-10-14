from django.contrib import admin
from .models import Food
# Register your models here.

@admin.register(Food)
class childrenAdmin(admin.ModelAdmin):
   list_display=['foodname','calories','fat','carbs','protein','fibres']
