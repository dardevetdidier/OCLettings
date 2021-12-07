import pytest
from django.urls import reverse

from lettings.models import Letting, Address


@pytest.fixture
def get_address():
    address = Address(
        id=1,
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA"
    )
    return address


@pytest.fixture
def get_letting(get_address):
    letting = Letting(
        id=1,
        title="Joshua Tree Green Haus /w Hot Tub",
        address=get_address
    )
    return letting


@pytest.mark.django_db
def test_index(client):
    url = reverse('lettings:index')
    print(url)
    response = client.get(url)
    expected_content = b"<title>"
    assert response.status_code == 200
    assert expected_content in response.content


@pytest.mark.django_db
def test_letting(client, get_letting):
    letting_id = get_letting.id
    print(letting_id)
    url = reverse('lettings:letting', kwargs={"letting_id": letting_id})
    print(url)
    response = client.get(url)
    expected_content = b"<title>"
    assert response.status_code == 200
    assert expected_content in response.content

