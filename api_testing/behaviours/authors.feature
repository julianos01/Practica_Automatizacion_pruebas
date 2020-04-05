Feature: Gestionar autores

  Scenario: consultar autores
    Given estoy en la url
    When consulto todos los autores
    Then recibo una respueta valida

  Scenario: crear un  autor
    Given estoy en la url
    When creo un  autor
    Then recibo una respueta valida

  Scenario: eliminar autores
    Given estoy en la url
    When eliminar  un autor
    Then recibo una respueta valida

  Scenario: consultar autores por id
    Given estoy en la url
    When consulto autores por id
    Then recibo una respueta valida

  Scenario: Actualizar autor
    Given estoy en la url
    When Actualizo un autor
    Then recibo una respueta valida
