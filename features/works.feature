@works @wip @prod
Feature: User looks on works section
Works are located at: /gallery

  Scenario: User goes to MODELS asset gallery
      Given user has Chrome running
        And user closes disclaimers
        And user is logged in
        And page contains element "nav item WORKS"
       When user clicks on element "nav item WORKS"
       Then they are on "/gallery/"

  Scenario Outline: User looks on work detail
       When user clicks on work named "<work>"
       Then page contains clickable element "ASSET POPUP"
        And page contains clickable element "ASSET POPUP AUTHOR AVATAR"
        And element "ASSET POPUP NAME" contains text "<title>"
        And element "ASSET POPUP AUTHOR NAME" contains text "<author>"
        And user clicks on element "ASSET POPUP CLOSE"

  Examples:
    | work                 | title                | author           |
    | Gallery release      | Gallery Release      | Vilém Duha       |
    | Glasshouse           | Glasshouse           | Adam Krhanek     |
    | Kitchen              | Kitchen              | Adam Krhanek     |
