from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

from .forms import CustomFlatPageForm, UserChangeForm, UserCreationForm
from .models import User, UserFeedback


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["email", "username", "terms_accepted_at", "marketing_list_accepted"]
    readonly_fields = [
        "terms_accepted_at",
        "marketing_list_accepted_at",
        "date_joined",
        "last_login",
    ]


CustomUserAdmin.fieldsets += (
    (
        "Sign up details",
        {"fields": ("terms_accepted_at", "marketing_list_accepted_at")},
    ),
    ("Avatar", {"fields": ("avatar",)}),
)


class CustomFlatPageAdmin(FlatPageAdmin):
    form = CustomFlatPageForm


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserFeedback)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)

admin_name = f"{settings.PROJECT_NAME} {_('Administration')}"
admin.site.site_title = admin_name
admin.site.site_header = admin_name
