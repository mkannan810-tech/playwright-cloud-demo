from playwright.sync_api import Page
import os

def test_file_upload(page: Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    
    # Create a dummy file for upload
    file_path = os.path.abspath("dummy.txt")
    with open(file_path, "w") as f:
        f.write("This is a test file.")

    # Upload the file
    page.set_input_files("#file-upload", file_path)
    page.click("#file-submit")

    # Verify upload message
    assert "File Uploaded!" in page.text_content("h3")

    # Wait 3 seconds so video shows the result
    page.wait_for_timeout(3000)
