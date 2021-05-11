Feature: boards

  @signin
  Scenario: create new board
    Given we create board with correct payload
    Then board creation "succeeds"
    And board can be fetched by ID

  @signin
  Scenario: create invalid board
    Given we create board with incorrect payload
    Then board creation "fails"

  @signin
  Scenario: fetch non existent board
    Given we fetch non existent board by id
    Then board not found error is thrown

  @signin
  Scenario: delete existing board
    Given board exists
    When board is deleted by ID
    Then board deletion succeeds
    And board cannot be fetched by ID

  #list of boards
  @signin
  Scenario: fetch boards list
    Given a set of boards
    When we fetch boards list
    Then boards are returned

  @signin
  Scenario: search boards by title
    Given a set of boards
    When we fetch boards list with search parameter
    Then relevant boards are returned

  @signin
  Scenario: filter boards by created time
    Given a set of boards
    When we fetch boards list with filter parameter
    Then related boards are returned

  @signin
  Scenario: sort boards by description
    Given a set of boards
    When we fetch boards list with sort parameter
    Then boards are returned right order

  @signin
  Scenario: fetch boards using pagination
    Given a set of boards
    When we fetch boards with pagination parameters
    Then verify relevant boards are returned



