Feature: Realizar reserva

    Scenario:
        Given Que he seleccionado un itinerario de vuelo ida y vuelta con el usuario "dcorrales" y password "123"
        When Ingreso informacion personal nombre "Duvan" apellido "Corrales" comida "Hindu"
         And Ingreso informacion de medio pago: "Visa" "1234567890" "06" "2010"
         And Ingreso direccion de facturacion: "Av siempre viva" "Springfield"
         And Indico direccion de entrega: "Calle 456" "New York"
        Then Hago compra segura
         And Se genera confirmacion del vuelo