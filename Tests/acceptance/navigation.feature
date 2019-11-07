Feature: User can navigate to patient management application and create a patient card

  Scenario: User navigates to homepage and creates patient card
    Given User is on the patient management app homepage
    When User  enters "Veronica" in the "firstName" field
    And User enters "Ann" in the "middleName" field
    And User enters "Bansah" in the "lastName" field
    And User enters "024-763-2527" in the "phoneNumber" field
    And User enters "03 - 27 - 90" in the "dob" field
    And User enters "Egret Lane" in the "address" field
    And User clicks on the Add New User button
    Then Patient card is created
