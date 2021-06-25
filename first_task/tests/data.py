from pytest import fixture
from typing import List
from pydantic import BaseModel, Field


class InputData(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

class ListData(BaseModel):
    each_item : List[InputData]




@fixture(params=["Johndoe2021", "Ivanivanov1984", "Spameggs"])
def usernames(request):
    return request.param


SINGLE_USER = InputData(
    id=3,
    username="gvanrossum",
    firstName="Guido",
    lastName="van Rossum",
    email="bdfl@python.test",
    password="actuallyilovephp",
    phone="123456789",
    userStatus=0
)

USER_TO_UPDATE = InputData(
    id=42,
    username="Arthur",
    firstName="Arthur",
    lastName="Arthur",
    email="test@test.com",
    password="12345",
    phone="2020327",
    userStatus=0
)

NEW_DATA = InputData(
    id=42,
    username="Arthur",
    firstName="Arthur",
    lastName="Dent",
    email="test@test.com",
    password="12345",
    phone="2020327",
    userStatus=0
)

USER_TO_DELETE = InputData(
    id=84,
    username="ZaphodBeeblebrox",
    firstName="Zaphod",
    lastName="Beeblebrox",
    email="test@test.com",
    password="12345",
    phone="2020327",
    userStatus=0
)

print(SINGLE_USER.username)