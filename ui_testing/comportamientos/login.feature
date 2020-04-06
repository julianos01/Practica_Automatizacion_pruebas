Feature: login en Mercury Tours

  Scenario:
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "dcorrales" y un password "123"
    Then El sistema me autentica como usuario legitimo