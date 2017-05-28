from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        ordering = ('username', )
        db_table = 'auth_user'
