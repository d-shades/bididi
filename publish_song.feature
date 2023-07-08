Feature: Song
    A song flow.

    Scenario: Publish the song
        Given I have a song
        When I publish the song
        Then I have a song in collection

    Scenario: Play a song
        Given I have a song
        When I play the song
        Then the times listened increases