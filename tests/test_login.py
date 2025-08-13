from playwright.sync_api import sync_playwright

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("#username", "tomsmith")
        page.fill("#password", "wrongpassword")
        page.click("button[type='submit']")

        error_message = page.text_content("#flash")

        context.tracing.stop(path="trace_login.zip")
        browser.close()

        assert "Your password is invalid!" in error_message
   # Wait 3 seconds so video shows the result
    page.wait_for_timeout(3000)
