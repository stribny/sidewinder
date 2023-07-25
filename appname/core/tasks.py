from datetime import timedelta

from django.conf import settings
from django.template.loader import get_template
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from huey import crontab
from huey.contrib import djhuey as huey

from appname.core.models import User
from appname.core.services.email import EmailService


@huey.db_task()
@huey.periodic_task(crontab(hour="0", minute="1"))
@huey.lock_task("send_users_report")
def send_users_report():
    if settings.ADMIN_EMAIL:
        last_day = (timezone.now() - timedelta(days=1)).date()
        users_joined_last_day = User.objects.filter(date_joined__gte=last_day)
        context = {"users": users_joined_last_day}
        template = get_template("core/email/users_report.txt")
        EmailService().send(
            _("Daily user report"), template.render(context), settings.ADMIN_EMAIL
        )
