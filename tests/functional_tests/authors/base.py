from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from utils.browser import make_edge_browser
from selenium.webdriver.common.by import By


class AuthorsBaseTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_edge_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, qtd=10):
        time.sleep(10)

    def get_by_placeholder(self, form, placeholder):
        return form.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]'
        )
