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
    # Jan visits the site
    browser.get('http://localhost:8000')

    # He notices the title and header reference the site name
    site_name = 'Scout'
    assert site_name in browser.title
    header_text = browser.find_element_by_tag_name('h1').text
    assert site_name in header_text

    # He is invited to search for code snippets
    expected_search_prompt = 'Enter some code-related keywords'
    search_box = browser.find_element_by_id('search_box')
    actual_search_prompt = search_box.get_attribute('placeholder')
    assert actual_search_prompt == expected_search_prompt

    assert False, 'incomplete test'
