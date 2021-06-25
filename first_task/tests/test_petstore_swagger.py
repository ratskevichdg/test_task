HEADERS = {"Content-Type": "application/json"}


from data import InputData
import requests
import json
from pytest import mark
from pydantic.schema import schema

from data import (
    usernames,
    SINGLE_USER,
    USER_TO_UPDATE,
    NEW_DATA,
    USER_TO_DELETE,
    BaseModel
)


@mark.create
def test_create_user():
    response = requests.post(
        "https://petstore.swagger.io/v2/user",
        data=SINGLE_USER.json(),
        headers=HEADERS,
    )
    recently_added_user = requests.get(
        f"https://petstore.swagger.io/v2/user/{SINGLE_USER.username}"
    )
    assert recently_added_user.json()["username"] == SINGLE_USER.username
    assert response.status_code == 200

@mark.read
def test_get_user(usernames):
    response = requests.get(
        f"https://petstore.swagger.io/v2/user/{usernames}",
        headers=HEADERS,
    )
    assert response.status_code == 200
    assert response.json()["username"] == usernames

@mark.update
def test_update_user():
    # Create new user
    requests.post(
        "https://petstore.swagger.io/v2/user",
        data=USER_TO_UPDATE.json(),
        headers=HEADERS,
    )
    # Check his lastname
    old = requests.get(
        f"https://petstore.swagger.io/v2/user/{USER_TO_UPDATE.username}",
        headers=HEADERS,
    ).json()["lastName"]
    # Change user info
    response = requests.put(
        f"https://petstore.swagger.io/v2/user/{USER_TO_UPDATE}",
        data=NEW_DATA.json(),
        headers=HEADERS,
    )
    # Check his lastname after editing
    new = requests.get(
        f"https://petstore.swagger.io/v2/user/{USER_TO_UPDATE.username}",
        headers=HEADERS,
    ).json()["lastName"]
    assert response.status_code == 200
    # Check is new lastname not equal old lastname
    assert new != old

@mark.delete
def test_delete_user(usernames):
    # Create new user
    requests.post(
        "https://petstore.swagger.io/v2/user",
        data=USER_TO_DELETE.json(),
        headers=HEADERS,
    )
    # Delete user
    response = requests.delete(
        f"https://petstore.swagger.io/v2/user/{USER_TO_DELETE.username}",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    # Try to get deleted user
    response_after_deleting = requests.get(
        f"https://petstore.swagger.io/v2/user/{USER_TO_DELETE.username}",
        headers={"Content-Type": "application/json"},
    )
    assert response_after_deleting.status_code == 404
