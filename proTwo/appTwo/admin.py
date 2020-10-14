from django.contrib import admin
from appTwo.models import Topic,AccessRecord,Webpage,Users,UserProfileInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users)
admin.site.register(UserProfileInfo)
