import os
from playwright.sync_api import sync_playwright

TEST_FILE = os.path.abspath("sample_upload.txt")

def test_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page.goto("https://the-internet.herokuapp.com/upload")
        page.set_input_files("input#file-upload", TEST_FILE)
        page.click("input#file-submit")

        uploaded_file_name = page.text_content("#uploaded-files")

        context.tracing.stop(path="trace_upload.zip")
        browser.close()

        assert "sample_upload.txt" in uploaded_file_name

   # Wait 3 seconds so video shows the result
    page.wait_for_timeout(3000)
