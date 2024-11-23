from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_activation_code(email, code):
    send_mail(
        "MotionWeb Project",
        f"Ушул ссылка менен отунуз озунузду аккаунтубузду активация кылыш учун!: \n\n http://localhost:8000/api/v1/auth/activate/{code}",
        'sassassas107@gmail.com',
        [email],
    )