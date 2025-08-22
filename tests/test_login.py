# test_login.py

import pytest
from playwright.sync_api import Page, Playwright, sync_playwright

def test_invalid_login(page: Page):
    """
    Tests an invalid login scenario on the Herokuapp login page.
    """
    # Open the login page
    page.goto("https://the-internet.herokuapp.com/login")

    # Enter credentials
    page.fill("#username", "tomsmith")
    page.fill("#password", "wrongpassword")

    # Click the login button
    page.click("button[type=submit]")

    # Verify the error message is visible
    error_message_selector = "#flash"
    assert "Your password is invalid!" in page.text_content(error_message_selector)

    # Print success message if assertion passes
    print("TEST PASSED")

# The pytest framework will automatically detect and run this test function.
