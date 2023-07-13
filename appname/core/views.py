from allauth.account.views import LoginView as AllAuthLoginView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _

from .forms import UpdateAccountForm, UserFeedbackForm
from .models import User


def index(request):
    return TemplateResponse(request, "core/index.html", {})


def terms(request):
    return TemplateResponse(request, "core/terms.html", {})


def feedback(request):
    form = UserFeedbackForm()

    if request.method == "POST":
        form = UserFeedbackForm(request.POST)

        if form.is_valid():
            model = form.save()
            model.user = request.user if request.user.is_authenticated else None
            model.save()
            form = UserFeedbackForm()
            messages.success(request, _("Feedback has been submitted. Thank you!"))

    return TemplateResponse(request, "core/feedback.html", {"form": form})


@login_required
def user_settings(request):
    form = UpdateAccountForm(instance=request.user)

    if request.method == "POST":
        form = UpdateAccountForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _("Account details have been updated!"))

    return TemplateResponse(request, "core/settings.html", {"form": form})


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
    return redirect("index")


class LoginView(AllAuthLoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if settings.DEBUG:
            context["all_users"] = User.objects.all()

        return context


def login_as_user(request):
    if not settings.DEBUG or request.method != "POST":
        raise Http404

    from django.contrib.auth import login

    as_user = User.objects.get(pk=int(request.POST.get("select_user")))
    backend = settings.AUTHENTICATION_BACKENDS[0]

    login(request, as_user, backend)

    messages.success(request, _("Successfully signed in as ") + str(as_user))
    return redirect("index")
