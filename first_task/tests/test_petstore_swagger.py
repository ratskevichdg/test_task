import requests
import json
from requests.api import head
from data import (
    usernames,
    INPUT_LIST,
    HEADERS,
    SINGLE_USER,
    USER_TO_UPDATE,
    NEW_DATA,
    USER_TO_DELETE,
    INPUT_ARRAY,
)


def test_create_with_list():
    response = requests.post(
        "https://petstore.swagger.io/v2/user/createWithList",
        data=json.dumps(INPUT_LIST),
        headers=HEADERS,
    )
    assert response.status_code == 200
    assert response.json()["message"] == "ok"


def test_get_user(usernames):
    response = requests.get(
        f"https://petstore.swagger.io/v2/user/{usernames}",
        headers=HEADERS,
    )
    assert response.status_code == 200
    assert response.json()["username"] == usernames


def test_update_user():
    requests.post(
        "https://petstore.swagger.io/v2/user",
        data=json.dumps(USER_TO_UPDATE),
        headers=HEADERS,
    )
    old = requests.get(
        f"https://petstore.swagger.io/v2/user/{USER_TO_UPDATE['username']}",
        headers=HEADERS,
    ).json()["lastName"]
    response = requests.put(
        f"https://petstore.swagger.io/v2/user/{USER_TO_UPDATE}",
        data=json.dumps(NEW_DATA),
        headers=HEADERS,
    )
    new = requests.get(
        f"https://petstore.swagger.io/v2/user/{USER_TO_UPDATE['username']}",
        headers=HEADERS,
    ).json()["lastName"]
    assert response.status_code == 200
    assert new != old


def test_delete_user(usernames):
    requests.post(
        "https://petstore.swagger.io/v2/user",
        data=json.dumps(USER_TO_DELETE),
        headers=HEADERS,
    )
    response = requests.delete(
        f"https://petstore.swagger.io/v2/user/{USER_TO_DELETE['username']}",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    response1 = requests.get(
        f"https://petstore.swagger.io/v2/user/{USER_TO_DELETE['username']}",
        headers={"Content-Type": "application/json"},
    )
    assert response1.status_code == 404


def test_user_login():
    response = requests.get(
        f"https://petstore.swagger.io/v2/user/login",
        headers=HEADERS,
        auth=("Johndoe2021", "1234"),
    )
    assert response.status_code == 200


def test_user_logout():
    response = requests.get(
        f"https://petstore.swagger.io/v2/user/logout",
        headers=HEADERS,
    )
    assert response.status_code == 200


def test_create_with_array():
    response = requests.post(
        "https://petstore.swagger.io/v2/user/createWithArray",
        data=json.dumps(INPUT_ARRAY),
        headers=HEADERS,
    )
    recently_added_user = requests.get(
        f"https://petstore.swagger.io/v2/user/{INPUT_ARRAY[0]['username']}"
    )
    assert recently_added_user.json()["username"] == INPUT_ARRAY[0]["username"]
    assert response.status_code == 200


def test_create_user():
    response = requests.post(
        "https://petstore.swagger.io/v2/user",
        data=json.dumps(SINGLE_USER),
        headers=HEADERS,
    )
    recently_added_user = requests.get(
        f"https://petstore.swagger.io/v2/user/{SINGLE_USER['username']}"
    )
    assert recently_added_user.json()["username"] == SINGLE_USER["username"]
    assert response.status_code == 200
