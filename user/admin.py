from django.contrib import admin

from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "name", "address", "email")
    search_fields = ("username", "name", "address", "phone", "email")


class CafeteriaAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    # list_filter = ("good")


class ScoreAdmin(admin.ModelAdmin):
    list_display = ("cafeteria", "num", "com", "fen")
    search_fields = ("cafeteria", "num", "com", "fen")


class ActionAdmin(admin.ModelAdmin):
    def show_all_join(self, obj):
        return [a.name for a in obj.user.all()]

    def num(self, obj):
        return obj.user.count()

    list_display = ("num", "status")
    search_fields = ("content", "user")
    list_filter = ("status",)


class CommenAdmin(admin.ModelAdmin):
    list_display = ("user", "cafeteria", "create_time")
    search_fields = ("user", "cafeteria",)
    list_filter = ("user", "cafeteria")


class ActionCommenAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "create_time")
    search_fields = ("user", "action")
    list_filter = ("user", "action")


class LiuyanAdmin(admin.ModelAdmin):
    list_display = ("user", "create_time")
    search_fields = ("user",)
    list_filter = ("user",)


class NumAdmin(admin.ModelAdmin):
    list_display = ("users", "cafeterias", "comments", "actions", "message_boards")


admin.site.register(Tags)
admin.site.register(User, UserAdmin)
admin.site.register(Cafeteria, CafeteriaAdmin)
# admin.site.register(Score, ScoreAdmin)
admin.site.register(Comment, CommenAdmin)
admin.site.register(Num, NumAdmin)
