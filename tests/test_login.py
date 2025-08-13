from playwright.sync_api import Page

def test_invalid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "wrongpassword")
    page.click("button[type='submit']")

    # Verify error message
    assert "Your password is invalid!" in page.text_content("#flash")

    # Wait 3 seconds so video shows the result
    page.wait_for_timeout(3000)
