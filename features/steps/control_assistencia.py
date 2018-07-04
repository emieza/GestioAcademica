
from behave import *
from app import *

ALUMNE_TEST_ID = 2233

@given("alumne en estat {estat}")
def step_impl(context,estat):
    context.alumne = context.classe.crea_alumne( ALUMNE_TEST_ID )
    context.alumne.estat = estat

@given("profe logat")
def step_impl(context):
    context.profe = Profe()
    context.profe.loga("enric","enric123")

@when("profe llista alumnes")
def step_impl(context):
    pass

@then("es mostra alumne en estat {estat}")
def step_impl(context,estat):
    print(estat,context.alumne.estat)
    assert context.alumne.estat == estat


@when("profe canvia estat alumne a {estat}")
def step_impl(context,estat):
    context.alumne.estat = estat

@then("senyal d'alarma per fals positiu")
def step_impl(context):
    pass

