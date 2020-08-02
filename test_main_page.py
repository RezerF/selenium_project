'''
добавить в корзину
проверить, что есть сообщение об успешном добавлении в корзину
перейти к написанию отзыва
проверить, что есть название, цена, описание товара
вернуться на главную

Обратите внимание, что все проверки у нас тоже становятся отдельными методами. В самом тест-кейсе
не остается никаких вспомогательных слов типа assert, только описание шагов. Прямо как
 в нашей тестовой документации
'''
import pytest
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "https://bike-centre.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

def test_guest_can_go_to_reg_form(browser):
    link = "https://bike-centre.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(page.browser, page.browser.current_url)
    login_page.go_to_reg_form()
    login_page.should_be_login_page()












