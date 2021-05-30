# from _pytest.fixtures import FixtureManager
from pytest import fixture


@fixture(params=["Johndoe2021", "Ivanivanov1984", "Spameggs"])
def usernames(request):
    return request.param


INPUT_LIST = [
    {
        "id": 0,
        "username": "Johndoe2021",
        "firstName": "John",
        "lastName": "Doe",
        "email": "example@test.com",
        "password": "12345",
        "phone": "2020327",
        "userStatus": 0,
    },
    {
        "id": 1,
        "username": "Ivanivanov1984",
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "email": "vanya@test.com",
        "password": "54321",
        "phone": "9379992",
        "userStatus": 1,
    },
    {
        "id": 2,
        "username": "Spameggs",
        "firstName": "Spam",
        "lastName": "Eggs",
        "email": "no.imagination@at.all",
        "password": "qwerty",
        "phone": "2147483647",
        "userStatus": 1,
    },
]

SINGLE_USER = {
    "id": 3,
    "username": "gvanrossum",
    "firstName": "Guido",
    "lastName": "van Rossum",
    "email": "bdfl@python.test",
    "password": "actuallyilovephp",
    "phone": "123456789",
    "userStatus": 0,
}

INPUT_ARRAY = [
    {
        "id": 4,
        "username": "Rossgeller",
        "firstName": "Ross",
        "lastName": "Geller",
        "email": "rossgeller@test.com",
        "password": "102938",
        "phone": "918273",
        "userStatus": 1,
    },
    {
        "id": 5,
        "username": "RachelKarenGreen",
        "firstName": "Rachel",
        "lastName": "Green",
        "email": "RKG@test.com",
        "password": "pswd",
        "phone": "2554868",
        "userStatus": 1,
    },
]

HEADERS = {"Content-Type": "application/json"}

USER_TO_UPDATE = {
    "id": 42,
    "username": "Arthur",
    "firstName": "Arthur",
    "lastName": "Arthur",
    "email": "test@test.com",
    "password": "12345",
    "phone": "2020327",
    "userStatus": 0,
}

NEW_DATA = {
    "id": 42,
    "username": "Arthur",
    "firstName": "Arthur",
    "lastName": "Dent",
    "email": "test@test.com",
    "password": "12345",
    "phone": "2020327",
    "userStatus": 0,
}

USER_TO_DELETE = {
    "id": 84,
    "username": "ZaphodBeeblebrox",
    "firstName": "Zaphod",
    "lastName": "Beeblebrox",
    "email": "test@test.com",
    "password": "12345",
    "phone": "2020327",
    "userStatus": 0,
}
