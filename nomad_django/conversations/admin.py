from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Message, models.Conversation)
class MessageAdmin(admin.ModelAdmin):
    pass

class ConversationAdmin(admin.ModelAdmin):
    pass