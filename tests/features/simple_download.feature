Feature: Download files with no complications

  Scenario: Download Google's robots.txt
    Given a manifest file with contents
    """
    http://www.google.com/robots.txt
    """
    When I run earthdatagrab
    Then the file "robots.txt" containing "User-agent:" should have been downloaded within 10 seconds
