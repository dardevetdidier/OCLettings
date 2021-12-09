import pytest
from django.urls import reverse
from django.test import RequestFactory

from oc_lettings_site.views import index


@pytest.mark.django_db
class TestViews:

    def test_index(self):
        path = reverse('index')
        request = RequestFactory().get(path)
        print(request)
        response = index(request)
        expected_content = "<title>Holiday Homes</title>"
        assert response.status_code == 200
        assert expected_content in response.content.decode('utf-8')
