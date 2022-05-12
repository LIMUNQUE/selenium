import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"./drivers/geckodriver.exe")
        driver=self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):#Cada una es una prueba que abre una nueva ventana
        search_field = self.driver.find_element_by_id('search')#search by id

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')#search by name
        #self.driver.find_element_by_class_name('search-query')

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
