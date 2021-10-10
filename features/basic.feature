Feature: Login

  Scenario: User opens BlenderKit homepage
    Given user has Chrome running
     When user opens BlenderKit
     Then page will include text "Dream in 3D"

  Scenario: User goes to login page
      Given page includes element "LOG IN button"
       When user clicks on element "LOG IN button"
       Then they are on "/accounts/login/"
        And page includes element "USERNAME input"
        And page includes element "PASSWORD input"
