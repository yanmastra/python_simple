from django.contrib.auth.hashers import (
    check_password as auth_check_password, make_password,
)
from django.db import models


# Create your models here.
class User(models.Model):
    REQUIRED_FIELDS = ['id', 'password', 'access', 'enable']
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=255, null=False, default='123456')
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def natural_key(self):
        return self.get_username(),

    def get_username(self):
        return self.username

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(password: str):
            self.set_password(password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return auth_check_password(raw_password, self.password, setter)

    class Meta:
        db_table = 'user_auth'
