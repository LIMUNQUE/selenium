import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #show if element is not found
from selenium.webdriver.common.by import By # Call the exception we want to validate

class AssertionsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"../drivers/geckodriver.exe")
        driver=self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))#If there is an element with that name

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))#If there is an element with that id

    def tearDown(self) -> None:
        self.driver.quit()

    def is_element_present(self, how, what):#validate if element is present
        try:
            self.driver.find_element(by=how, value=what)#find element by id
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)