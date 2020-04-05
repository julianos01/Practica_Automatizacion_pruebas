from behave import *
from test.test_authors import ApiRequestsActivities

test = ApiRequestsActivities()

response_codes=[]

@given(u'estoy en la url')
def step_impl(context):
    context.url = "https://fakerestapi.azurewebsites.net/api"


@when(u'consulto todos los autores')
def step_impl(context):
    test.test_get_all_authors()




@then(u'recibo una respueta valida')
def step_impl(context):
    test.test_response()


@when(u'creo un  autor')
def step_impl(context):
    test.test_create_author()


@when(u'eliminar  un autor')
def step_impl(context):
    test.test_delete_authors()


@when(u'consulto autores por id')
def step_impl(context):
    test.test_get_authors()


@when(u'Actualizo un autor')
def step_impl(context):
    test.test_put_author()


@when(u'consulto todos los libros')
def step_impl(context):
    test.test_get_all_books()


@when(u'creo un  libro')
def step_impl(context):
    test.test_create_books()


@when(u'eliminar  un libros')
def step_impl(context):
    test.test_delete_books()


@when(u'consulto libros por id')
def step_impl(context):
    test.test_get_book()


@when(u'Actualizo un libro')
def step_impl(context):
    test.test_put_book()
