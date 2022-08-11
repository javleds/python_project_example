import pytest
from src.person import Person

def test_person_to_string() -> None:
    person = Person('Javier', 'Ledezma')
    assert person.__str__() == 'Javier Ledezma'