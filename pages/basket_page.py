from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def check_nothing_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket has element"

    def check_message_empty(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET).text
        print(message)
        assert message == "Your basket is empty. Continue shopping", "Basket is not empty"
