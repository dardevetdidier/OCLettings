import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_views(client):
    url = reverse('lettings:index')
    print(url)
    response = client.get(url)
    expected_content = b"<title>"
    assert response.status_code == 200
    assert expected_content in response.content


@pytest.mark.django_db
def test_letting_views(client):
    url = reverse('lettings:letting', kwargs={'letting_id': 1})
    print(url)
    response = client.get(url)
    expected_content = b"<title>"
    assert response.status_code == 200
    assert expected_content in response.content

