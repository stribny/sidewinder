from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _

from .forms import UpdateAccountForm, UserFeedbackForm


def index(request):
    return TemplateResponse(request, "core/index.html", {})


def terms(request):
    return TemplateResponse(request, "core/terms.html", {})


def websocket(request):
    return TemplateResponse(request, "core/websocket.html", {})


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
def settings(request):
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
