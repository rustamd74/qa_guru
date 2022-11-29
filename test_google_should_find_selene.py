from selene.support.shared import browser
from selene import be,have


def test_search_bar(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in ...'))


def test_search_bar2(open_browser):
    browser.element('[name="q"]').clear()
    browser.element('[name="q"]').should(be.blank).type('kfjhvjjhcbbccuubb').press_enter()
    browser.element('[aria-level="3"]').should(have.text('По запросу kfjhvjjhcbbccuubb ничего не найдено'))
