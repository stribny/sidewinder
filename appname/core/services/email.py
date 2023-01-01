from django.conf import settings
from django.core.mail import send_mail


class EmailService:
    def send(self, subject: str, message: str, to: str) -> None:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [to],
            fail_silently=False,
        )
