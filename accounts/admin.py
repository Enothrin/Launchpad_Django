from django.contrib import admin
from accounts.models import AudioFile, Button, Pad


class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'file')


admin.site.register(AudioFile, AudioFileAdmin)
admin.site.register(Button)
admin.site.register(Pad)
# Register your models here.
