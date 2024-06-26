from django.contrib import admin

from users.models import User, EmailVerification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'expiration']
    fields = ['user', 'expiration']
    readonly_fields = ['expiration']