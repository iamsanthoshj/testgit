import pytest

@pytest.fixture
def liste():
    a = 10
    b = 20
    c = 30
    return[a,b,c]

def test_liste(liste):
    assert liste[1] == 20

def test_listed(liste):
    assert liste[1] == 30
print("@hi")

