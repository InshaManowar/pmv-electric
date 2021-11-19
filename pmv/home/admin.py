from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CareerRequest, Dealer, Photos, Fleet, Interest

from embed_video.admin import AdminVideoMixin
from .models import Item
# Register your models here.

class CareerRequestAdmin(ImportExportModelAdmin):
    list_display = ('name','email', 'interest')
admin.site.register(CareerRequest, CareerRequestAdmin)

class PhotoAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Photos, PhotoAdmin)

class DealerAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone')

admin.site.register(Dealer, DealerAdmin)


class FleetAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'website')

admin.site.register(Fleet, FleetAdmin)


class InterestAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'location', 'phone')

admin.site.register(Interest, InterestAdmin)

class ItemAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
