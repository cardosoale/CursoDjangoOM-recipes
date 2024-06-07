from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from utils.browser import make_edge_browser


class AuthorBaseTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_edge_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, qtd=10):
        time.sleep(10)
