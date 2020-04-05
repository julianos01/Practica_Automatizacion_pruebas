Feature: Gestionar libros

  Scenario: consultar libros
    Given estoy en la url
    When consulto todos los libros
    Then recibo una respueta valida

  Scenario: crear un  libro
    Given estoy en la url
    When creo un  libro
    Then recibo una respueta valida

  Scenario: eliminar libros
    Given estoy en la url
    When eliminar  un libros
    Then recibo una respueta valida

  Scenario: consultar libros por id
    Given estoy en la url
    When consulto libros por id
    Then recibo una respueta valida

  Scenario: Actualizar libro
    Given estoy en la url
    When Actualizo un libro
    Then recibo una respueta valida
