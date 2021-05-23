import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.


class UUIDmodel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class User(AbstractUser, UUIDmodel):
    USERNAME_FIELD = "email"

    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)

    username = models.CharField(
        _("username"),
        max_length=50,
        unique=False,
        help_text=_(
            "Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        null=False,
        blank=True,
        default="",
    )
