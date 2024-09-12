import pytest
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.reverse import reverse_lazy
# 10code


# test


@pytest.mark.django_db
class TestView:
    # def test_category(self, client, categories):
    #     url = reverse_lazy('category-list')
    #     response = client.get(url)
    #     data = response.json()
    #     assert response.status_code == status.HTTP_200_OK
    #     assert len(data) == 50
    #     assert set(data[0].keys()) == {'id', 'name', 'slug'}
    #
    # def test_product(self, client, category):
    #     url = reverse_lazy('product-list')
    #     response = client.get(url)
    #     assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_users_list(self, client, users):
        url = reverse_lazy('users')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()
        assert len(response) == 4
        assert len(response['results']) == 5
        assert response['count'] == 5
        allowed_fields = {'date_joined', 'email', 'first_name', 'id', 'last_name', 'type', 'username'}
        assert set(response['results'][0]) == allowed_fields
        assert response['next'] is None
        assert response['previous'] is None

        response = client.options(url)
        http_methods = response.headers.get('Allow')
        http_methods = set(map(lambda i: i.lower(), http_methods.split(', ')))
        allowed_http_methods = {'get', 'options', 'head', 'post'}
        assert allowed_http_methods == http_methods

        page_size = 50
        url = str(reverse_lazy('users')) + '?' + urlencode({'page_size': page_size})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        response = response.json()
        assert response['next'] is None
        assert response['previous'] is None
