Feature: Test Google service

  Scenario: Value search
    Given Launch Chrome browser
    When Open Google page
    Then Input value in search field
    Then Check search result
    And Close browser
