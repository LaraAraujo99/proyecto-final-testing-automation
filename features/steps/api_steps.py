from behave import given,when,then
import requests

headers = {
    "x-api-key": "pub_918227ce6194bfaefbf703ec61373dea26414b05a17eb1d099cabdb6b983d48d"
}

@given("la API de Reqres esta disponible")
def step_impl(context):
    context.base_url = "https://reqres.in/api"

# Scenario 1
@when("realizar un login valido")
def step_impl(context):
    body = { 
        "email" : "eve.holt@reqres.in",
        "password" : "cityslicka"
    }

    context.response = requests.post(f"{context.base_url}/login", headers=headers, json=body)
# :d Indica que el valor que se está reemplazando lo pasa a nro entero
# :f Indica que el valor que se está reemplazando lo pasa a nro decimal

@then("el status code debe ser {status_code:d}")
def step_impl(context,status_code):
    assert context.response.status_code == status_code

# Scenario 2
@when("realizar un login sin contraseña")
def step_impl(context):
    body = { 
        "email" : "eve.holt@reqres.in"
    }

    context.response = requests.post(f"{context.base_url}/login", headers=headers, json=body)

@then("el mensaje de error debe ser '{mensaje}'")
def step_impl(context, mensaje):
    body = context.response.json()
    assert body["error"] == mensaje

