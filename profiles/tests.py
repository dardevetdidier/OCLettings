import pytest
from django.urls import reverse
from mixer.backend.django import mixer
from django.test import RequestFactory

from profiles.models import Profile
from profiles.views import index, profile


@pytest.mark.django_db
class TestViews:

    def test_index(self):
        path = reverse('profiles:index')
        request = RequestFactory().get(path)
        print(request)
        response = index(request)
        expected_content = b"<title>"
        assert response.status_code == 200
        assert expected_content in response.content

    def test_profile(self):
        path = reverse('profiles:profile', kwargs={'username': "test"})
        request = RequestFactory().get(path)
        request.profile = mixer.blend(Profile)
        print(request.profile)
        response = profile(request, username=request.profile)
        expected_content = f"<title>{request.profile}</title>"
        assert response.status_code == 200
        assert expected_content in response.content.decode('utf-8')
