Feature: user login

  Scenario: user login vetcare
    Given Launch Chrome Browser
    When open login page
    And Enter username "12june@yopmail.com" and password "abc123"
    And Click on Login button
    Then user must sucessfully login on the main page
    When the user clicks the text button
    Then The user start the text chat
    And Type text message
    Then send button
    #Then the user can perform further actions

  Scenario Outline:  login vetcare with multiples parameter
    Given Launch Chrome Browser
    When open login page
    And Enter username "<username>" and password "<password>"
    And Click on Login button
    Then user must sucessfully login on the main page
    When the user clicks the text button
    Then The user start the text chat
    And Type text message
    Then send button

    Examples:
      | username| password |
      #| staxx@yopmail.com | abc123 |
      | 12june@yopmail.com | abc123 |
      #| tester.buddy2023@yopmail.com | abc123 |
      #| uservideocall@yopmail.com | abc123 |