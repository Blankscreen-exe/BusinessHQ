from django.contrib import admin

from chat.models import ChatSessionModel, ChatSessionReviewModel, MessageModel

admin.site.register(ChatSessionModel)
admin.site.register(ChatSessionReviewModel)
admin.site.register(MessageModel)
