
from behave import *
from models import *

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
    context.firefox.get("http://localhost:5000/llistat_alumnes")
    titol = context.firefox.find_element_by_tag_name("h2")
    assert titol.text == "Llistat d'alumnes"

@then("es mostra alumne en estat {estat}")
def step_impl(context,estat):
    context.firefox.get("http://localhost:5000/llistat_alumnes")

    #print(estat,context.alumne.estat)
    #assert context.alumne.estat == estat


@when("profe canvia estat alumne a {estat}")
def step_impl(context,estat):
    context.alumne.estat = estat

@then("senyal d'alarma per fals positiu")
def step_impl(context):
    pass


# SELENIUM TESTS
################
#https://www.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example

from selenium.webdriver.common.by import By

@given("web en marxa")
def step_impl(context):
    context.firefox.get("https://wiket.esteveterradas.cat")

@when('profe es loga amb "{user}" i "{passw}"')
def step_impl(context,user,passw):
    # accedim a login page
    context.firefox.get("https://wiket.esteveterradas.cat/index.php?title=Especial:Registre_i_entrada&returnto=P%C3%A0gina+principal")
    userbox = context.firefox.find_element_by_id("wpName1")
    passbox = context.firefox.find_element_by_id("wpPassword1")
    submit = context.firefox.find_element_by_id("wpLoginAttempt")
    # introduim dades
    userbox.clear()
    userbox.send_keys(user)
    passbox.clear()
    passbox.send_keys(passw)
    # enviem
    submit.click()
    #submit.submit()
    # check
    userid = context.firefox.find_element(By.XPATH,"//li[@id='pt-userpage']/a[@class='new']")
    assert userid.text == "Bddtest"

@then("usuari {user} logat")
def step_impl(context,user):
    pass

