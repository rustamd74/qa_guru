import pytest
from selene.support.shared import browser



@pytest.fixture(scope="session")
def open_browser():
    browser.open('https://google.com').driver.maximize_window()
    b = browser.open('https://google.com')
    yield b
    browser.close()



