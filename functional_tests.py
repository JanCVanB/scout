from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def browser(request):
    browser_ = webdriver.Firefox()

    def fin():
        browser_.quit()
    request.addfinalizer(fin)

    return browser_


def test_can_show_a_relevant_code_snippet(browser):
    browser.get('http://localhost:8000')

    assert 'Django' in browser.title
