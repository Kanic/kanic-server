from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_mechanic=False):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_mechanic = is_mechanic
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(username=username, email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255,
                              unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_mechanic = models.BooleanField(verbose_name="Is Mechanic", default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined',
                                       default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return "%s %s" %(self.first_name, self.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_nested_attributes_for_serializer(self):
        '''This method is for model Request to get nested attribute of mode User'''
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        return data


class Mechanic(models.Model):
    user = models.OneToOneField(User)
    year_of_experience = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

def new_user_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.is_mechanic:
        mechanic, is_created = Mechanic.objects.get_or_create(user=instance)
    elif created:
        pass


post_save.connect(new_user_receiver, sender=User)
