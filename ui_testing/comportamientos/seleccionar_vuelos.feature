Feature: Seleccion vuelo

  Scenario:
    Given Estando en la pagina de seleccion de vuelos disponibles con usuario "dcorrales" y password "123"
    When Selecciono un vuelo de ida y vuelta
    Then El sistema presenta la pagina de reserva de vuelos