import uuid
from typing import List

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password

# Create your models here.


class UUIDmodel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-date_created"]
    
    def __str__(self):
        return str(self.id)


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, UUIDmodel):
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

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []