import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
    search_box = browser.find_element_by_id('id_search_box')
    actual_search_prompt = search_box.get_attribute('placeholder')
    assert actual_search_prompt == expected_search_prompt

    # He searches "python yield"
    search_box.send_keys('python yield')
    search_box.send_keys(Keys.ENTER)

    # The page updates, and now the page shows a code snippet
    # that uses the dummy variables "mylist" and "mygenerator"
    # (the highest-voted python page on StackOverflow.com is
    #  /questions/231767/what-does-the-yield-keyword-do-in-python)
    snippets = browser.find_elements_by_tag_name('code')
    assert any(['mylist' in snippet.text and 'mygenerator' in snippet.text
                for snippet in snippets])
