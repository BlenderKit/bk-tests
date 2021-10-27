@subscribe
Feature: User buys a full plan subscription

  Scenario: User opens BlenderKit homepage
      Given user has Chrome running
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

  Scenario: User goes to subscription page
      Given page contains element "nav item SUBSCRIBE"
       When user clicks on element "nav item SUBSCRIBE"
       Then they are on "/plans/pricing/"
        And page contains element "YEARLY switch"
        And page contains element "GET PLAN button"

  Scenario: User selects YEARLY FULL plan
       When user clicks on element "YEARLY switch"
        And user clicks on element "GET PLAN button"
       Then they are on "/plans/order/extend/new/6/"

  Scenario: User confirms 30DAY GLIMPSE plan
  # TODO: Check if previously selected plan is highlitghted
  # Change contry
       When user clicks on element "30DAY GLIMPSE button"
        And user clicks on element "PAYPAL SANDBOX switch"
        And user clicks on element "TO PAYMENT button"
       Then page contains element "PAYPAL MAIL input"

  Scenario: User pays and gets her invoice
       When user types <PP_USERNAME> into element "PAYPAL MAIL input"
        And user clicks on element "PAYPAL NEXT button"
        And user types <PP_PASSWORD> into element "PAYPAL PASS input"
        And user clicks on element "PAYPAL LOGIN button"
        And user clicks on element "PAYMENT SUBMIT button"
       Then page contains element "INVOICE link"
        And page includes text "Welcome to Full plan"
