

Feature: controlar assistència
"Control d'assistència a classe"

  Scenario Outline: mostrar estat alumne
    Given alumne en estat <estat>
      And profe logat
    When profe llista alumnes
    Then es mostra alumne en estat <estat>

    Examples: presencia alumne
    | estat   |
    | present |
    | falta   |


  Scenario Outline: canviar estat alumne
    Given alumne en estat <estat_inicial>
      And profe logat
    When profe canvia estat alumne a <estat_final>
    Then es mostra alumne en estat <estat_final>

    Examples: presencia alumne
    | estat_inicial | estat_final |
    | present       | falta       |
    | falta         | present     |

  Scenario: alarma fals positiu
    Given alumne en estat present
    When profe canvia estat alumne a falta
    Then senyal d'alarma per fals positiu
