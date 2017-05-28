import factory
from factory import Sequence

from accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    first_name = 'John'
    last_name = 'Doe'
    username = Sequence(lambda n: 'user-{}'.format(n))
    email = Sequence(lambda n: 'person-{}@example.com'.format(n))
    password = 'Secret123'
    is_active = True

    class Meta:
        model = User
        django_get_or_create = ('email',)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._create(model_class, *args, **kwargs)

        if password:
            user.set_password(password)
            user.clear_password = password
            user.save()
        return user


class StaffUserFactory(UserFactory):
    is_staff = True


class SuperUserFactory(StaffUserFactory):
    is_superuser = True
