from django.contrib import admin

from services.models import ServiceReviewsModel, ServicesModel, ServiceTierModel, ServiceTagModel

admin.site.register(ServicesModel)
admin.site.register(ServiceTierModel)
admin.site.register(ServiceReviewsModel)
admin.site.register(ServiceTagModel)
