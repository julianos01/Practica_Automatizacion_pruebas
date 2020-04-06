from behave import *
from test.buscar_vuelos import BuscarVuelosTest

test = BuscarVuelosTest()

@given(u'Estando en la pagina de Mercury Tours con usuario "{user}" y password "{passw}"')
def step_impl(context, user, passw):
    test.setUpClass()
    test.test_go_url('http://newtours.demoaut.com/')

    context.user = user
    context.password = passw
    test.test_login(context.user, context.password)

@when(u'Busco un vuelo de "{origen}" a "{destino}" en clase "{clase}" para la aerolínea "{aerolinea}"')
def step_impl(context, origen, destino, clase, aerolinea):
    context.origen = origen
    context.destino = destino
    context.clase = clase
    context.aerolinea = aerolinea
    test.test_buscar_vuelo(context.origen, context.destino, context.clase, context.aerolinea)

@then(u'El sistema presenta lista de itinerarios de vuelos')
def step_impl(context):
    test.test_image_select_flight()
    test.tearDownClass()

@Given(u'Estando en la pagina de seleccion de vuelos disponibles con usuario "{user}" y password "{passw}"')
def step_impl(context, user, passw):
    test.setUpClass()
    test.test_go_url('http://newtours.demoaut.com/')

    context.user = user
    context.passw = passw
    test.test_login(context.user, context.passw)
    test.test_buscar_vuelo('Paris','Seattle','Business','Unified Airlines')

@when(u'Selecciono un vuelo de ida y vuelta')
def step_impl(context):
    test.test_seleccionar_vuelo()

@then(u'El sistema presenta la pagina de reserva de vuelos')
def step_impl(context):
    test.test_image_book_flight()
    test.tearDownClass()

@given(u'Que he seleccionado un itinerario de vuelo ida y vuelta con el usuario "{user}" y password "{passw}"')
def step_impl(context,user,passw):
    test.setUpClass()
    test.test_go_url('http://newtours.demoaut.com/')

    context.user = user
    context.passw = passw
    test.test_login(context.user, context.passw)
    test.test_buscar_vuelo('Paris','Seattle','Business','Unified Airlines')
    test.test_seleccionar_vuelo()

@when(u'Ingreso informacion personal nombre "{nombre}" apellido "{apellido}" comida "{comida}"')
def step_impl(context, nombre, apellido, comida):
    context.nombre = nombre
    context.apellido = apellido
    context.comida = comida
    test.test_info_personal(context.nombre, context.apellido, context.comida)
    #test_ingreso_info_personal(context, context.nombre, context.apellido, context.comida)

@when(u'Ingreso informacion de medio pago: "{tc}" "{nro_tc}" "{mes_exp}" "{anno_exp}"')
def step_impl(context, tc, nro_tc, mes_exp, anno_exp):
    context.tc = tc
    context.nro_tc = nro_tc
    context.mes_exp = mes_exp
    context.anno_exp = anno_exp
    test.test_ingreso_info_pago(context.tc, context.nro_tc, context.mes_exp, context.anno_exp)

@when(u'Ingreso direccion de facturacion: "{direccion}" "{ciudad}"')
def step_impl(context, direccion, ciudad):
    context.direccion = direccion
    context.ciudad = ciudad
    test.test_ingreso_info_direccion(context.direccion, context.ciudad)

@when(u'Indico direccion de entrega: "{direccion}" "{ciudad}"')
def step_impl(context, direccion, ciudad):
    context.direccion = direccion
    context.ciudad = ciudad
    test.test_ingreso_direccion_entrega(context.direccion, context.ciudad)

@then(u'Hago compra segura')
def step_impl(context):
    test.test_compra()

@then(u'Se genera confirmacion del vuelo')
def step_impl(context):
    test.test_image_flight_confirmation()
    test.tearDownClass()