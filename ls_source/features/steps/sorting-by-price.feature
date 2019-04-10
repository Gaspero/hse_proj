# Created by ivanshadrin at 2019-04-10
Feature: Removing themes from course
  #I want to learn Vue.js
  #I don't want to repeat JS-basics that I'm already know
  #I master JS

  Scenario: Removing unnecessary themes from an already made course
    Given there is a course that includes JS-basics, Vue.js and other frameworks lessons
        | name           | type     |
        | Closures       | Basics   |
        | Redux          | React    |
        | Vuex           | Vue.js   |
        | Vue-router     | Vue.js   |
    When I remove JS-basics and other frameworks themes from my course's roadmap
    Then the system rearranges a list of themes
    And the system recounts total points that could be got