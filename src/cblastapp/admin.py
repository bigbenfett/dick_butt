from django.contrib import admin

# Register your models here.
from .models import EstRequest


class EstRequestAdmin(admin.ModelAdmin):
	class Meta:
		model=EstRequest

admin.site.register(EstRequest, EstRequestAdmin)