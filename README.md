### Selenium

- Allow automatize several process on a browser
- It means that everything what an user can do could be programed
- It support several languages such as python, java, javascript, etc
- Compatible with popular browsers like Chrome and Firefox, you just have to install its drivers
-------------

###Dependencies
You have to get the lastest ython version in the oficial page
Install the depencies:
Selenium: For the automatizationn
PyUnitReport: For generating reports

`$ pip install selenium
`
`$ pip install pyunitreport`

Aditionally, you have to download the driver of the browser that you will use.

-------------
####Structure

Indented 4 spaces, like `<pre>` (Preformatted Text).

    <?
        echo "Hello world!";
    ?>
    
Code Blocks (Preformatted text):

    | First Header  | Second Header |
    | ------------- | ------------- |
    | Content Cell  | Content Cell  |
    | Content Cell  | Content Cell  |

####Structure with decorators　

```python
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=r"./geckodriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10)
		
	def yourTests(self):
        driver = self.driver
        driver.get('https://www.platzi.com')
		
	@classmethod
    def tearDownClass(cls):
        cls.driver.quit()
		
if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

```
###Basic Structure　

```python
import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"./drivers/geckodriver.exe")
        driver=self.driver
        driver.get('http://google.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_text_field(self):
       pass

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)


```
follow me in github  :tw-1f60e: :tw-1f527: