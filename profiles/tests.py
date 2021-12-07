import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    url = reverse('profiles:index')
    print(url)
    response = client.get(url)
    expected_content = b"<title>"
    assert response.status_code == 200
    assert expected_content in response.content


