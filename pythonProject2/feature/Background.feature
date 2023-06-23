Feature: user login

    #Then the user can perform further actions

    Scenario :  login vetcare with multiples parameter
        Given Launch Chrome Browser
        When open log_in page
        And Please Enter username "12june@yopmail.com" and password "abc123"
        And Now Click on Login button
        Then Now user must sucessfully login on the main page

    Scenario: Update membership
        When Click on membership
        Then Click on update membership
        Then select package 
        Then click on pay