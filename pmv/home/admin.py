from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CareerRequest, Contact, Dealer, Photos, Fleet, Interest, Reserve

from embed_video.admin import AdminVideoMixin
from .models import Item
# Register your models here.

class CareerRequestAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'interest')
admin.site.register(CareerRequest, CareerRequestAdmin)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('name','email',)
admin.site.register(Reserve, ReserveAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)
    
admin.site.register(Photos, PhotoAdmin)

class DealerAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone')

admin.site.register(Dealer, DealerAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'subject')

admin.site.register(Contact, ContactAdmin)


class FleetAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'website')

admin.site.register(Fleet, FleetAdmin)


class InterestAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'location', 'phone')

admin.site.register(Interest, InterestAdmin)

class ItemAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)
