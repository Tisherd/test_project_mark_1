from .pages.product_page import ProductPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


# @pytest.mark.parametrize('link', urls)

# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   8, 9])
# def test_guest_can_add_product_to_basket(browser, link):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.press_button_add_to_basket()
    # page.solve_quiz_and_get_code()
    # page.should_be_message_about_adding()
    # page.should_be_message_basket_total()

@pytest.mark.xfail(reason="parce qu we have element")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_not_message_about_add()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_message_about_add()

@pytest.mark.xfail(reason="parce qu element not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_not_message_about_add_disappeared()