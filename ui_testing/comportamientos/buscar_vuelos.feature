Feature: Busco itinerario de vuelos

  Scenario:
    Given Estando en la pagina de Mercury Tours con usuario "dcorrales" y password "123"
    When Busco un vuelo de "Paris" a "Seattle" en clase "Business" para la aerolínea "Unified Airlines"
    Then El sistema presenta lista de itinerarios de vuelos


