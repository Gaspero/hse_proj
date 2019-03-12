Feature: As a website owner, I want to secure my website

  Scenario: Get root page
     Given APP is setup
      When i call root page
      Then i should see the alert "Hello World!"

#  Scenario: Incorrect Username
#     Given APP is setup
#      When i login with "monty" and "default"
#      Then i should see the alert "Invalid username"
#
#  Scenario: Incorrect Password
#     Given APP is setup
#      When i login with "admin" and "python"
#      Then  i should see the alert "Invalid password"
#
#  Scenario: Logout
#     Given APP is setup
#           and i login with "admin" and "default"
#      When i logout
#      Then  i should see the alert "You were logged out"