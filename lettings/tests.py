import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from django.test import RequestFactory

from lettings.models import Letting
from lettings.views import index, letting


@pytest.mark.django_db
class TestViews:

    def test_index(self):
        path = reverse('lettings:index')
        request = RequestFactory().get(path)
        print(request)
        response = index(request)
        expected_content = "<title>Lettings</title>"
        assert response.status_code == 200
        assert expected_content in response.content.decode('utf-8')

    def test_letting(self):
        path = reverse('lettings:letting', kwargs={'letting_id': 1})
        request = RequestFactory().get(path)
        request.letting = mixer.blend(Letting)
        print(request)
        response = letting(request, letting_id=1)
        expected_content = f"<title>{request.letting}</title>"
        assert response.status_code == 200
        assert expected_content in response.content.decode('utf-8')
