from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.renderers import TemplatesSetting
from django.utils import timezone
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from .models import User, UserFeedback


class CustomFormRenderer(TemplatesSetting):
    form_template_name = "forms/custom.html"


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "username")


class AcceptTermsSignupForm(SignupForm):
    required_css_class = "required"

    terms_accepted = forms.BooleanField(
        required=True,
        initial=False,
        label=_("I accept the Terms of Service"),
        label_suffix="",
    )
    marketing_list_accepted = forms.BooleanField(
        required=False,
        initial=False,
        label=_("I want to receive product updates"),
        label_suffix="",
    )

    def __init__(self, *args, **kwargs):
        super(AcceptTermsSignupForm, self).__init__(*args, **kwargs)
        self.fields.move_to_end("terms_accepted")
        self.fields.move_to_end("marketing_list_accepted")

    def clean(self):
        data = self.cleaned_data
        terms_accepted = data.get("terms_accepted")

        if not terms_accepted:
            msg = gettext("The ToS has to be accepted.")
            self.add_error("terms_accepted", msg)

        return data

    def save(self, request):
        user = super(AcceptTermsSignupForm, self).save(request)
        user.terms_accepted_at = timezone.now()

        if self.cleaned_data["marketing_list_accepted"]:
            user.marketing_list_accepted_at = timezone.now()

        user.save()
        return user


class UpdateAccountForm(forms.ModelForm):
    required_css_class = "required"

    class Meta:
        model = User
        fields = ("first_name", "last_name", "avatar")


class UserFeedbackForm(forms.ModelForm):
    required_css_class = "required"

    class Meta:
        model = UserFeedback
        fields = ["email", "text"]
