import requests
# voy a llamar a pytest_check como check
import pytest_check as check
import pytest

headers = {
    "x-api-key": "pub_918227ce6194bfaefbf703ec61373dea26414b05a17eb1d099cabdb6b983d48d"
}

# body = {
#     "name" : "Lara",
    
# }
# response = requests.post("https://reqres.in/api/users/2",headers=headers, json=body)
# print(response.status_code)
# print(response.json())

@pytest.mark.api
def test_login_valido():
    body = {
        "email" : "eve.holt@reqres.in",
        "password" : "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json= body)

    assert response.status_code == 200

@pytest.mark.api
def test_login_sin_password():
    body = {
        "email" : "eve.holt.reqres.in"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing password"

@pytest.mark.api
def test_login_sin_email():
    body = {
        "password" : "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers, json = body)

    body = response.json()
    assert response.status_code == 400
    assert body["error"] == "Missing email or username"

@pytest.mark.api
def test_create_user():
    body = { 
        "name" : "Pepe",
        "email" : "pepe.perez@reqres.in",
        "password" : "1234*"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)

    data = response.json()

    assert response.status_code == 201
    # check.equal(response.status_code,201)

    # assert body["email"].count("@") == 1
    check.equal(body["email"].count("@"),1)
    # assert "*" in body["password"]
    check.is_in("*", body["password"])

    # assert data["name"] == body["name"]
    check.equal(data["name"], body["name"])
    # assert data["email"] == body["email"]
    check.equal(data["email"], body["email"])

    # assert response.elapsed.total_seconds() < 2, "El tiempo de respuesta fue mayor a 2"
    check.less(response.elapsed.total_seconds(),2)

@pytest.mark.api
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 204

@pytest.mark.api
def test_get_user():
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 200
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 2, "El tiempo de respuesta fue mayor a 2"