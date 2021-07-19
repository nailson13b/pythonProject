# This is a Feature file

Feature: Fill the Contact Form

  Scenario: User Login credentials

    Given Launch the App and Click on Login Button
    And I entered "abc@gmail.com" UserID
    And I entered "1234" password
    When click on Login Button
    And Home page opens
    Then Verify Home Screen