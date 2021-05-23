from djoser.email import ActivationEmail, PasswordResetEmail


class CustomActivationEmail(ActivationEmail):
    template_name = "email/activation.html"


class CustomPasswordResetEmail(PasswordResetEmail):
    template_name = "email/password_reset.html"
