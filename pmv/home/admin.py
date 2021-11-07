from django.contrib import admin

from .models import CareerRequest, Photos, Video, Faqs

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