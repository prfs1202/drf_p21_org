from datetime import UTC

import factory
from apps.models import Category, User


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('company')

    class Meta:
        model = Category


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.django.Password('1')
    date_joined = factory.Faker('date_time', tzinfo=UTC)
    type = factory.Iterator(list(zip(*User.Type.choices))[0])

    # username = factory.LazyAttribute(lambda obj: '_'.join(obj.words_))

    class Meta:
        model = User

    class Params:
        words_ = factory.Faker("words", nb=2)

    @factory.lazy_attribute
    def username(self):
        return '_'.join(self.words_) + ' -- vali'
