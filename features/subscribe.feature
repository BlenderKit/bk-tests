@subscribe
Feature: User buys a full plan subscription

  Scenario: User goes to subscription page
      Given user has Chrome running
        And user closes disclaimers
        And user is logged in
        And page contains element "nav item SUBSCRIBE"
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
       When user clicks on element "30DAY GLIMPSE button"

  Scenario Outline: User selects different countries
    When user selects "<country>" in dropdown menu "COUNTRY select"
     And user waits for "4" seconds
    Then element "TAX PERCENTAGE span" contains text "<tax>"
     And discount, tax and total price are calculated correctly

  Examples:
    |country | tax |
    # Non-EU Countries
    |Japan | 0 |
    |India | 0 |
    |United States of America | 0   |
    |Brazil | 0 |
    |Russia | 0 |
    |China | 0 |
    |Australia | 0 |
    |Turkey | 0 |
    |Ukraine | 0 |
    |United Kingdom | 0 |
    # European Union
    |Belgium | 21 |
    |Bulgaria | 20 |
    |Denmark | 25 |
    |Estonia | 20 |
    |Finland | 24 |
    |France | 20 |
    |Croatia | 25 |
    |Ireland | 23 |
    |Italy | 22 |
    |Cyprus | 19 |
    |Lithuania | 21 |
    |Latvia | 21 |
    |Luxembourg | 17 |
    |Hungary | 27 |
    |Malta | 18 |
    |Germany | 19 |
    |Netherlands | 21 |
    |Poland | 23 |
    |Portugal | 23 |
    |Austria | 20 |
    |Romania | 19 |
    |Greece | 24 |
    |Slovakia | 20 |
    |Slovenia | 22 |
    |Spain | 21 |
    |Sweden | 25 |
    |Czechia | 21 |

  Scenario: User selects PayPal Sandbox
       When user clicks on element "PAYPAL SANDBOX switch"
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
