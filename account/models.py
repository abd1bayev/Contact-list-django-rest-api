from django.db import models
from contact_list.models import Contact
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Djangoga bizning foydalanuvchi modelimiz bilan ishlashga yordam beradi"""

    def create_user(self, email, full_name, password=None, is_admin=False, is_staff=False,
                    is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Tizimimizda "foydalanuvchi profili" ni ifodalaydi."""
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True,)
    gender = models.CharField(max_length=255, blank=True, default='rather_not_say')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)
    phone_numbers = models.ManyToManyField((Contact), blank=True)


    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'gender']  # Email & Password are required by default.

    objects = UserProfileManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
         # The user is identified by their email address
         return self.email

    def __str__(self):              # __unicode__ on Python 2
         return self.email

    @staticmethod
    def has_perm(perm, obj=None):
         # "Does the user have a specific permission?"
         # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
         # "Does the user have permissions to view the app `app_label`?"
         # Simplest possible answer: Yes, always
         return True

    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         return self.staff

    @property
    def is_admin(self):
         # "Is the user a admin member?"
         return self.admin

    @property
    def is_active(self):
         # "Is the user active?"
         return self.active
