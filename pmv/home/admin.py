from django.contrib import admin

from home.models import CareerRequest, Photos, Video

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