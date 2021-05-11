Feature: authentication

  Scenario: create user and signin
    Given we create user with credentials
    Then user creation "succeeds"
    And user can signin

# negative case scenarioes
  Scenario: create duplicate user
    Given we create user with duplicate credentials
    Then user creation "fails"

  Scenario: create user with weak password
    Given we create new user with < 8 character password
    Then bad request error is thrown with message
    And user cannot signin

  Scenario: signin with incomplete credentials
    Given user exists
    When we signin with only username
    Then bad request error is thrown


  Scenario: signin with incorrect credentials
    Given user already exists
    When we signin with incorrect password
    Then unauthorized error is thrown with message


