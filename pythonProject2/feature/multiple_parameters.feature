Feature: user login

    #Then the user can perform further actions

  Scenario Outline:  login vetcare with multiples parameter
    Given Launch Chrome Browser
    When open log_in page
    And Please Enter username "<username>" and password "<password>"
    And Now Click on Login button
    Then Now user must sucessfully login on the main page
    When after the user clicks the text button
    When select chat type
    When then The user start the text chat
    And now Type text message
    Then click on send button

    Examples:
      | username| password |
      | staxx@yopmail.com | abc123 |
      | 12june@yopmail.com | abc123 |
      #| tester.buddy2023@yopmail.com | abc123 |
      #| uservideocall@yopmail.com | abc123 |