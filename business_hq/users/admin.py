from django.contrib import admin

from users.models import User, UserCardModel, UserAddressModel

admin.site.register(User)
admin.site.register(UserCardModel)
admin.site.register(UserAddressModel)
