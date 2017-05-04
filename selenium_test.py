import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome('./chromedriver')
#driver.get('localhost:8000/home');
#assert "JEA and Books" in driver.title

#elem = driver.find_element_by_name('searchquery')
#elem.clear()
#elem.send_keys('Goats' + Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.quit()

class searchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_search(self):
        driver = self.driver
        driver.get('localhost:8000/home')
        self.assertIn("JEA and books",driver.title)
        elem = driver.find_element_by_name("searchquery")
        elem.send_keys("Goats")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()