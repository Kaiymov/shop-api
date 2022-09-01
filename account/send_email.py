from django.core.mail import send_mail


def send_confirmation_email(user, code):
    # code = user.activation_code
    code = code
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    # to_email = user.email
    to_email = user
    send_mail('Hello, активируйте ваш аккаунт', 
    f'Что-бы активировать ваш аккаунт нужно перейти по ссылке: {full_link}',
    'johnsnowtest73@gmail.com',
    [to_email,],
    fail_silently=False)



def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
        'Subject',
        f'Your code for reset password {code}',
        'from@emample.com',
        [to_email,],
        fail_silently=False
    )



def send_notification(user, id):
    to_email = user.email
    send_mail(
        'Уведомление о Создании заказа',
        f'Выс создали заказ №{id}, ожидайте звонка!',
        'from@example.com',
        [to_email,],
        fail_silently=False
    )

