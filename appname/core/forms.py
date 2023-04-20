import pendulum
from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django_tiptap.widgets import TipTapWidget

from .models import User, UserFeedback


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "username")


class AcceptTermsSignupForm(SignupForm):
    terms_accepted = forms.BooleanField(
        required=False, initial=False, label=_("I accept the Terms of Service")
    )
    marketing_list_accepted = forms.BooleanField(
        required=False, initial=False, label=_("I want to receive product updates")
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
        user.terms_accepted_at = pendulum.now()

        if self.cleaned_data["marketing_list_accepted"]:
            user.marketing_list_accepted_at = pendulum.now()

        user.save()
        return user


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "avatar")


class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ["email", "text"]


class CustomFlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TipTapWidget())

    class Meta:
        model = FlatPage
        fields = ("url", "title", "content", "sites")
