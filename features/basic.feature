Feature: Login via email and password

  Scenario: User opens BlenderKit homepage
      Given user has Chrome running
       When user opens BlenderKit
       Then page will include text "Dream in 3D"

  Scenario: User goes to login page
      Given page contains element "LOG IN button"
       When user clicks on element "LOG IN button"
       Then they are on "/accounts/login/"
        And page contains element "USERNAME input"
        And page contains element "PASSWORD input"

  Scenario: User logs into BlenderKit
       When user types <USERNAME> into element "USERNAME input"
        And user types <PASSWORD> into element "PASSWORD input"
        And user clicks on element "LOG IN submit"
       Then they are on Homepage
        And page contains element "PROFILE dropdown"

  Scenario: User goes to subscription page
      Given page contains element "SUBSCRIBE button"
       When user clicks on element "SUBSCRIBE button"
       Then they are on "/plans/pricing/"
        And page contains element "YEARLY switch"
        And page contains element "GET PLAN button"

  Scenario: User buys YEARLY FULL plan
       When user clicks on element "YEARLY switch"
        And user clicks on element "GET PLAN button"
       Then they are on "/plans/order/extend/new/6/"
