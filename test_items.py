link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_existing_of_add_button_into_cart(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button is not None
