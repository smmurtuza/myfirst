Feature: Vetcare Logo

  Scenario: Logo present on login page
     Given Launch chrome browser
      When open vetcare user page
      Then Verify that the logo present on page
      And close program