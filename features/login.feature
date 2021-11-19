@login
Feature: User logs into BlenderKit

  Scenario: User opens BlenderKit homepage
      Given user has Chrome running
        And user closes disclaimers
       When user opens BlenderKit
       Then page includes text "Dream in 3D"

  Scenario: User goes to login page
      Given page contains element "LOG IN button"
       When user clicks on element "LOG IN button"
       Then they are on "/accounts/login/"
        And page contains element "USERNAME input"
        And page contains element "PASSWORD input"

  Scenario: User logs into BlenderKit
       When user types <BK_USERNAME> into element "USERNAME input"
        And user types <BK_PASSWORD> into element "PASSWORD input"
        And user clicks on element "LOG IN submit"
       Then they are on Homepage
        And page contains element "PROFILE dropdown"
