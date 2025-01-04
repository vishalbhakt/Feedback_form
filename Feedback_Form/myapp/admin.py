from django.contrib import admin
from myapp import models

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display =('name','email','contact','feedback','rating')

admin.site.register(models.Feedback_Form,FeedbackAdmin)
