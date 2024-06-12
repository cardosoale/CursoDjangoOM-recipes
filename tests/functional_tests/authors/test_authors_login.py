from .base import AuthorsBaseTest

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_login_succesfully(self):
        string_password = 'pass'
        user = User.objects.create_user(
            username='my_user',
            password=string_password
        )

        # User opens login page
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User sees the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # User enters their username and password
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        form.submit()

        # User sees the login success message and their name
        self.assertIn(
            f'Your are logged in with {user.username}.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(self.live_server_url +
                         reverse('authors:login_create'))
        self.assertIn('Not Found', self.browser.find_element(
            By.TAG_NAME, 'body').text)

    def test_form_login_is_invalid(self):
        # User opens login page
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User sees the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # And tries to send empty values
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')

        username.send_keys(' ')
        password.send_keys(' ')

        form.submit()

        # User see an error message on your screen
        self.assertIn(
            'Invalid username or password',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_login_invalid_credentials(self):
        # User opens login page
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User sees the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # And it tries to send values with data that doesn't match
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')

        username.send_keys('invalid_username')
        password.send_keys('invalid_password')

        form.submit()

        # User see an error message on your screen
        self.assertIn(
            'Invalid credentials',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
