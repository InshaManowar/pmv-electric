from django.contrib import admin

from .models import CareerRequest, Dealer, Photos, Video, Faqs, Fleet

# Register your models here.
class CareerRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(CareerRequest, CareerRequestAdmin)



class PhotoAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Photos, PhotoAdmin)
class VideoAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Video, VideoAdmin)


class FaqsAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Faqs, FaqsAdmin)

class DealerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dealer, DealerAdmin)
class FleetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Fleet, FleetAdmin)
