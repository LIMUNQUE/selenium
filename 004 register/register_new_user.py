import unittest
from selenium import webdriver
from api_data_mock import ApiDataMock


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"../drivers/geckodriver.exe")
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() & create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and news_letter_subscription.is_enabled()
                        and submit_button.is_enabled())

        first_name.send_keys(ApiDataMock.first_name)
        middle_name.send_keys(ApiDataMock.middle_name)
        last_name.send_keys(ApiDataMock.last_name)
        email_address.send_keys(ApiDataMock.email_address)
        password.send_keys(ApiDataMock.password)
        confirm_password.send_keys(ApiDataMock.password)
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(15)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)