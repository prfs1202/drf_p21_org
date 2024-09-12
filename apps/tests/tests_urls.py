import pytest
from rest_framework.reverse import reverse_lazy


@pytest.mark.django_db
class TestUrl:
    def test_auth(self):
        assert '/api/v1/auth/register' == reverse_lazy('register')
