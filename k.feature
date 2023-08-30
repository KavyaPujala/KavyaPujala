Feature:Registration for given data
  Scenario Outline:Successfully registration
    Given Open browser
    And Enter email "<email>" and password "<password>"
    Then Click signup button for successfully registration
    Examples:
      | email | password |
    |kavyap2899@gmail.com|987654|